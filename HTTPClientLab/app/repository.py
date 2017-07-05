


import requests
import json

class Repository(object):

    def __init__(self,url):

        self.url = url

    def browse_repository(self,author, repo, search_for='homepage'):


        url = "%s/%s/%s" % (self.url, author, repo)

        print ("Browsing Repository URL: %s" % url)
        result = requests.get(url)
        if(result.ok):
            repo_info = json.loads(result.text or result.content)
            print ("Github repository info for: %s" % repo)
            result = "No result found!"
            keys = []
            for key, value in repo_info.iteritems():
                if search_for in key:
                    result = value
            return result



