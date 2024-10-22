import os
import subprocess
from enum import Enum
from pathlib import Path
from typing import Callable, Dict, List, Literal, Optional

import click
import pne
import questionary
import requests
import typer
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from rich.console import Console

from gcop import version
from gcop.config import ModelConfig, gcop_config

load_dotenv()

app = typer.Typer(
    name="gcop",
    help="gcop is your local git command copilot",
    add_completion=False,
)
console = Console()


class LLMResponse(BaseModel):
    thought: str = Field(
        ..., description="the reasoning of why output these commit messages"
    )  # noqa
    content: str = Field(
        ...,
        description="git commit messages based on guidelines",  # noqa
    )


def get_git_diff(diff_type: Literal["--staged", "--cached"]) -> str:
    """Get git diff

    Args:
        diff_type(str): diff type, --staged or --cached

    Returns:
        str: git diff
    """
    try:
        result = subprocess.check_output(
            ["git", "diff", diff_type], text=True, encoding="utf-8"
        )
        return result
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Error getting git diff: {e}")


def generate_commit_message(diff: str, feedback: Optional[str] = None) -> List[str]:
    """Generate a git commit message based on the given diff.

    Args:
        diff(str): git diff
        feedback(Optional[str]): feedback from the previous commit message.

    Returns:
        str: git commit message
    """
    prompt = f"""
    # Git Commit Message Generator
    You are a professional software developer tasked with generating standardized git commit messages based on given git diff content. Your job is to analyze the diff, understand the changes made, and produce a concise, informative commit message following the Conventional Commits specification.

    ## Input
    You will receive a git diff output showing the differences between the current working directory and the last commit.

    ## Guidelines
    Generate a conventional git commit message adhering to the following format and guidelines:

    1. Start with a type prefix, followed by a colon and space. Common types include:
    - feat: A new feature
    - fix: A bug fix
    - docs: Documentation only changes
    - style: Changes that do not affect the meaning of the code
    - refactor: A code change that neither fixes a bug nor adds a feature
    - perf: A code change that improves performance
    - test: Adding missing tests or correcting existing tests
    - chore: Changes to the build process or auxiliary tools and libraries
    2. After the type, provide a short, imperative summary of the change (not capitalized, no period at the end).
    3. The entire first line (type + summary) should be no more than 50 characters.
    4. After the first line, leave one blank line.
    5. The body of the commit message should provide detailed explanations of the changes, wrapped at 72 characters.
    6. Use markdown lists to organize multiple points if necessary.
    7. Include any of the following information when applicable:
    - Motivation for the change
    - Contrast with previous behavior
    - Side effects or other unintuitive consequences of the change

    ## Analysis Steps
    1. Carefully read the git diff output, identifying changed files and specific code modifications.
    2. Determine the primary purpose of the changes (e.g., adding a feature, fixing a bug, refactoring code, updating dependencies).
    3. Analyze the scope and impact of the changes, determining if they affect multiple components or functionalities.
    4. Consider how these changes impact the overall project or system functionality and performance.

    ## Notes
    - Maintain a professional and objective tone, avoiding emotional or unnecessary descriptions.
    - Ensure the commit message clearly communicates the purpose and impact of the changes.
    - If the diff contains multiple unrelated changes, suggest splitting them into separate commits.

    ## Examples
    - Good Example

    ```
    feat: implement user registration

    - Add registration form component
    - Create API endpoint for user creation
    - Implement email verification process

    This feature allows new users to create accounts and verifies
    their email addresses before activation. It includes proper
    input validation and error handling.
    ```
    reason: contain relevant detail of the changes, no just one line

    - Bad Example

    ```
    feat: add user registration
    ```
    reason: only one line, need more detail based on guidelines

    Please generate a conventional commit message based on the provided git diff, following the above guidelines.
    
    ## Provided Git Diff
    \n{diff}
    """  # noqa

    if feedback is not None:
        prompt += f"""
    This is original git commit message, it's not good enough, please reflect the
    feedback and generate the better git messages.
    {feedback}
    """

    model_config: ModelConfig = gcop_config.model_config
    response: LLMResponse = pne.chat(
        messages=prompt,
        model=model_config.model_name,
        model_config={
            "api_key": model_config.api_key,
            "api_base": model_config.api_base,
            "temperature": 0.0,
        },
        output_schema=LLMResponse,
    )
    console.print(f"[green][Thought] {response.thought}[/]")
    return response.content


