import os
import sys
import time
import urllib
import hashlib
import urllib2
import base64
from xml.dom.minidom import parse

import requests

from servicemanager.smfile import remove_if_exists
from actions.colours import BColors


b = BColors()


class SmNpm():

    def __init__(self, context, service_name):
        self.context = context
        self.service_name = service_name
        self.service_type = context.service_type(service_name)

    @staticmethod
    def _report_hook(count, block_size, total_size):
        global start_time
        if count == 0:
            start_time = time.time()
            return
        duration = time.time() - start_time
        progress_size = int(count * block_size)
        speed = int(progress_size / (1024 * duration))
        percent = int(count * block_size * 100 / total_size)
        sys.stdout.write("\r%d%%, %d MB, %d KB/s, %d seconds passed" %
                         (percent, progress_size / (1024 * 1024), speed, duration))
        sys.stdout.flush()

    def _create_npm_extension(self):
        return ".tgz"

    @staticmethod
    def _sha_if_exists(path):
        print path
        if os.path.exists(path):
            return hashlib.sha1(open(path, 'rb').read()).hexdigest()
        else:
            return 0

    def _download_from_npm(self, npm_path, package, show_progress):
        url = self._get_protocol() + "://" + self.context.application.npm_repo_host + "/" + npm_path + package
        if show_progress:
            urllib.urlretrieve(url, package, self._report_hook)
            print("\n")
        else:
            urllib.urlretrieve(url, package)

    def _is_valid_repository(self, repository, data):
        repository_id = data.getElementsByTagName(
            "latest" + repository + "RepositoryId")[0].firstChild.nodeValue
        repo_mappings = self.context.config_value("npm")["repoMappings"]
        if not repository_id in repo_mappings.values():
            self.context.log(
                "The repositoryId " + repository_id +
                " is not in: " + str(repo_mappings.values()))
            sys.exit(-1)

    def _find_version_in_dom(self, repository, dom):
        latest = "latest" + repository
        try:
            data = dom.getElementsByTagName("artifact")[0]
        except:
            self.context.log("Unable to get latest version from npm")
            return None

        self._is_valid_repository(repository, data)
        return data.getElementsByTagName(latest)[0].firstChild.nodeValue

    def _get_protocol(self):
        protocol = "https"
        if "protocol" in self.context.config_value("npm"):
            protocol = self.context.config_value("npm")["protocol"]
        return protocol

    def _get_npm_response(self):
        binary = self.context.service_data(self.service_name)["binary"]
        npm_url = self.context.application.npm_repo_host + \
            "/" + binary["artifact"] + "/"
        url = self._get_protocol() + "://" + npm_url
        headers = {'Accept': 'application/json'}
        response = requests.get(url, headers=headers)
        return response.json()

    def _get_version_shasum(self, version):
        json_object = self._get_npm_response()
        return json_object["versions"][version]["dist"]["shasum"]

    def get_all_versions(self):
        versions = []
        json_object = self._get_npm_response();
        for release in json_object["versions"]:
            versions.append(release)
        return versions

    def download_if_necessary(self, version):
        binary = self.context.service_data(self.service_name)["binary"]
        npm_host = self.context.application.npm_repo_host
        artifact = binary["artifact"]
        filename = artifact + "-" + version + self._create_npm_extension()
        npm_path = artifact + "/-/"
        microservice_target_path = self.context.get_microservice_target_path(
            self.service_name)

        if version:
            shasum = self._get_version_shasum(version)
            # first check the shasum in order to determine if new artifact
            # download is required
            if self._sha_if_exists(microservice_target_path + filename) != shasum:
                remove_if_exists(microservice_target_path + filename)
                self.context.log("Downloading binary for '" + self.service_name + "': " + filename)
                self._download_from_npm(npm_path, filename, self.context.show_progress)
        else:
            print b.warning + "WARNING: Due to lack of version data from npm you may not have an up to date version..." + b.endc
