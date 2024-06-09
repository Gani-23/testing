from github import Github
import os
import subprocess

github_username = 'gani-23'
github_password = "Password"

repository_owner = 'gani-23'
repository_name = 'testing'

local_repo_path = os.path.join(os.path.dirname(__file__), repository_name)

g = Github(github_username, github_password)

repo = g.get_user(repository_owner).get_repo(repository_name)

default_branch = repo.default_branch

latest_remote_commit_sha = repo.get_branch(default_branch).commit.sha
if os.path.exists(local_repo_path):
    os.chdir(local_repo_path)

    result = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True)
    local_commit_sha = result.stdout.strip()

    if local_commit_sha != latest_remote_commit_sha:
        print("Local repository is behind. Fetching latest changes...")

        subprocess.run(['git', 'pull'])

        print("Pull successful. Local repository is now up to date.")
    else:
        print("Local repository is up to date. No need to pull changes.")
else:
    print(f"Local repository not found at path: {local_repo_path}")