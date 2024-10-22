import uuid

from requests import HTTPError, request
from requests.auth import HTTPBasicAuth
from ..settings import TheCvesSettings

from .gen.models import Report


class TheCVESBackend:
    def __init__(self, setting: TheCvesSettings):
        self.base_url = setting.host  # TODO hard code this
        self.auth = HTTPBasicAuth(setting.username, setting.api_key)

    def _request(self, method: str, url: str, params=None, headers=None, data=None):
        try:
            res = request(method=method, url=url, params=params, auth=self.auth, headers=headers, json=data)
            if res.ok:
                return res.json()
            else:
                raise HTTPError(res.text)
        except HTTPError as e:
            raise e
        except Exception as e:
            raise e

    def get_status(self, job_id: uuid.UUID) -> Report:
        return Report(**self._request('GET', f'{self.base_url}/report/{job_id}'))

    def start_job(self, report_id: Report) -> Report:
        return Report(**self._request('POST', f'{self.base_url}/report', data=dict(report_id)))
