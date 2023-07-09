import requests

def get_blog_posts():
    response = requests.get('https://blog.lesgrandsvoisins.com/ghost/api/content/posts/?key=1c04bede3eb01bfb3fb106b902&limit=6&include=tags,authors')
    ret = response.json()['posts']
    return ret
