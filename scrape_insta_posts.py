from instascrape import Profile, Post
import requests

sessionid = requests.Session()

profile = Profile("<PROFILE URL HERE>").scrape(session=None)


# print(recent_posts)
