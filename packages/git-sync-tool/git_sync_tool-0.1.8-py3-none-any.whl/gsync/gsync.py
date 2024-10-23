import argparse
import json
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from enum import Enum

import git
from colorama import Fore, Style, init
from prettytable import PrettyTable
from tqdm import tqdm

init(autoreset=True)

class SyncStatus(Enum):
    SYNCED = 0
    UNSAVED = 1
    AHEAD = 2
    BEHIND = 3
    DIVERGED = 4

sync_labels = [
    f"{Fore.GREEN}Synced{Style.RESET_ALL}",
    f"{Fore.YELLOW}Unsaved{Style.RESET_ALL}",
    f"{Fore.YELLOW}Ahead{Style.RESET_ALL}",
    f"{Fore.RED}Behind{Style.RESET_ALL}",
    f"{Fore.RED}Diverged{Style.RESET_ALL}",
]

def get_repos():
    result = subprocess.run(
        ['gh', 'repo', 'list', '--limit', '1000', '--json', 'name'],
        capture_output=True, text=True, check=True
    )
    return {repo['name'] for repo in json.loads(result.stdout)}

def list_folders(path):
    return {name for name in os.listdir(path) 
               if os.path.isdir(os.path.join(path, name))}

def check_repo(path):
    repo = git.Repo(path)

    repo.remotes.origin.fetch()

    local_commits = len(list(repo.iter_commits('origin/' + repo.active_branch.name + '..')))
    remote_commits = len(list(repo.iter_commits(repo.active_branch.name + '..origin/' + repo.active_branch.name)))

    if local_commits == 0 and remote_commits == 0:
        if repo.is_dirty(untracked_files=True):
            return (path, SyncStatus.UNSAVED)
        else:
            return (path, SyncStatus.SYNCED)
    elif local_commits > 0 and remote_commits > 0:
        return (path, SyncStatus.DIVERGED)
    elif remote_commits > 0:
        return (path, SyncStatus.BEHIND)
    elif local_commits > 0:
        return (path, SyncStatus.AHEAD)

def compare_repos(known_repos, exist_repos, path="."):
    missing_locally = known_repos - exist_repos
    missing_online = exist_repos - known_repos
    existing_both = known_repos & exist_repos

    exists = []
    
    with ThreadPoolExecutor() as executor:
        future_to_repo = {executor.submit(check_repo, os.path.join(path, repo)): repo for repo in sorted(existing_both)}
        for future in tqdm(as_completed(future_to_repo), total=len(future_to_repo), desc="Checking Repos", bar_format="{l_bar}{bar}|{n_fmt}/{total_fmt}"):
            repo = future_to_repo[future]
            try:
                path, status = future.result()
                exists.append((repo, status))
            except Exception as e:
                print(f"Error checking {repo}: {e}")

    exists.sort(key=lambda x: x[1].value)

    table = PrettyTable()
    table.field_names = ["Project", "Repo", "Sync"]

    for repo, status in exists:
        table.add_row([repo, f"{Fore.GREEN}Match{Style.RESET_ALL}", sync_labels[status.value]])

    for repo in sorted(missing_locally):
        table.add_row([repo, f"{Fore.YELLOW}No Local{Style.RESET_ALL}", ""])

    for repo in sorted(missing_online):
        table.add_row([repo, f"{Fore.RED}No Repo{Style.RESET_ALL}", ""])

    print(table)

def status(path):
    known_repos = get_repos()
    exist_repos = list_folders(path)
    compare_repos(known_repos, exist_repos, path)

def clone_repo(name):
    subprocess.run(
        ['git', 'clone', name],
        capture_output=False, text=True, check=True
    )

def clone():
    known_repos = get_repos()
    exist_repos = list_folders(".")
    missing_locally = known_repos - exist_repos

    if len(missing_locally) == 0:
        print("All repositories already exist locally.")
        return

    confirm = input(f"Are you sure you want to clone {len(missing_locally)} repositories? [y/n]: ").lower()
    if confirm != 'y':
        print("Aborting clone operation.")
        return

    with ThreadPoolExecutor() as executor:
        future_to_repo = {executor.submit(clone_repo, f"git@github.com:mfacton/{repo}.git"): repo for repo in sorted(missing_locally)}
        for future in tqdm(as_completed(future_to_repo), total=len(future_to_repo), desc="Cloning Repos", bar_format="{l_bar}{bar}|{n_fmt}/{total_fmt}"):
            pass


def main():
    parser = argparse.ArgumentParser(description="Sync local repos with remote GitHub repos")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser('status', help="Show sync info")
    list_parser.add_argument(
        "-p", "--path",
        default=os.getcwd(),
        help="Path to the directory containing local repositories (default: current directory)"
    )

    subparsers.add_parser('clone', help="Clone remote repos that don't exist locally")

    args = parser.parse_args()

    if args.command == "status":
        status(args.path)
    elif args.command == "clone":
        clone()

if __name__ == "__main__":
    main()
