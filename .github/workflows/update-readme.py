import requests
import os

token = os.environ["GITHUB_TOKEN"]
username = "pyguy-programming"

headers = {"Authorization": f"token {token}"}
repos = requests.get(f"https://api.github.com/users/{username}/repos?sort=updated&per_page=100", headers=headers).json()

repo_list = "\n".join([
    f'<a href="{r["html_url"]}"><img src="https://github-readme-stats.vercel.app/api/pin/?username={username}&repo={r["name"]}&theme=react" alt="{r["name"]}"></a>'
    for r in repos if not r['fork']
])

with open("README.md", "r") as f:
    readme = f.read()

new_readme = readme.split("<!-- REPOS_START -->")[0]
new_readme += "<!-- REPOS_START -->\n" + repo_list + "\n<!-- REPOS_END -->"
new_readme += readme.split("<!-- REPOS_END -->")[1]

with open("README.md", "w") as f:
    f.write(new_readme)