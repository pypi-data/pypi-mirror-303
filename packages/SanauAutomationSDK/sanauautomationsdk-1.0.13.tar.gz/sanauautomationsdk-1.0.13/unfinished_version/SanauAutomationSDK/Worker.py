from .classes.ArmApiCredentials import ArmApiCredentials

from .controllers.JobsController import JobsController
from .api.Wrapper import Wrapper

from typing import Callable
import time


class Worker:

    def __init__(self, job_class, arm_api_credentials: ArmApiCredentials, execute: Callable, get_db: Callable):
        self.job_class = job_class
        self.jobs_controller = JobsController(job_class=job_class, execute=execute,
                                              get_db=get_db, api_wrapper=Wrapper(region=arm_api_credentials.country,
                                                                                 domain=arm_api_credentials.domain,
                                                                                 access_key=arm_api_credentials.access_key))

    def run(self):
        while True:
            # time.sleep(40) if ((8 <= datetime.now().hour <= 20)
            #                    and (0 <= datetime.today().weekday() < 5)) else time.sleep(2)
            time.sleep(5)
            self.fetch_and_run_pending_job()

    def fetch_and_run_pending_job(self):
        # Gets the most top pending job
        selected_job_id = self.jobs_controller.get_last_job_id()

        if selected_job_id is None:
            return False
        job = self.job_class.get_or_none(self.job_class.id == selected_job_id)

        # Checks if the job is already running
        if not self.jobs_controller.check_for_existing_job(job):
            return False

        # Checks if the job has required jobs
        if not self.jobs_controller.check_required_jobs(job):
            return False

        # Starts the job
        self.jobs_controller.execute_job(job)
