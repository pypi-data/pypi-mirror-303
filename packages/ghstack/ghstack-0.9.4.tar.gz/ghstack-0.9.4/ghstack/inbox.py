import ghstack.github
import json

def main(
    github: ghstack.github.GitHubEndpoint,
) -> None:
    print(json.dumps(github.get("notifications")))
