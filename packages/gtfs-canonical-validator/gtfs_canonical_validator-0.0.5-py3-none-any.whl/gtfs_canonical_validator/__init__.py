import logging
from .version import __version__
from .constants import Constants
from .gtfs_validator import GTFSValidator
from .models.response import Response

logging.basicConfig()


class CanonicalValidator:
    def __init__(self, zip_file):
        self.file = zip_file
        self.logger = logging.getLogger('CANONICAL_VALIDATOR')
        self.logger.setLevel(logging.INFO)
        self.uploader = GTFSValidator(logger=self.logger)

    def validate(self) -> Response:
        response = Response()
        uploader_status, uploader_error = self.uploader.upload(file_path=self.file)
        if uploader_status:
            self.logger.info(f'File uploaded with JOB ID: {self.uploader.job_id}')
            report_url = Constants().get_result_url(job_id=self.uploader.job_id)
            report = self.uploader.get_mobility_data(url=report_url)
            self.logger.info('Got Success Response From Mobility')
            errors = CanonicalValidator.parse_errors(report['notices'])
            if len(errors) > 0:
                response.error = errors
                response.info = report['notices']
            else:
                response.info = report['notices']
                response.status = True
        else:
            response.error = uploader_error

        return response

    @staticmethod
    def parse_errors(notices):
        return [item for item in notices if item.get('severity') == 'ERROR']
