import re


class ValidateSource:
    def __init__(self, path) -> None:
        self.path = path

        self.arch_type = None
        self.repo_name = None
        self.repo_path_dir = ""
        self.repo_details = {}
        self.__validate_for_git()
        self.__validate_for_request()
        self.__validate_for_local()

    def __validate_for_request(self):
        # noqa: raw file github

        if self.arch_type is None:
            match2 = re.search(r"^(http[s]{0,1})\://", self.path)
            if match2:
                self.arch_type = "request"


    def __validate_for_git(self):
        match1 = re.search(r"(\/[a-zA-Z0-9\_\-]{2,}\.git[\/]{0,}\b)", self.path)
        if match1:
            self.arch_type = "git"
            self.repo_name = match1[0].replace("/", "").split(".")[0]
            split_path = self.path.split(r".git")
            if len(split_path) > 1:
                self.path = split_path[0] + ".git"
                self.repo_path_dir = re.sub(r"^[\/]","","/".join(split_path[1::]))
            match_branch = re.search(r"[\/]{0,1}\[\b([a-zA-Z0-9\.\_\-\/]{2,})\b\]", self.repo_path_dir)

            if match_branch:
                branch_name = re.sub(r"^[\/]","", match_branch[0])
                branch_name = re.sub(r"[\[\]]","", branch_name)
                self.repo_details["branch_name"] = branch_name
                self.repo_path_dir = re.sub(r"^[\/]","",self.repo_path_dir.replace(match_branch[0],""))

    def __validate_for_local(self):
        # noqa: raw file in local
        match1 = re.search(r"^([.]{1,}|[\/]{1}[A-Za-z]{1,}|[A-Za-z]{1}\:[\/]{1})", self.path)
        if match1:
            self.arch_type = "local"
        else:
            match2 = re.search(r"([\/]{1,})", self.path)
            if match2 and self.arch_type is None:
                self.arch_type = "local"
