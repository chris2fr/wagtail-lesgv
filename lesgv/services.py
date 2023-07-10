import requests
import urllib.parse
import xmlrpc.client

def get_blog_posts(params={}):
    url = 'https://blog.lesgrandsvoisins.com/ghost/api/content/posts/?key=1c04bede3eb01bfb3fb106b902'
    # print(url)
    for i in ["limit","order","filter","page","formats","include"]:
        if params.get("ghost_{}".format(i),False):
            url += "&{}={}".format(i,urllib.parse.quote("{}".format(params.get("ghost_{}".format(i)))))
    response = requests.get(url)
    # print(url)
    ret = response.json()['posts']
    return ret


def get_events(params={}):
    
    info = xmlrpc.client.ServerProxy('https://ooo.lesgrandsvoisins.com.com/start').start()
    url, db, username, password = info['host'], info['database'], info['user'], info['password']
