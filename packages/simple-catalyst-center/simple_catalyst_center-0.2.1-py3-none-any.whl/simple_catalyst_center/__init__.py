from .rest_client.api import API
from .rest_client.resource import Resource
from .rest_client.request import make_request
from .rest_client.models import Request
from types import MethodType
import base64
import os
import logging
import time


class CiscoCatalystCenterResource(Resource):
    pass


class CiscoCatalystCenterClient(object):
    def __init__(self, url, **kwargs):
        self._log = logging.getLogger()
        self._base_url = url

        if self._base_url[:-1] != "/":
            self._base_url + "/"

        self._username = kwargs.get("username", None)
        self._password = kwargs.get("password", None)

        self.api = API(
            api_root_url=url,  # base api url
            params={},  # default params
            headers={},  # default headers
            timeout=10,  # default timeout in seconds
            append_slash=False,  # append slash to final url
            json_encode_body=True,  # encode body as json
            ssl_verify=kwargs.get("ssl_verify", None),
            resource_class=CiscoCatalystCenterResource,
            log_curl_commands=kwargs.get("log_curl_commands",False)
        )

    def __str__(self):
        return pformat(self.api.get_resource_list())

    def login(self, username=None, password=None, tenant=None):
        if username:
            self._username = username
        if password:
            self._password = password

        authstr = "Basic " + base64.b64encode(
            b":".join((self._username.encode("utf-8"), self._password.encode("utf-8")))
        ).strip().decode("utf-8")
        response = self.api.dna.system.api.v1.auth.token.create(
            headers={"Authorization": authstr}, only_body=False
        ).client_response

        try:
            self.api.headers["X-Auth-Token"] = response.json()["Token"]
        except Exception:
            self._log.error("Cannot find Token. Please check URL and credentials.")
            return False
        return True

    def wait_for_task(self, id, timeout=60):
        while timeout > 0:
            result = self.api("/dna/intent/api/v1/task")(id).get()
            timeout -= 1
            time.sleep(1)
            if "endTime" in result:
                self._log.debug(result)
                if "additionalStatusURL" in result:
                    return result["additionalStatusURL"]
                else:
                    result

    def download(self, url, path, overwrite=False, create_dir=True):
        dir_name = os.path.dirname(path)
        file_name = os.path.basename(path)

        if dir_name != file_name:
            if not os.path.isdir(dir_name) and not create_dir:
                self._log.error(
                    f"Destination directory {dir_name} not found and create_dir is False"
                )
                return False
            if dir_name:
                os.makedirs(dir_name, exist_ok=True)
            if os.path.isfile(path) and not overwrite:
                self._log.error(
                    f"Destination file {path} exists and overwrite is False"
                )
                return False
            if os.path.isdir(path):
                self._log.error(
                    f"Destination path {path} exists and is a directory. We expect it beeing a path to the destination file"
                )
                return False
        if url.startswith("/api/v1/task/"):
            url = self.wait_for_task(url.split("/")[-1])

        with open(path, "wb") as fh:
            fh.write(self.api(url).get())
        return True
