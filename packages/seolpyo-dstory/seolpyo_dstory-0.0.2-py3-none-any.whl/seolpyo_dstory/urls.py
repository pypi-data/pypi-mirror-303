from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.urls import path

from . import views

app_name = 'seolpyo_dstory'


urlpatterns = []

if settings.AUTH_USER_MODEL == 'seolpyo_dstory.User':
    urlpatterns += [
        path('user/login/', views.LoginView.as_view(), name='login'),
        path('user/logout/', views.LogoutView.as_view(), name='logout'),
    ]

urlpatterns += [
    path('', views.ListView.as_view(), name='list'),
    path('robots.txt/', views.robots),
    path('ads.txt/', views.adsense),
    path('naver<str:code>.html/', views.naver,),
    path('search/<str:keyword>/', views.SearchView.as_view(), name='search'),
    path('category/<str:category>/', views.CategoryListView.as_view(), name='category'),
    path('category/<str:category_parent>/<str:category>/', views.CategoryListView.as_view(), name='category'),

    path('post/', views.PostView.as_view(), name='post'),

    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.EditView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),

    path('entry/<str:slug>/', views.DetailView.as_view(), name='detail_slug'),

    path('notice/', views.NoticeListView.as_view(), name='list_notice'),
    path('notice/<int:pk>/', views.NoticeView.as_view(), name='notice'),

    path('pages/<int:pk>/', views.PageView.as_view(), name='page'),

    path('tag/<str:tag>/', views.TagListView.as_view(), name='tag'),

    path('rss/', views.FeedView(), name='rss'),
    path('sitemap.xml/', sitemap, views.sitemaps, name='django.contrib.sitemaps.views.sitemap',),
]

