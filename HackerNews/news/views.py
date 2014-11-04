from django.shortcuts import render
from django.http import HttpResponse

def fetch_top_story():
    from urllib.request import urlopen
    from datetime import datetime
    import json
    top_stories_url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    item_url_format = 'https://hacker-news.firebaseio.com/v0/item/{0}.json'
    get_content = lambda url: urlopen(url).read().decode('utf8')

    story_ids = json.loads(get_content(top_stories_url))
    stories = sorted(filter(lambda story: datetime.fromtimestamp(int(story['time'])).year >= 2006,
        (json.loads(get_content(item_url_format.format(id))) for id in story_ids)),
        key = lambda story: int(story['time']),
        reverse = True)
    grouped_stories = [{'date': datetime.fromtimestamp(int(story['time'])), 'title': story['title'], 'score': int(story['score'])} for story in stories]
    print(grouped_stories)
    return grouped_stories

def index(request):
	grouped_stories = Qfetch_top_story()
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'grouped_stories': grouped_stories,
    })
    return HttpResponse(template.render(context))
# Create your views here.
