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
    for i in range(len(ret)):
        if ret[i]['feature_image']:
            ret[i]['feature_image_1000'] = ret[i]['feature_image'].replace("/content/images/", "/content/images/size/w1000/")
            ret[i]['feature_image_300'] = ret[i]['feature_image'].replace("/content/images/", "/content/images/size/w300/")
            ret[i]['feature_image_600'] = ret[i]['feature_image'].replace("/content/images/", "/content/images/size/w600/")
    return ret

def ProcessGhostParams(value={}):
    post_filter = value.get('post_filter') or ''
    if post_filter != '' and value.get('ghost_tag'):
        post_filter += ","
    if value.get('ghost_tag'):
        post_filter += "primary_tag:{}".format(value.get('ghost_tag'))
    params = {
        'ghost_limit':value.get('ghost_limit') or  15, 
        'ghost_include':value.get('ghost_include') or 'tags,authors',
        'ghost_order':value.get('ghost_order') or "",
        'ghost_filter':post_filter,
        'ghost_page':"{}".format(value.get('ghost_page') or 1)
    }
    return params

# def get_events(params={}):
#     info = xmlrpc.client.ServerProxy('https://ooo.lesgrandsvoisins.com.com/start').start()
#     url, db, username, password = info['host'], info['database'], info['user'], info['password']
