"""
This module contains the CommitizenGitmojiCz class,
which is a subclass of BaseCommitizen.
"""

import re
import textwrap
from collections import OrderedDict
from pathlib import Path
from typing import Any, Dict, List, Union

from commitizen import git
from commitizen.cz.base import BaseCommitizen
from commitizen.cz.utils import required_validator, multiple_line_breaker
from commitizen.defaults import MAJOR, MINOR, PATCH
import commitizen.defaults

from shared import utils
from shared.gitmojis import GitMojiConstant as mojis

__all__ = ["CommitizenGitmojiCz", "parse_scope", "parse_subject"]


def parse_scope(text: str) -> str:
    """Parse the scope of the change."""
    if not text:
        return ""

    scope = text.strip().split()
    return "-".join(scope)


def parse_subject(text: str) -> str:
    """Parse the subject of the change."""
    if isinstance(text, str):
        text = text.strip(".").strip()

    return required_validator(text, msg="Subject is required.")


def parse_bordy(text: str) -> str:
    """Process the text using multiple_line_breaker and then soft-wrap it."""
    processed_text = multiple_line_breaker(text)

    return "\n".join(
        "\n".join(textwrap.wrap(line, width=72))
        for line in processed_text.splitlines()
    )


class CommitizenGitmojiCz(BaseCommitizen):
    """Commitizen adapter for gitmoji style."""

    # pattern to match messages for bumping
    # if none of these match, version will not be bumped
    # (unless manually specified)
    bump_pattern = (
        r"^((BREAKING[\-\ ]CHANGE"
        r"|feat"
        r"|fix"
        r"|hotfix"
        r"|refactor"
        r"|perf)"
        r"(\(.+\))?"  # scope
        r"!?):"  # breaking
    )
    # map types to SemVer
    bump_map = OrderedDict(
        (
            (r"^.+!$", MAJOR),
            (r"^BREAKING[\-\ ]CHANGE", MAJOR),
            (r"^feat", MINOR),
            (r"^fix", PATCH),
            (r"^hotfix", PATCH),
            (r"^refactor", PATCH),
            (r"^perf", PATCH),
        )
    )
    bump_map_major_version_zero = bump_map.copy()

    # parse information for generating the change log
    commit_parser = (
        rf"^(?P<change_type>{utils.get_type_pattern()}|BREAKING CHANGE)"
        rf"(?:\((?P<scope>[^()\r\n]*)\)|\()?(?P<breaking>!)?:\s"
        rf"(?P<emoji>{utils.get_icon_pattern()})?\s?"
        rf"(?P<message>.*)?"
    )

    # exclude from changelog
    changelog_pattern = r"^(?!init)(?!merge)(?!bump).*"
    # map types to changelog sections
    change_type_map = {
        # features
        "feat": f"{mojis.GJ_FEAT.value} Features",
        # fixes
        "fix": f"{mojis.GJ_FIX.value}{mojis.GJ_HOTFIX.value} Fixes",
        "hotfix": f"{mojis.GJ_FIX.value}{mojis.GJ_HOTFIX.value} Fixes",
        # refactorings
        "refactor": f"{mojis.GJ_REFACTOR.value} Refactorings",
        # style & architecture
        "style": f"{mojis.GJ_STYLE.value} Style & Architecture",
        # performance
        "perf": f"{mojis.GJ_PERF.value} Performance",
        # docs
        "docs": f"{mojis.GJ_DOCS.value} Documentation",
        # tests
        "test": f"{mojis.GJ_TEST.value} Tests",
        # ci & build
        "build": f"{mojis.GJ_CI.value}{mojis.GJ_BUILD.value} CI & Build",
        "ci": f"{mojis.GJ_CI.value}{mojis.GJ_BUILD.value} CI & Build",
        # configuration & scripts & packages
        "config": f"{mojis.GJ_CONFIG.value} Configuration, Scripts, Packages",
        # cleanup
        "dump": f"{mojis.GJ_DUMP.value} Clean up",
        # dependencies
        "dep-add": (
            f"{mojis.GJ_DEP_ADD.value}{mojis.GJ_DEP_RM.value}"
            f"{mojis.GJ_DEP_BUMP.value}{mojis.GJ_DEP_DROP.value} Dependencies"
        ),
        "dep-rm": (
            f"{mojis.GJ_DEP_ADD.value}{mojis.GJ_DEP_RM.value}"
            f"{mojis.GJ_DEP_BUMP.value}{mojis.GJ_DEP_DROP.value} Dependencies"
        ),
        "dep-bump": (
            f"{mojis.GJ_DEP_ADD.value}{mojis.GJ_DEP_RM.value}"
            f"{mojis.GJ_DEP_BUMP.value}{mojis.GJ_DEP_DROP.value} Dependencies"
        ),
        "dep-drop": (
            f"{mojis.GJ_DEP_ADD.value}{mojis.GJ_DEP_RM.value}"
            f"{mojis.GJ_DEP_BUMP.value}{mojis.GJ_DEP_DROP.value} Dependencies"
        ),
        # language & accessibility
        "lang": f"{mojis.GJ_LANG.value} Language & Accessibility",
        # logs
        "logs-add": f"{mojis.GJ_LOGS_ADD.value}{mojis.GJ_LOGS_RM.value} Logs",
        "logs-rm": f"{mojis.GJ_LOGS_ADD.value}{mojis.GJ_LOGS_RM.value} Logs",
        # ignore
        "ignore": f"{mojis.GJ_IGNORE.value} Ignore",
        # chore
        "chore": f"{mojis.GJ_CHORE.value} Chore",
        # None: init, bump, merge
    }
    # Order sections in changelog
    # All other sections are ordered alphabetically
    change_type_order = [
        f"{mojis.GJ_FEAT.value} Features",
        f"{mojis.GJ_FIX.value}{mojis.GJ_HOTFIX.value} Fixes",
        f"{mojis.GJ_REFACTOR.value} Refactorings",
        f"{mojis.GJ_PERF.value} Performance",
    ]
    # message to bump version
    commitizen.defaults.bump_message = (
        "bump(release): 🔖 $current_version → $new_version"
    )

    def changelog_message_builder_hook(
        self, parsed_message: dict, _: git.GitCommit
    ) -> Union[dict, list, None]:
        """Hook to build the changelog message.
        :param parsed_message: The parsed commit message
        :param _: The commit object
        :return: The changelog message
        """
        if "emoji" in parsed_message and parsed_message["emoji"]:
            parsed_message["message"] = (
                parsed_message["message"]
                .lstrip(parsed_message["emoji"])
                .lstrip()
            )

        return parsed_message

    def questions(self) -> List[Dict[str, Any]]:
        """Return the questions to ask the user."""
        return [
            {
                "type": "list",
                "name": "prefix",
                "message": "Select the type of change you are committing",
                "choices": [
                    {
                        "value": moji.value,
                        "name": moji.name,
                    }
                    for moji in utils.get_gitmojis()
                ],
            },
            {
                "type": "input",
                "name": "scope",
                "message": (
                    "What is the scope of this change? (class or file name): "
                    "(press [enter] to skip)\n"
                ),
                "filter": parse_scope,
            },
            {
                "type": "input",
                "name": "subject",
                "filter": parse_subject,
                "message": (
                    "Write a short and imperative summary "
                    "of the code changes: "
                    "(lower case (except for name) and no period)\n"
                ),
            },
            {
                "type": "input",
                "name": "body",
                "message": (
                    "Provide additional contextual information about "
                    "the code changes: (press [enter] to skip)\n"
                ),
                "filter": parse_bordy,
            },
            {
                "type": "confirm",
                "message": (
                    "Is this a BREAKING CHANGE? "
                    "Correlates with MAJOR in SemVer"
                ),
                "name": "is_breaking_change",
                "default": False,
            },
            {
                "type": "input",
                "name": "footer",
                "message": (
                    "Footer. Information about Breaking Changes and reference "
                    "issues that this commit closes: (press [enter] to skip)\n"
                ),
            },
        ]

    def message(self, answers: Dict[str, Any]) -> str:
        """Generate a commit message from the answers."""
        prefix: tuple[str, str] = answers["prefix"]
        scope = answers["scope"]
        subject = answers["subject"]
        body = answers["body"]
        footer = answers["footer"]
        is_breaking_change = answers["is_breaking_change"]

        if scope:
            scope = f"({scope})"
        if body:
            body = f"\n\n{body}"
        if (
            is_breaking_change
            and footer
            and not footer.startswith("BREAKING CHANGE")
        ):
            footer = f"BREAKING CHANGE: {footer}"
        if footer:
            footer = f"\n\n{footer}"

        prefix_scope = f"{prefix[0]}{scope}"
        if is_breaking_change:
            prefix_scope = f"{prefix_scope}!"

        message = f"{prefix_scope}: {prefix[1]} {subject}{body}{footer}"

        return message

    def example(self) -> str:
        """Return an example commit message."""
        return (
            f"fix: {mojis.GJ_FIX.value} correct minor typos in code\n"
            "\n"
            "see the issue for details on the typos fixed\n"
            "\n"
            "closes issue #12"
        )

    def schema(self) -> str:
        """Return the commit message schema."""
        return (
            "<type>(<scope>): <gitmoji> <subject>\n"
            "<BLANK LINE>\n"
            "<body>\n"
            "<BLANK LINE>\n"
            "(BREAKING CHANGE: )<footer>"
        )

    # pattern to validate commits
    def schema_pattern(self) -> str:
        """Return the schema validation pattern."""
        return utils.get_pattern()

    def info(self) -> str:
        """Return information about the commit message style."""
        dir_path = Path(__file__).parent
        filepath = dir_path.joinpath("conventional_gitmojis_info.txt")
        with open(filepath, "r", encoding="UTF-8") as f:
            content = f.read()
        return content

    def process_commit(self, commit: str) -> str:
        """Process a commit."""
        pat = self.schema_pattern()
        m = re.match(pat, commit)
        if m is None:
            return ""
        return m.group(3).strip()
