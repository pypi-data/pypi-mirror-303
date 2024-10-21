from autogs.util import generate_random_string

from typing import Optional

from github import Github


def create_branch(repository: str,
                  github_token: str,
                  branch_name: str,
                  base_branch: str = 'main'):
    """
    Create a new branch in a GitHub repository from base branch
    Arguments:
        - repository: Repository name in the format 'owner/repo'
        - github_token: GitHub personal access token
        - branch_name: Name of the new branch
        - base_branch: Base branch to create the new branch from

    """
    g = Github(github_token)
    repo = g.get_repo(repository)
    base_branch_ref = repo.get_git_ref(f'heads/{base_branch}')
    try:
        repo.create_git_ref(ref=f'refs/heads/{branch_name}',
                            sha=base_branch_ref.object.sha)
        print(f'Branch {branch_name} created successfully')
    except Exception as e:
        print(f'Error creating branch: {e}')


def commit_file_to_branch(
        repository: str,
        github_token: str,
        branch_name: str,
        file_path: str,
        commit_message: str,
        content: str
):
    """
    Add a file to a branch in a GitHub repository
    Arguments:
        - repository: Repository name in the format 'owner/repo'
        - github_token: GitHub personal access token
        - branch_name: Name of the branch to commit to
        - file_path: Path to the file to commit
        - commit_message: Commit message
        - content: File content
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
                branch=branch_name
            )
            print(f'File {file_path} updated successfully in branch {branch_name}')
        except Exception as e:
            print(f'Error updating file: {e}')
            return
    except Exception as e:
        try:
            repo.create_file(
                path=file_path,
                message=commit_message,
                content=content,
                branch=branch_name
            )
            print(f'File {file_path} created successfully in branch {branch_name}')
        except Exception as e:
            print(f'Error creating file: {e}')
            return


def create_pullrequest(
        repository: str,
        github_token: str,
        branch_name: str,
        title: Optional[str] = None,
        message: str = '',
        auto_merge: bool = False
):
    """
    Create a pull request in a GitHub repository
    Arguments:
        - repository: Repository name in the format 'owner/repo'
        - github_token: GitHub personal access token
        - branch_name: Name of the branch to commit to
        - file_path: Path to the file to commit
        - commit_message: Commit message
        - content: File content
        - auto_merge: Automatically merge the pull request
    """
    g = Github(github_token)
    repo = g.get_repo(repository)
    if not title:
        title = f'Automatically generated pull request'
    try:
        pull_request = repo.create_pull(
            title=title,
            body=message,
            head=branch_name,
            base='main',
            maintainer_can_modify=True,
            draft=False
        )
        print(f'Pull request created: {pull_request.html_url}')
        if auto_merge:
            merge_pull_request_by_branch(repository, github_token, branch_name)
    except Exception as e:
        print(f'Error creating or merging pull request: {e}')


def merge_pull_request_by_branch(
        repository: str,
        github_token: str,
        branch_name: str):
    """
    Merge a pull request in a GitHub repository using the branch name
    Arguments:
        - repository: Repository name in the format 'owner/repo'
        - github_token: GitHub personal access token
        - branch_name: Name of the branch associated with the pull request
    """
    g = Github(github_token)
    repo = g.get_repo(repository)
    try:
        pulls = repo.get_pulls(state='open', head=f'{repo.owner.login}:{branch_name}')
        if pulls.totalCount == 0:
            print(f'No open pull request found for branch {branch_name}')
            return
        pull_request = pulls[0]
        pull_request.merge()
        print(f'Pull request #{pull_request.number} merged: {pull_request.html_url}')
    except Exception as e:
        print(f'Error merging pull request: {e}')


if __name__ == '__main__':
    from autogs._static import DEFAULT_GITHUB_TOKEN

    MY_GITHUB_TOKEN = DEFAULT_GITHUB_TOKEN
    MY_REPO_NAME = 'younesStrittmatter/autogs-db-sweetpea'
    branch_name = f'data-branch-{generate_random_string()}'
    create_branch(MY_REPO_NAME, MY_GITHUB_TOKEN, branch_name)
    content = 'def test():\n    print("Hello, World!")'
    commit_file_to_branch(
        MY_REPO_NAME,
        MY_GITHUB_TOKEN,
        branch_name, 'tst.py', 'Add tst', content)
    create_pullrequest(MY_REPO_NAME, MY_GITHUB_TOKEN, branch_name, 'Add tst', 'Add tst', auto_merge=True)

