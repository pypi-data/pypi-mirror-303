class Constants:
    JOB_URL = 'https://stg-gtfs-validator-web-mbzoxaljzq-ue.a.run.app/create-job'
    RESULT_BASE_URL = 'https://staging-gtfs-validator-results.mobilitydata.org'
    timeout = 10 # 10 seconds timeout
    max_retries = 5

    def get_result_url(self, job_id):
        return f'{self.RESULT_BASE_URL}/{job_id}/report.json'.format(job_id=job_id)

