import requests
from django.shortcuts import render
from django.core.paginator import Paginator


# POSTS VIEW ENDPOINT
def posts(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts/').json()
    return render(request, 'blog-listing.html', {'response': response})


# POST DETAILS VIEW ENDPOINT
def post_details(request):
    return render(request, 'blog-post.html')
