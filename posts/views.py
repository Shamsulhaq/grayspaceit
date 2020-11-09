import requests
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# POSTS VIEW ENDPOINT
def posts(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts/').json()
    paginator = Paginator(response, 5)
    page = request.GET.get('page')

    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)
    # for p in paginator:
    #     print(p)
    # print(paginator.num_pages)
    # print(response)
    template_name = 'blog-listing.html'
    context = {
        'response': response
    }
    # print(context)
    return render(request, template_name, context)


# POST DETAILS VIEW ENDPOINT
def post_details(request, id):
    response = requests.get('https://jsonplaceholder.typicode.com/posts/{}'.format(id)).json()
    comments = requests.get('https://jsonplaceholder.typicode.com/posts/{}/comments'.format(id)).json()
    template_name = 'blog-post.html'
    context = {
        'response': response,
        'comments': comments
    }
    return render(request, template_name, context)
