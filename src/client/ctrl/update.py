import requests
import subprocess


def check_for_updates():
    # Replace with your project's GitHub repository URL
    repo_url = "https://github.com/lkgames256/ctrl.git"

    # Make an HTTP GET request to the GitHub API endpoint
    response = requests.get(f"{repo_url}/commits/HEAD")

    # Extract the latest commit hash from the JSON response
    latest_commit_hash = response.json()["sha"]

    # Use the git CLI to determine the current commit hash
    current_commit_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf-8").strip()

    # Check if an update is available
    is_up_to_date = latest_commit_hash == current_commit_hash

    if not is_up_to_date:
        # Update the local repository using git CLI
        subprocess.run(["git", "clone", "--depth=1", repo_url])
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "Update from GitHub"])
        subprocess.run(["git", "push", "origin", "master"])
    else:
        print("Your local repository is up to date.")


if __name__ == "__main__":
    check_for_updates()
