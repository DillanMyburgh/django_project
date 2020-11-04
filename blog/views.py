from django.shortcuts import render

posts = [
    {
        'author': 'DillanM',
        'title': 'Blog Post 1',
        'content': 'My firts blog post',
        'date_posted': 'August 29, 2020'
    },
    {
        'author': 'Next dude',
        'title': 'Blog Post 2',
        'content': 'Some other dude posted on my site!',
        'date_posted': 'August 30, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
