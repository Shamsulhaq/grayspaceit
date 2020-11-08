from django.urls import path
from posts.views import posts, post_details

urlpatterns = [
    path('', posts, name='post'),
    path('details/', post_details, name='post-details'),
    # path('<int:id>/', post_details, name='post-details')
]
