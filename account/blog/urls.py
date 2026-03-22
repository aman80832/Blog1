from django.urls import path
from.import views
urlpatterns=[
    path('posts/',views.home,name='home'),
    path('profile/',views.profile_detalis,name='profile'),
    path('posts/add/',views.AddblogView.as_view(),name='add_blogs'),
    path('comments/',views.comments_page,name='comments_page'),
    path('author/<int:id>/', views.author_posts, name='author_posts'),
    path('profile/add/',views.AddProfile.as_view(),name='add_profile'),
    path('post/<int:pk>/comment/', views.AddCommentsView.as_view(), name='add_comment'),
]