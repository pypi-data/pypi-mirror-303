"""PyPackIT Test1: A Placeholder Project Title.

Replace this text with a short abstract of PyPackIT Test1, describing its
purpose and main features. By default, this text is displayed on the
repository's main README file, on the homepage of the project's website, on the
project's PyPI and TestPyPI pages, and on the package's main docstring. Like all
other entries in the repository's control center, this text can also contain
dynamic references to other entries, using the <code>${‎{ json-path.to.value
}}</code> syntax. By default, the first occurrence of the name of the project in
this text is styled as strong and linked to the project's website.

2024 Armin Ariamajd
SPDX-License-Identifier: MIT
"""

from pypackit_test1 import data

__all__ = ["data", "__version_details__", "__version__"]

__version_details__: dict[str, str] = {
    "version": "0.0.3",
    "build_date": "2024.10.23",
    "committer_date": "2024.10.23",
    "author_date": "2024.10.23",
    "branch": "None",
    "distance": "0",
    "commit_hash": "4d10750f872af4723d0ded3d0e013a8c4813bebb",
}

"""Details of the currently installed version of the package,
including version number, date, branch, and commit hash."""

__version__: str = __version_details__["version"]
"""Version number of the currently installed package."""
