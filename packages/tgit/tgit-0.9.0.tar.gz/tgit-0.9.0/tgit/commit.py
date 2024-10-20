import argparse
import itertools
import os
from dataclasses import dataclass
from typing import Optional

import git
from openai import AuthenticationError, OpenAI
from pydantic import BaseModel
from rich import print

from tgit.settings import settings
from tgit.utils import get_commit_command, run_command, type_emojis

commit_type = ["feat", "fix", "chore", "docs", "style", "refactor", "perf", "wip"]


def define_commit_parser(subparsers: argparse._SubParsersAction):
    commit_type = ["feat", "fix", "chore", "docs", "style", "refactor", "perf"]
    commit_settings = settings.get("commit", {})
    types_settings = commit_settings.get("types", [])
    for data in types_settings:
        type_emojis[data.get("type")] = data.get("emoji")
        commit_type.append(data.get("type"))

    parser_commit = subparsers.add_parser("commit", help="commit changes following the conventional commit format")
    parser_commit.add_argument(
        "message",
        help="commit message, the first word should be the type, if the message is more than two parts, the second part should be the scope",
        nargs="*",
    )
    parser_commit.add_argument("-v", "--verbose", action="count", default=0, help="increase output verbosity")
    parser_commit.add_argument("-e", "--emoji", action="store_true", help="use emojis")
    parser_commit.add_argument("-b", "--breaking", action="store_true", help="breaking change")
    parser_commit.add_argument("-a", "--ai", action="store_true", help="use ai")
    parser_commit.set_defaults(func=handle_commit)


@dataclass
class CommitArgs:
    message: list[str]
    emoji: bool
    breaking: bool
    ai: bool


class CommitData(BaseModel):
    type: str
    scope: Optional[str]
    msg: str
    is_breaking: bool


def get_ai_command() -> str | None:
    client = OpenAI()
    # 获取用户执行该脚本所在的目录
    current_dir = os.getcwd()
    try:
        repo = git.Repo(current_dir, search_parent_directories=True)
    except git.InvalidGitRepositoryError:
        print("[yellow]Not a git repository[/yellow]")
        return
    diff = repo.git.diff("--cached")
    if not diff:
        print("[yellow]No changes to commit, please add some changes before using AI[/yellow]")
        return
    types = "|".join(commit_type)
    try:
        chat_completion = client.beta.chat.completions.parse(
            messages=[
                {
                    "role": "system",
                    "content": "You are a git bot. You should read the diff and suggest a commit message. "
                    + "Only if the changes are not compatible with previous versions (change the API, break the build, etc.), you should suggest a breaking change. "
                    + f"The type should be one of {types}. The message should in all lowercase. And it shoud be short, in just few words. "
                    + "The scope should be short, it is better to be a single word. "
                    + "The message should cover all the changes in the diff. It should be in present tense. If the change has many parts, you can && to separate them, and you should also shorten the message. ",
                },
                {"role": "user", "content": diff},
            ],
            model="gpt-4o",
            max_tokens=200,
            response_format=CommitData,
        )
    except AuthenticationError:
        print("[red]Could not authenticate with OpenAI, please check your API key.[/red]")
        return
    resp = chat_completion.choices[0].message.parsed
    return get_commit_command(resp.type, resp.scope, resp.msg, settings.get("commit", {}).get("emoji", False), resp.is_breaking)


def handle_commit(args: CommitArgs):

    global commit_type
    prefix = ["", "!"]
    choices = ["".join(data) for data in itertools.product(commit_type, prefix)] + ["ci", "test", "version"]

    if args.ai:
        command = get_ai_command()
        if not command:
            return
    else:
        messages = args.message
        if len(messages) == 0:
            print("Please provide a commit message, or use --ai to generate by AI")
            return
        commit_type = messages[0]
        if len(messages) > 2:
            commit_scope = messages[1]
            commit_msg = " ".join(messages[2:])
        else:
            commit_scope = None
            commit_msg = messages[1]
        if commit_type not in choices:
            print(f"Invalid type: {commit_type}")
            print(f"Valid types: {choices}")
            return
        use_emoji = args.emoji
        if use_emoji == False:
            use_emoji = settings.get("commit", {}).get("emoji", False)
        is_breaking = args.breaking
        command = get_commit_command(commit_type, commit_scope, commit_msg, use_emoji, is_breaking)
    run_command(command)
