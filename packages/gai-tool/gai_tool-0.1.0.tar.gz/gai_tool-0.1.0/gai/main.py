import argparse
import subprocess
import yaml
import os

from gai.api import GroqClient, Gitlab_api, Github_api
from gai.src import DisplayChoices, Commit, Prompts, Merge_requests


class Main:
    model = None
    temperature = None
    max_tokens = None
    target_branch = None

    def parse_arguments(self):
        parser = argparse.ArgumentParser(
            description="Git-AI (gai): Automate your git messages")

        # Helper text
        subparsers = parser.add_subparsers(
            dest='command', help='Available commands')

        # Merge request
        merge_parser = subparsers.add_parser(
            'merge', help='Execute an automated merge request')

        merge_parser.add_argument(
            'remote', help='Specify the remote git url (e.g., origin, upstream)')

        # Commit
        commit_parser = subparsers.add_parser(
            'commit', help='Execute an automated commit')

        # Common arguments
        for p in [merge_parser, commit_parser]:
            p.add_argument('--model', '-mo', type=str,
                           help='Override the model specified in config')
            p.add_argument('--temperature', '-t', type=float,
                           help='Override the temperature specified in config')
            p.add_argument('--max-tokens', '-mt', type=int,
                           help='Override the max_tokens specified in config')
            p.add_argument('--target-branch', '-tb', type=str,
                           help='Specify the target branch for merge requests')

        return parser.parse_args()

    def load_config(self):
        with open("gai/config.yaml", "r") as file:
            config = yaml.safe_load(file)

        self.model = self.args.model or config['model']
        self.temperature = self.args.temperature or config['temperature']
        self.max_tokens = self.args.max_tokens or config['max_tokens']
        self.target_branch = self.args.target_branch or config['target_branch']

    def init_groq_client(self):
        self.groq_chat_client = GroqClient(
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )

    def do_merge_request(self):
        # Initialize singleton
        Merge_requests.initialize(self.args.remote)

        mr = Merge_requests()

        platform = mr.get_remote_platform()

        commits = mr.get_commits(
            target_branch=self.target_branch,
            source_branch=self.Gitlab.get_current_branch())  # TODO: fix this func

        prompt = self.Prompt.build_merge_request_title_prompt(commits)

        description = mr.format_commits(commits)

        print(prompt)
        print(f"token count: {len(prompt.split())}")

        selected_title = self.DisplayChoices.render_choices_with_try_again(
            prompt=prompt,
            ai_client=self.groq_chat_client.get_chat_completion)

        print("Creating merge request with...")
        print(f"Title: {selected_title}")
        print(f"Description: {description}")

        print("Platform: ", platform)

        match platform:
            case "gitlab":
                self.Gitlab.create_merge_request(
                    title=selected_title,
                    description=description)

            case "github":
                self.Github.create_pull_request(
                    title=selected_title,
                    body=description)
            case _:
                raise ValueError(
                    "Platform not supported. Only github and gitlab are supported.")

    def do_commit(self):
        git_diffs = self.Commit.get_diffs()

        prompt = self.Prompt.build_commit_message_prompt(
            git_diffs)

        # print(build_prompt)
        print(f"Token count: {len(prompt.split())}")

        selected_commit = self.DisplayChoices.render_choices_with_try_again(
            prompt=prompt,
            ai_client=self.groq_chat_client.get_chat_completion)

        print("selected_commit", selected_commit)
        self.Commit.commit_changes(selected_commit)

    def run(self):
        self.args = self.parse_arguments()

        self.Commit = Commit()
        self.Prompt = Prompts()
        self.DisplayChoices = DisplayChoices()

        self.Gitlab = Gitlab_api()
        self.Github = Github_api()

        self.load_config()
        self.init_groq_client()

        if self.args.command == 'merge':
            self.do_merge_request()
        elif self.args.command == 'commit':
            self.do_commit()
        else:
            print("Please specify a command: merge or commit")


def main():
    app = Main()
    app.run()


if __name__ == "__main__":
    main()
