from django.shortcuts import render

posts = [
    {
        'author': 'Tom',
        'title': 'Blog Post 1',
        'date': '01/01/2001',
    }, {
        'author': 'Jerry',
        'title': 'Blog Post 2',
        'date': '04/22/2023',
    }, {
        'author': 'Tiffany',
        'title': 'Blog Post 3',
        'date': '12/02/2006',
    }
]

def home(request):
    context = {
        'posts': posts,
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {"title": "About"})
