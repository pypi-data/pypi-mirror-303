def get_git_ref(repo_path):
    """
    Get the current git ref at the given repo path

    If this is a ReadTheDocs build environment, the version name will be used from there.
    Otherwise, it will use the current checked out tag or branch
    If none of these are true, returns `None`
    """
    import git
    import os

    repo = git.Repo(repo_path)

    def get_branch():
        try:
            return repo.active_branch.name
        except (TypeError):
            return None

    def get_tag():
        tags = [tag for tag in repo.tags if tag.commit == repo.head.commit]
        match tags:
            case []:
                return None
            case [tag, *_]:
                return tag.name

    # see https://github.com/readthedocs/readthedocs.org/issues/11662,
    # this seems to be the best way to do this instead
    match os.environ.get('READTHEDOCS_VERSION_TYPE'):
        case None:
            return get_tag() or get_branch()
        case 'branch':
            return os.environ.get('READTHEDOCS_GIT_IDENTIFIER')
        case 'tag':
            return get_tag()
        case _:
            return None
