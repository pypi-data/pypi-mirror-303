import json
import time
import requests
from .constants import Constants


class GTFSValidator:
    def __init__(self, logger):
        self.timeout = Constants.timeout
        self.max_retries = Constants.max_retries
        self.job_id, self.url, self.error = GTFSValidator.get_info()
        self.logger = logger

    @staticmethod
    def get_info():
        payload = json.dumps({'countryCode': 'US'})
        headers = {'Content-Type': 'application/json'}
        try:
            with requests.post(Constants.JOB_URL, headers=headers, data=payload) as response:
                response.raise_for_status()
                response_obj = response.json()
                return response_obj['jobId'], response_obj['url'], None
        except requests.exceptions.RequestException as e:
            return None, None, f'Error: {e}'

    def upload(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                payload = file.read()
                headers = {'Content-Type': 'application/octet-stream'}
                with requests.put(self.url, headers=headers, data=payload) as response:
                    response.raise_for_status()
                    return True, None
        except (IOError, requests.exceptions.RequestException) as e:
            self.logger.error(f'Failed to upload the file: {e}')
            return False, f'Error uploading file: {e}'

    def get_mobility_data(self, url, count=0):
        try:
            with requests.get(url) as response:
                response.raise_for_status()
                return response.json()
        except requests.exceptions.RequestException as e:
            if count == self.max_retries:
                self.logger.info('skipping tried 5 times already')
            else:
                self.logger.error(f'Error: {e}')
                self.logger.info(f'Retrying Request Count To Get Validation Result: {count + 1}')
                time.sleep(self.timeout)
                return self.get_mobility_data(url=url, count=count + 1)