@app.command(name="config")
def config_command(from_init: bool = False):
    """Open the config file in the default editor."""
    initial_content = (
        "model:\n  model_name: provider/name,eg openai/gpt-4o"
        "\n  api_key: your_api_key\n"
    )
    if not os.path.exists(gcop_config.config_path):
        Path(gcop_config.config_path).write_text(initial_content)

    if not from_init:
        click.edit(filename=gcop_config.config_path)
        return

    with open(gcop_config.config_path) as f:
        content = f.read()

        if content == initial_content:
            click.edit(filename=gcop_config.config_path)


@app.command(name="init")
def init_command():
    """Add command into git config"""
    try:
        subprocess.run(
            ["git", "config", "--global", "alias.p", "push"],
            check=True,
            encoding="utf-8",  # noqa
        )
        subprocess.run(
            ["git", "config", "--global", "alias.pf", "push --force"],
            check=True,
            encoding="utf-8",  # noqa
        )
        subprocess.run(
            ["git", "config", "--global", "alias.undo", "reset --soft HEAD^"],
            check=True,
            encoding="utf-8",  # noqa
        )
        subprocess.run(
            ["git", "config", "--global", "alias.gcommit", "!gcop commit"],
            check=True,
            encoding="utf-8",  # noqa
        )
        subprocess.run(
            ["git", "config", "--global", "alias.c", "!gcop commit"],
            check=True,
            encoding="utf-8",  # noqa
        )
        subprocess.run(
            ["git", "config", "--global", "alias.ac", "!git add . && gcop commit"],
            check=True,
            encoding="utf-8",  # noqa
        )
        subprocess.run(
            ["git", "config", "--global", "alias.info", "!gcop info"],
            check=True,
            encoding="utf-8",  # noqa
        )
        subprocess.run(
            ["git", "config", "--global", "alias.gconfig", "!gcop config"],
            check=True,
            encoding="utf-8",  # noqa
        )
        subprocess.run(
            ["git", "config", "--global", "alias.ghelp", "!gcop help"],
            check=True,
            encoding="utf-8",  # noqa
        )
        console.print("[green]git aliases added successfully[/]")

        config_command(from_init=True)
        console.print("[green]gcop initialized successfully[/]")
    except subprocess.CalledProcessError as error:
        print(f"Error adding git aliases: {error}")


