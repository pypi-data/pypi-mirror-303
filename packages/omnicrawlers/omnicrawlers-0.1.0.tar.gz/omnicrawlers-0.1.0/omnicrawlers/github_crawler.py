import subprocess
import os
import tempfile

class GithubCrawler:
    def extract(self, repo_link):
        print(f"Cloning repository: {repo_link}")

        local_temp = tempfile.mkdtemp()

        try:
            os.chdir(local_temp)
            subprocess.run(["git", "clone", repo_link])

            repo_name = repo_link.rstrip("/").split("/")[-1]
            repo_path = os.path.join(local_temp, repo_name)

            tree = {}
            for root, dirs, files in os.walk(repo_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", errors="ignore") as f:
                        tree[file_path] = f.read()
            return tree  # Print the content of the repository

        finally:
            return "Done"
