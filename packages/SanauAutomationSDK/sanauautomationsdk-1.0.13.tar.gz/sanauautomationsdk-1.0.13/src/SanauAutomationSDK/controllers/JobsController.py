from ..api.Wrapper import Wrapper
from ..api.arm.handlers.AlertsHandler import AlertsHandler
from ..utils.logutils import logger

from peewee import fn
from datetime import datetime, timezone
from typing import Callable

import json


class JobsController:

    def __init__(self, job_class, execute: Callable, get_db: Callable, api_wrapper: Wrapper):
        self.job_class = job_class
        self.execute = execute
        self.get_db = get_db
        self.alerts_handler = AlertsHandler(api_wrapper)

    def execute_job(self, job):
        try:
            logger.info(f'Starting job {job.id} - {job.task}! Wish me luck!')
            job.status = 'started'
            job.summary = '{}'
            job.started_at = datetime.now(timezone.utc)
            job.tries += 1
            job.save()

            self.execute(job)

            job.completed_at = datetime.utcnow()
            job.status = 'completed'
            job.save()
            logger.info(f'Job {job.id} - {job.task} completed!')

        except Exception as e:
            logger.info(f'Ehhhh! {e}')
            self.update_summary(job_id=job.id, name='Ошибка!', status='failed', message=str(e))

            if (7 <= datetime.now().hour <= 18) or job.tries >= 10:
                logger.info(f'Im done :(')
                job.status = 'failed'
                job.completed_at = datetime.utcnow()
            else:
                logger.info(f'I will try again later!')
                job.status = 'pending'
            job.save()

        finally:
            self.check_last_job(job)

    def enqueue(self, database_id, name, task, params=None, priority=None):
        if params is None: params = {}
        if priority is None: priority = 2
        if task in self.job_class.related_job.keys():
            related_jobs = dict()
            related_jobs['required_jobs'] = self.job_class.related_job[task]
        else:
            related_jobs = {}

        job = self.job_class.select().where(
            (self.job_class.database_id == 694),
            (self.job_class.task == 'check_vat_limit_current'),
            (self.job_class.status << ['pending', 'started'])
        ).order_by(self.job_class.__class__.created_at.desc()).get_or_none()

        if job is None:
            job = self.job_class.create(name=name, task=task, database_id=database_id, params=params, priority=priority,
                                        related_jobs=related_jobs)
        else:
            job = self.job_class.update(status='pending').where((self.job_class.id == job.id)).execute()

        return job

    def update_summary(self, job_id, name, status, message):
        job = self.job_class.get_or_none(id=job_id)
        job_summary = job.summary
        summary_steps = job_summary.setdefault('steps', [])
        if len(summary_steps) == 0 or summary_steps[-1]['name'] != name:
            summary_steps.append(
                {'name': name, 'status': status, 'log': [str(datetime.now(timezone.utc)) + ' ' + message]})
        else:
            summary_steps[-1]['status'] = status
            summary_steps[-1]['log'].append(str(datetime.now(timezone.utc)) + ' ' + message)

        summary = json.dumps(job_summary, ensure_ascii=False)
        self.job_class.update(summary=summary).where((self.job_class.id == job.id)).execute()

    def get_last_job_id(self):
        query = self.job_class.select().where((self.job_class.status == 'pending')).order_by(
            self.job_class.priority.asc())
        selected_job_id = None
        if query.exists():
            for job in query:
                if self.job_class.get_or_none((self.job_class.status << ['pending', 'started']),
                                              (self.job_class.database_id == job.database_id),
                                              (self.job_class.priority < job.priority),
                                              (fn.DATE(self.job_class.created_at) == fn.DATE(job.created_at))):
                    continue
                selected_job_id = job.id
                break
        return selected_job_id if selected_job_id is not None else None

    def check_required_jobs(self, job):
        required_jobs = job.related_jobs['required_jobs'] if 'required_jobs' in job.related_jobs.keys() else []

        related_jobs = self.job_class.select().where((self.job_class.status == 'failed'),
                                                     (self.job_class.database_id == job.database_id),
                                                     (self.job_class.task << required_jobs),
                                                     (fn.DATE(self.job_class.created_at) == fn.DATE(job.created_at)))

        if not related_jobs.exists():
            return True

        name = 'Пропуск'
        status = 'failed'
        message = f"Не были выполнены обязательные джобы ({', '.join(job.name for job in related_jobs)})."
        self.update_summary(job_id=job.id, name=name, status=status, message=message, )
        self.check_last_job(job)

        return False

    def check_for_existing_job(self, job_id):
        start = self.job_class.update(status='started').where(self.job_class.id == job_id,
                                                              self.job_class.status == 'pending')
        return True if start.execute() else False

    def check_last_job(self, job):
        completed_jobs = self.job_class.select().where((self.job_class.status == 'completed'),
                                                       (self.job_class.database_id == job.database_id),
                                                       (fn.DATE(self.job_class.created_at) == fn.DATE(
                                                           job.created_at.date()))).order_by(
            self.job_class.created_at.desc()).get_or_none()

        if completed_jobs is None:
            print("Начало дня!")
            self.alerts_handler.resolve_alert(entity_id=self.get_db(job.database_id).entity_id, key="ones:database:validation:not_successful_alerts")

        unfinished_jobs = self.job_class.select().where((self.job_class.status == 'pending'),
                                                        (self.job_class.database_id == job.database_id),
                                                        (fn.DATE(self.job_class.created_at) == fn.DATE(
                                                            job.created_at.date()))).order_by(
            self.job_class.created_at.desc()).get_or_none()

        if unfinished_jobs is None:
            failed_jobs = self.job_class.select().where((self.job_class.status == 'failed'),
                                                        (self.job_class.database_id == job.database_id),
                                                        (fn.DATE(self.job_class.created_at) == fn.DATE(
                                                            job.created_at.date())))
            failed_jobs_names = []
            if failed_jobs.exists():
                failed_jobs_names = [failed_job.name for failed_job in failed_jobs]
            if job.status == 'failed':
                failed_jobs_names.append(job.name)

            if len(failed_jobs_names) > 0:
                message = ', '.join(failed_jobs_names)
                print(f"Не прошли следующие проверки: {message}")
                self.alerts_handler.create_alert(entity_id=self.get_db(job.database_id).entity_id,
                                                 key="ones:database:validation:not_successful_alerts",
                                                 message=f"Не прошли следующие проверки: {message}", severity=200)
                return True

            else:
                print("Все проверки прошли успешно!")
                self.alerts_handler.resolve_alert(entity_id=self.get_db(job.database_id).entity_id, key="ones:database:validation:not_successful_alerts")
                return True
        else:
            return False
