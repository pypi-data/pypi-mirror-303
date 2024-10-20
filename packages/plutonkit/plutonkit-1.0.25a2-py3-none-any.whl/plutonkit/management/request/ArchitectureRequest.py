import os
import subprocess
from glob import glob
from http.client import responses

import requests

from plutonkit.config import ARCHITECTURE_DETAILS_FILE
from plutonkit.config.message import ARCHITECTURE_REQUEST_ERROR_MESSAGE

from .ValidateSource import ValidateSource


class ArchitectureRequest:
    def __init__(self, path, dirs,details_file=ARCHITECTURE_DETAILS_FILE) -> None:
        self.path = path
        self.dirs = dirs
        self.validate = ValidateSource(path)
        self.isValidReq = False
        self.getValidReq = None
        self.errorMessage = ARCHITECTURE_REQUEST_ERROR_MESSAGE
        self.details_file = details_file
        self.__init_architecture()

    def __init_architecture(self):
        if self.validate.arch_type == "request":
            data = self._curl(f"{self.path}/{self.details_file}")
            if data.status_code == 200:
                self.isValidReq = True
                self.getValidReq = str(data.text)
            else:
                self.errorMessage = responses[data.status_code]
        if self.validate.arch_type == "git":

            try:
                subprocess.check_output(
                    ["git", "clone", self.validate.path],
                    cwd=self.dirs,
                    stderr=subprocess.STDOUT,
                )
                if "branch_name" in self.validate.repo_details:
                    subprocess.check_output(
                        ["git", "checkout", self.validate.repo_details["branch_name"]],
                        cwd=os.path.join(self.dirs, self.validate.repo_name),
                        stderr=subprocess.STDOUT,
                    )
                arch_file = self._read_file(self.details_file)
                self.isValidReq = arch_file["is_valid"]
                if self.isValidReq:
                    self.getValidReq = arch_file["content"]
                else:
                    self.errorMessage = arch_file["content"]

            except subprocess.CalledProcessError as clone_error:
                output = clone_error.output.decode("utf-8")
                self.errorMessage = output

        if self.validate.arch_type == "local":
            arch_file = self._read_file(self.details_file)
            self.isValidReq = arch_file["is_valid"]
            if self.isValidReq:
                self.getValidReq = arch_file["content"]
            else:
                self.errorMessage = arch_file["content"]
        if self.isValidReq is False and self.errorMessage != ARCHITECTURE_REQUEST_ERROR_MESSAGE:
            self.errorMessage = f"No `{self.details_file}` was found in local directory"

    def getBlob(self, file):
        data_glob = []
        raw_data = []
        main_dir = ""
        if self.validate.arch_type == "request":
            return [file]
        if self.validate.arch_type == "local":
            main_dir = os.path.join(self.dirs, self.path)
            data_glob =   glob(os.path.join(self.dirs, self.path, file.get("file","")))
        if self.validate.arch_type == "git":
            main_dir = os.path.join(self.dirs, self.validate.repo_name,self.validate.repo_path_dir )
            data_glob =  glob( os.path.join(self.dirs, self.validate.repo_name,self.validate.repo_path_dir,file.get("file","")) )
        for val in data_glob:
            raw_jsn = {"file":val.replace(f"{main_dir}/","")}
            if "mv_file" in file:
                for val2 in glob(os.path.join(self.dirs, self.path, file.get("mv_file",""))):
                    raw_jsn["mv_file"] = val2.replace(f"{main_dir}/","")
                    raw_data.append(raw_jsn)
            else:
                raw_data.append(raw_jsn)
        return raw_data

    def getFiles(self, file):
        if self.validate.arch_type == "request":
            data = self._curl(f"{self.path}/{file}")
            return {
                "is_valid": data.status_code == 200,
                "content": str(data.text)
            }
        if self.validate.arch_type == "git":
            return self._read_file(file)
        if self.validate.arch_type == "local":
            return self._read_file(file)
        return {"is_valid": False}

    def _curl(self, path):
        data = requests.get(path, timeout=25)
        return data

    def _read_file(self, file):
        if self.validate.arch_type == "local":
            path = os.path.join(self.dirs, self.path, file)
        else:
            path = os.path.join(self.dirs, self.validate.repo_name,self.validate.repo_path_dir,file)

        try:
            f_read = open(path, "r", encoding="utf-8")

            data =  {
                "is_valid": True,
                "content": str(f_read.read())
            }
            f_read.close()
            return data
        except Exception as e:
            return {
                "is_valid": False,
                "content": str(e)
            }

    def clearRepoFolder(self):
        if self.validate.arch_type == "git":
            self.isValidReq = True
            try:
                subprocess.check_output(
                    ["rm", "-rf", self.validate.repo_name],
                    cwd=self.dirs,
                    stderr=subprocess.STDOUT,
                )
            except subprocess.CalledProcessError as clone_error:
                output = clone_error.output.decode("utf-8")
                print(output)
