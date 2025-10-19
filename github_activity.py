import sys
import json
import urllib.request
import urllib.error

def fetch_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    headers = {"User-Agent": "github-activity-cli"}

    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            data = json.load(response)
            return data
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"User '{username}' not found.")
        else:
            print(f"HTTP Error: {e.code}")
    except urllib.error.URLError:
        print("Failed to reach the server.")
    return None

def parse_event(event):
    type = event["type"]
    repo = event["repo"]["name"]
    payload = event.get("payload", {})

    if type == "PushEvent":
        commits = payload.get("commits", [])
        count = len(commits)
        if count == 0:
            return None
        return f"- Pushed {count} commit(s) to {repo}"
    elif type == "IssuesEvent":
        action = payload.get("action", "did something")
        return f"- {action.capitalize()} an issue in {repo}"
    elif type == "WatchEvent":
        return f"- Starred {repo}"
    elif type == "ForkEvent":
        return f"- Forked {repo}"
    elif type == "PullRequestEvent":
        action = payload.get("action", "did something")
        return f"- {action.capitalize()} a pull request in {repo}"
    else:
        return f"- {type} in {repo}"

def display_activity( events):
    if not events:
        print("No recent activity found.")
        return
    for event in events[:10]:
        parsed = parse_event(event)
        if parsed:
            print(parsed)



def main():
    if len(sys.argv) != 2:
        print("Usage: python github-activity.py <username>")
        return
    username = sys.argv[1]
    events = fetch_activity(username)
    if events is not None:
        display_activity(events)

if __name__ == "__main__":
    main()
