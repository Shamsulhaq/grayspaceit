from django.urls import path
from posts.views import posts, post_details

urlpatterns = [
    path('', posts, name='post'),
    path('<str:id>/', post_details, name='post-details')
]
