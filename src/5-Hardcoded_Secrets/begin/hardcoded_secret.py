"""Log in to GitHub's API with credentials supplied by the user.

Use this only with a GitHub account you own and a token created for that
account. GitHub does not support using an account password for API login.
"""

import base64
import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


# Replace these placeholders with your own values.
GITHUB_USERNAME = "your-github-username"
GITHUB_TOKEN = "your-github-personal-access-token"
GITHUB_USER_ENDPOINT = "https://api.github.com/user"


def login_to_github(username: str, token: str) -> dict:
	"""Authenticate to GitHub and return the authenticated user's profile."""
	credentials = f"{username}:{token}".encode("utf-8")
	encoded_credentials = base64.b64encode(credentials).decode("ascii")
	request = Request(
		GITHUB_USER_ENDPOINT,
		headers={
			"Accept": "application/vnd.github+json",
			"Authorization": f"Basic {encoded_credentials}",
			"User-Agent": "github-login-example",
		},
	)

	try:
		with urlopen(request, timeout=15) as response:
			return json.load(response)
	except HTTPError as error:
		if error.code in (401, 403):
			raise RuntimeError("GitHub rejected the username or token.") from error
		raise RuntimeError(f"GitHub returned HTTP {error.code}.") from error
	except URLError as error:
		raise RuntimeError(f"Could not reach GitHub: {error.reason}") from error


if __name__ == "__main__":
	profile = login_to_github(GITHUB_USERNAME, GITHUB_TOKEN)
	print(f"Logged in to GitHub as {profile['login']}.")
