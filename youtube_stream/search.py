import re, urllib.parse, urllib.request
from .commands import get_list

def get_link(music_name):
    query= urllib.parse.urlencode({"search_query": music_name.rstrip().lstrip()})
    searchUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query)
    search_results = re.findall(r"watch\?v=(\S{11})", searchUrl.read().decode())
    return "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

def search(query):
    queries=get_list(query)
    links = ""
    for query in queries:
        if query == "": continue
        links+=get_link(query)+" "
    return links