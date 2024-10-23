from .api.Wrapper import Wrapper
from .controllers.JobsController import JobsController
from .api.arm.handlers.TasksHandler import TasksHandler
from .classes.ArmApiCredentials import ArmApiCredentials

from typing import Callable
from datetime import datetime
import time


class Worker:

    def __init__(self, arm_api_credentials: ArmApiCredentials):
        self.api_wrapper = Wrapper(region=arm_api_credentials.country, domain=arm_api_credentials.domain, access_key=arm_api_credentials.access_key)

    def run(self, job_class, execute: Callable, get_db: Callable, load_bank_statement: Callable):
        jobs_controller = JobsController(job_class=job_class, execute=execute, get_db=get_db, api_wrapper=self.api_wrapper)
        tasks_handler = TasksHandler(api_wrapper=self.api_wrapper)

        while True:
            self.fetch_and_run_pending_job(job_class, jobs_controller)
            time.sleep(40) if ((8 <= datetime.now().hour <= 20)
                               and (0 <= datetime.today().weekday() < 5)) else time.sleep(2)

            if (8 <= datetime.now().hour <= 20) and (0 <= datetime.today().weekday() < 5):
                self.fetch_and_run_assigned_tasks(load_bank_statement=load_bank_statement, tasks_handler=tasks_handler)

    def fetch_and_run_pending_job(self, job_class, jobs_controller):
        # Gets the most top pending job
        selected_job_id = jobs_controller.get_last_job_id()

        if selected_job_id is None:
            return False
        job = job_class.get_or_none(job_class.id == selected_job_id)

        # Checks if the job is already running
        if not jobs_controller.check_for_existing_job(job):
            return False

        # Checks if the job has required jobs
        if not jobs_controller.check_required_jobs(job):
            return False

        # Starts the job
        jobs_controller.execute_job(job)

    def fetch_and_run_assigned_tasks(self, load_bank_statement: Callable, tasks_handler):
        tasks_handler.execute_tasks(load_bank_statement=load_bank_statement, status="last_task")
