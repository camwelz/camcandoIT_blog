from django.shortcuts import render

posts = [
    {
        'author': 'Cam',
        'title': 'First post',
        'content': 'First post content',
        'date_posted': 'Feb 18, 2023'
    },
    {
        'author': 'Cam',
        'title': 'Second post',
        'content': 'Second post content',
        'date_posted': 'Feb 19, 2023'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact'})