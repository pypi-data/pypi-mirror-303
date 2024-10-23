from typing import Dict, Union

from git import Git, GitCommandError


def get_author() -> Dict[str, str]:
    """Get the current global git author

    Returns:
        Dict[str, str]: A dictionary containing the name and email address of the author
    """
    try:
        return dict(
            name=Git().config(["--global", "user.name"]),
            email=Git().config(["--global", "user.email"]),
        )
    except GitCommandError:
        pass


def set_author(name: str, email: str) -> Dict[str, Union[str, bool]]:
    """Set the global git author

    Args:
        name (str): The name of the author
        email (str): The email address of the author

    Returns:
        Dict[str, Union[str, bool]]: A dictionary containing status information
    """
    try:
        Git().config(["--global", "user.name", name])
        Git().config(["--global", "user.email", email])
        return dict(success=True)
    except GitCommandError:
        return dict(success=False, message="There was an error setting the author")
