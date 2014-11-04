PART TWO

The tutorial of Django is based on python 3.0+, but what I'm used to is python 2.7, that makes me progress a little slower.

The whole configuration thing is driving me crazy...

What I can get from 'https://hacker-news.firebaseio.com/v0/topstories.json' is a list of item ids. I can use their id to fetch all the useful information I need from HackerNews, then I can show the current top stories.

To get the monthly top stories, I need to check the type of all items, and select the story for each month with highest score. To easily do selection, I can store all the item information into sqlite, then use sql to select stories instead of parsing json.