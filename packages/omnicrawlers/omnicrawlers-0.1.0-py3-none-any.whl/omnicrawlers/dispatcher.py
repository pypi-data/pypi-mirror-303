from linkedin_crawler import LinkedInCrawler 
from github_crawler import GithubCrawler

class Dispatcher:
    def __init__(self):
        self.linkedin_crawler = None
        self.github_crawler = GithubCrawler()
    def dispatch(self, link):
        if "linkedin.com/in/" in link:
            email = input("Enter LinkedIn username: ")
            password = input("Enter LinkedIn password: ")
            self.linkedin_crawler = LinkedInCrawler(email, password)
            print("Dispatching to LinkedIn Crawler...")
            self.linkedin_crawler.extract(link)
        elif "github.com/" in link:
            print("Dispatching to GitHub Crawler...")
            self.github_crawler.extract(link)
        else:
            print("Unsupported link format.")
if __name__ == "__main__":
    # Create a Dispatcher instance
    dispatcher = Dispatcher()

    # Prompt the user for the link to crawl
    link = input("Enter the LinkedIn or GitHub profile link: ").strip()

    # Dispatch the appropriate crawler based on the link
    dispatcher.dispatch(link)