@app.command(name="info")
def info_command():
    """Display detailed information about the current git repository."""
    try:
        # Get project name (usually the directory name)
        project_name = os.path.basename(os.getcwd())

        # Get current branch
        current_branch = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True
        ).strip()

        # Get latest commit info
        latest_commit = subprocess.check_output(
            ["git", "log", "-1", "--oneline"], text=True
        ).strip()

        # Get number of uncommitted changes
        uncommitted_changes = len(
            subprocess.check_output(
                ["git", "status", "--porcelain"], text=True
            ).splitlines()
        )

        # Get remote URL
        remote_url = subprocess.check_output(
            ["git", "config", "--get", "remote.origin.url"], text=True
        ).strip()

        # Get total number of commits
        total_commits = subprocess.check_output(
            ["git", "rev-list", "--count", "HEAD"], text=True
        ).strip()

        # Get number of contributors
        contributors = len(
            set(
                subprocess.check_output(
                    ["git", "log", "--format='%ae'"], text=True
                ).splitlines()
            )
        )

        # Get repository creation time
        creation_time = subprocess.check_output(
            [
                "git",
                "log",
                "--reverse",
                "--date=iso",
                "--format=%ad",
                "|",
                "head",
                "-1",
            ],
            text=True,
            shell=True,
        ).strip()

        # Get last modified time
        last_modified = subprocess.check_output(
            ["git", "log", "-1", "--date=iso", "--format=%ad"], text=True
        ).strip()

        # Get repository size
        repo_size = (
            subprocess.check_output(["git", "count-objects", "-vH"], text=True)
            .split("\n")[2]
            .split(":")[1]
            .strip()
        )

        # Get most active contributor
        most_active = (
            subprocess.check_output(
                ["git", "shortlog", "-sn", "--no-merges", "|", "head", "-n", "1"],
                text=True,
                shell=True,
            )
            .strip()
            .split("\t")[1]
        )

        # Get most changed file
        most_changed = (
            subprocess.check_output(
                [
                    "git",
                    "log",
                    "--pretty=format:",
                    "--name-only",
                    "|",
                    "sort",
                    "|",
                    "uniq",
                    "-c",
                    "|",
                    "sort",
                    "-rg",
                    "|",
                    "head",
                    "-n",
                    "1",
                ],
                text=True,
                shell=True,
            )
            .strip()
            .split()[-1]
        )

        # Get line count by language (requires cloc to be installed)
        try:
            line_count = subprocess.check_output(
                ["cloc", ".", "--quiet", "--json"], text=True
            )
            # Parse JSON output and format it
            import json

            line_count_data = json.loads(line_count)
            formatted_line_count = "\n".join(
                [
                    f"{lang}: {data['code']} lines"
                    for lang, data in line_count_data.items()
                    if lang != "header" and lang != "SUM"
                ]
            )
            line_count = formatted_line_count
        except FileNotFoundError:
            line_count = (
                "cloc not found. Please ensure it's installed and in your system PATH."
            )
        except json.JSONDecodeError:
            line_count = (
                "Error parsing cloc output. Please check if cloc is working correctly."
            )
        except subprocess.CalledProcessError:
            line_count = "Error running cloc. Please check if it's installed correctly."

        # Get latest tag
        try:
            latest_tag = subprocess.check_output(
                ["git", "describe", "--tags", "--abbrev=0"], text=True
            ).strip()
        except subprocess.CalledProcessError:
            latest_tag = "No tags found"

        # Get branch count
        branch_count = len(
            subprocess.check_output(["git", "branch", "-a"], text=True).splitlines()
        )

        # Get untracked files count
        untracked_count = len(
            subprocess.check_output(
                ["git", "ls-files", "--others", "--exclude-standard"], text=True
            ).splitlines()
        )

        # Get submodule info
        try:
            submodules = subprocess.check_output(
                ["git", "submodule", "status"], text=True
            ).strip()
            if not submodules:
                submodules = "No submodules"
        except subprocess.CalledProcessError:
            submodules = "No submodules"

        # Get latest merge commit
        try:
            latest_merge = subprocess.check_output(
                ["git", "log", "--merges", "-n", "1", "--pretty=format:%h - %s"],
                text=True,
            ).strip()
            if not latest_merge:
                latest_merge = "No merge commits found"
        except subprocess.CalledProcessError:
            latest_merge = "No merge commits found"

        # Get file type statistics
        file_types = subprocess.check_output(
            [
                "git",
                "ls-files",
                "|",
                "sed",
                "s/.*\\.//",
                "|",
                "sort",
                "|",
                "uniq",
                "-c",
                "|",
                "sort",
                "-rn",
            ],
            text=True,
            shell=True,
        ).strip()

        console.print(f"[bold]Project Name:[/] {project_name}")
        console.print(f"[bold]Current Branch:[/] {current_branch}")
        console.print(f"[bold]Latest Commit:[/] {latest_commit}")
        console.print(f"[bold]Uncommitted Changes:[/] {uncommitted_changes}")
        console.print(f"[bold]Remote URL:[/] {remote_url}")
        console.print(f"[bold]Total Commits:[/] {total_commits}")
        console.print(f"[bold]Contributors:[/] {contributors}")
        console.print(f"[bold]Repository Created:[/] {creation_time}")
        console.print(f"[bold]Last Modified:[/] {last_modified}")
        console.print(f"[bold]Repository Size:[/] {repo_size}")
        console.print(f"[bold]Most Active Contributor:[/] {most_active}")
        console.print(f"[bold]Most Changed File:[/] {most_changed}")
        console.print(f"[bold]Line Count by Language:[/]\n{line_count}")
        console.print(f"[bold]Latest Tag:[/] {latest_tag}")
        console.print(f"[bold]Branch Count:[/] {branch_count}")
        console.print(f"[bold]Untracked Files:[/] {untracked_count}")
        console.print(f"[bold]Submodules:[/]{submodules}")
        console.print(f"[bold]Latest Merge Commit:[/] {latest_merge}")
        console.print(f"[bold]File Type Statistics:[/]\n{file_types}")

    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error getting repository information: {e}[/]")


