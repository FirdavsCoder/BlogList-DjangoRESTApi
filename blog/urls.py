from django.urls import path
from .views import BlogListView, BlogDetail


urlpatterns = [
    path('', BlogListView.as_view(), name = 'blog_list'),
    path('<int:pk>', BlogDetail.as_view(), name = 'blog_detail')
]