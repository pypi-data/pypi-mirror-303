from github import Github

from autogs._static import DEFAULT_GITHUB_TOKEN


def create_branch(
    repository: str,
    branch_name: str,
    base_branch: str = "main",
    github_token: str = DEFAULT_GITHUB_TOKEN,
):
    """
    Create a new branch in a GitHub repository from base branch

    Args:
        - repository: Repository name in the format 'owner/repo'
        - branch_name: Name of the new branch
        - base_branch: Base branch to create the new branch from
        - github_token: GitHub personal access token
    """
    g = Github(github_token)
    repo = g.get_repo(repository)
    base_branch_ref = repo.get_git_ref(f"heads/{base_branch}")
    try:
        repo.create_git_ref(
            ref=f"refs/heads/{branch_name}", sha=base_branch_ref.object.sha
        )
        print(f"Branch {branch_name} created successfully")
    except Exception as e:
        print(f"Error creating branch: {e}")


def commit_file_to_branch(
    repository: str,
    branch_name: str,
    file_path: str,
    content: str,
    commit_message: str = "Update file",
    github_token: str = DEFAULT_GITHUB_TOKEN,
):
    """
    Add a file to a branch in a GitHub repository

    Args:
        - repository: Repository name in the format 'owner/repo'
        - branch_name: Name of the branch to commit to
        - file_path: Path to the file to commit
        - content: File content
        - commit_message: Commit message
        - github_token: GitHub personal access token
    """
    g = Github(github_token)
    repo = g.get_repo(repository)

    try:
        contents = repo.get_contents(file_path, ref=branch_name)
        try:
            repo.update_file(
                path=file_path,
                message=commit_message,
                content=content,
                sha=contents.sha,
                branch=branch_name,
            )
            print(f"File {file_path} updated successfully in branch {branch_name}")
        except Exception as e:
            print(f"Error updating file: {e}")
            return
    except Exception:
        try:
            repo.create_file(
                path=file_path,
                message=commit_message,
                content=content,
                branch=branch_name,
            )
            print(f"File {file_path} created successfully in branch {branch_name}")
        except Exception as e:
            print(f"Error creating file: {e}")
            return


def create_pull_request(
    repository: str,
    branch_name: str,
    base: str = "main",
    title: str = "Automatically generated pull request",
    message: str = "",
    auto_merge: bool = False,
    github_token: str = DEFAULT_GITHUB_TOKEN,
):
    """
    Create a pull request in a GitHub repository

    Args:
        - repository: Repository name in the format 'owner/repo'
        - branch_name: Name of the branch to create the pull request from
        - base: Base branch to create the pull request to
        - title: Title of the pull request
        - message: Body of the pull request
        - auto_merge: Automatically merge the pull request
        - github_token: GitHub personal access token
    """
    g = Github(github_token)
    repo = g.get_repo(repository)
    try:
        pull_request = repo.create_pull(
            title=title,
            body=message,
            head=branch_name,
            base=base,
            maintainer_can_modify=True,
            draft=False,
        )
        print(f"Pull request created: {pull_request.html_url}")
        if auto_merge:
            merge_pull_request_by_branch(repository, branch_name, github_token)
    except Exception as e:
        print(f"Error creating or merging pull request: {e}")


def merge_pull_request_by_branch(
    repository: str, branch_name: str, github_token: str = DEFAULT_GITHUB_TOKEN
):
    """
    Merge a pull request in a GitHub repository using the branch name

    Args:
        - repository: Repository name in the format 'owner/repo'
        - branch_name: Name of the branch associated with the pull request
        - github_token: GitHub personal access token
    """
    g = Github(github_token)
    repo = g.get_repo(repository)
    try:
        pulls = repo.get_pulls(state="open", head=f"{repo.owner.login}:{branch_name}")
        if pulls.totalCount == 0:
            print(f"No open pull request found for branch {branch_name}")
            return
        pull_request = pulls[0]
        pull_request.merge()
        print(f"Pull request #{pull_request.number} merged: {pull_request.html_url}")
    except Exception as e:
        print(f"Error merging pull request: {e}")


def get_existing_folders(
    repository: str,
    branch_name: str = "main",
    github_token: str = DEFAULT_GITHUB_TOKEN,
):
    """
    Get the list of existing folders in a GitHub repository branch

    Args:
        - repository: Repository name in the format 'owner/repo'
        - branch_name: Name of the branch to check
        - github_token: GitHub personal access token

    Returns:
        - list: List of existing folders
    """
    g = Github(github_token)
    repo = g.get_repo(repository)
    try:
        contents = repo.get_contents("", ref=branch_name)
        folders = [content.name for content in contents if content.type == "dir"]
        return folders
    except Exception as e:
        print(f"Error getting existing folders: {e}")
        return []


def is_folder(
    repository: str,
    folder_name: str,
    branch_name: str = "main",
    github_token: str = DEFAULT_GITHUB_TOKEN,
):
    """
    Check if a folder exists in a GitHub repository branch

    Args:
        - repository: Repository name in the format 'owner/repo'
        - folder_name: Name of the folder to check
        - branch_name: Name of the branch to check
        - github_token: GitHub personal access token

    Returns:
        - bool: True if the folder exists, False otherwise

    """
    folders = get_existing_folders(repository, branch_name, github_token)
    return folder_name in folders


if __name__ == "__main__":
    from autogs.util import generate_random_string

    MY_REPO_NAME = "younesStrittmatter/autogs-db-sweetpea"
    print(get_existing_folders(MY_REPO_NAME, "main"))
    branch_name = f"data-branch-{generate_random_string()}"
    create_branch(MY_REPO_NAME, branch_name)
    content = 'def test():\n    print("Hello, World!")'
    commit_file_to_branch(MY_REPO_NAME, branch_name, "tst/tst.py", "Add tst", content)
    create_pull_request(MY_REPO_NAME, branch_name, auto_merge=True)
