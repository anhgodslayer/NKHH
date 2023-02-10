from django.shortcuts import render
from django.http import HttpResponse
import feedparser
# Create your views here.

def get_feed(request):
    feed_url = 'http://www.zone-h.org/rss/specialdefacements'
    blog_feed = feedparser.parse(feed_url)
    posts = blog_feed.entries
    post_list = []
    for post in posts:
        temp = dict()
        try:
            temp['title'] = post.title
            temp['link'] = post.link
            temp['guid'] = post.guid
            temp['summary'] = post.description
            temp['time_published'] = post.published
        except:
            return HttpResponse("None of DATA!!!")
        post_list.append(temp)
    return render (request, 'Scrape_app/scrape.html', {'data' : post_list})