@app.command(name="commit")
def commit_command(feedback: Optional[str] = None):
    """Generate a git commit message based on the staged changes and commit the
    changes.

    If you want to commit the changes with the generated commit message, please
    select "yes". If you want to retry the commit message generation, please
    select "retry". If you want to retry the commit message generation with new
    feedback, please select "retry by feedback". If you want to exit the commit
    process, please select "exit".
    """
    diff: str = get_git_diff("--staged")
    if not diff:
        console.print("[yellow]No staged changes[/]")
        return

    console.print(f"[yellow][Code diff] \n{diff}[/]")

    commit_messages: str = generate_commit_message(diff, feedback)
    console.print(f"[green][Generated commit message]\n{commit_messages}[/]")

    response = questionary.select(
        "Do you want to commit the changes with this message?",
        choices=["yes", "retry", "retry by feedback", "exit"],
    ).ask()

    if response == "yes":
        subprocess.run(["git", "commit", "-m", commit_messages])
    elif response == "retry":
        commit_command(feedback=None)
    elif response == "retry by feedback":
        new_feedback = questionary.text("Please enter your feedback:").ask()
        if new_feedback:
            commit_command(feedback=new_feedback)
        else:
            console.print("[yellow]No feedback provided. Exiting...[/]")
    else:  # exit
        console.print("[yellow]Exiting commit process.[/]")

    # # request pypi to get the latest version
    # # TODO optimize logic, everyday check the latest version one time
    # response = requests.get("https://pypi.org/pypi/gcop/json")
    # latest_version = response.json()["info"]["version"]
    # if version != latest_version:
    #     console.print(f"[bold]A new version of gcop is available: {latest_version}[/]") # noqa
    #     console.print(f"[bold]Your current version: {version}[/]")
    #     console.print(
    #         "[bold]Please consider upgrading by running: pip install -U gcop[/]"
    #     )


@app.command(name="help")
def help_command():
    """Show help message"""
    help_message = """
[bold]gcop[/] is your local git command copilot
[bold]Version: [/]{version}
[bold]GitHub: https://github.com/Undertone0809/gcop[/]

[bold]Usage: gcop [OPTIONS] COMMAND[/]

[bold]Commands:
  git p          Push the changes to the remote repository
  git pf         Push the changes to the remote repository with force
  git undo       Undo the last commit but keep the file changes
  git ghelp      Add command into git config
  git gconfig    Open the config file in the default editor
  git gcommit    Generate a git commit message based on the staged changes and commit the changes
  git c          The same as `git gcommit` command
  git ac         The same as `git add . && git gcommit` command
  git info       Display basic information about the current git repository
"""  # noqa

    console.print(help_message)


if __name__ == "__main__":
    app()
