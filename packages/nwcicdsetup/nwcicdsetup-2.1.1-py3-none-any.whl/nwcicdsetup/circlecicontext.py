import os
from dataclasses import dataclass, field


@dataclass
class CircleCIContext:
    branch: str
    pipeline_number: int
    project_reponame: str
    project_username: str
    working_directory: str
    circle_token: str
    github_token: str
    vcs_type: str = "gh"
    current_vcs_revision: str = field(default="", init=False)
    last_successful_vcs_revision: str = field(default="", init=False)

    @staticmethod
    def create_from_environ(pipeline: int) -> "CircleCIContext":
        if len(os.environ["CIRCLE_PROJECT_USERNAME"]) < 0:
            raise Exception("project username is null")

        return CircleCIContext(
            branch=os.environ["CIRCLE_BRANCH"],
            pipeline_number=pipeline,
            project_reponame=os.environ.get("CIRCLE_PROJECT_REPONAME", ""),
            project_username=os.environ["CIRCLE_PROJECT_USERNAME"],
            working_directory=os.environ["CIRCLE_WORKING_DIRECTORY"],
            circle_token=os.environ["CIRCLE_TOKEN"],
            github_token=os.environ["GITHUB_TOKEN"])

    @staticmethod
    def create_dummy_env(pipeline: int) -> "CircleCIContext":
        if len(os.environ["CIRCLE_PROJECT_USERNAME"]) < 0:
            raise Exception("project username is null")
            
        circle_token = os.environ.get("CIRCLE_TOKEN", "")
        github_token = os.environ.get("GITHUB_TOKEN", "")
        return CircleCIContext(
            branch="develop",
            pipeline_number=pipeline,
            project_reponame="nw-platform",
            project_username="nativewaves",
            working_directory=".",
            circle_token=circle_token,
            github_token=github_token)
