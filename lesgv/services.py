import requests

def get_blog_posts(params={}):
    url = 'https://blog.lesgrandsvoisins.com/ghost/api/content/posts/?key=1c04bede3eb01bfb3fb106b902'
    # print(url)
    for i in ["limit","order","filter","page","formats","include"]:
        if params.get("ghost_{}".format(i)):
            url += "&{}={}".format(i,params.get("ghost_{}".format(i)))
    response = requests.get(url)
    # print(url)
    ret = response.json()['posts']
    return ret


