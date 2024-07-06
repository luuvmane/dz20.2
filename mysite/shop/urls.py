from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('post/new/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('post/<slug:slug>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('post/<slug:slug>/edit/', BlogPostUpdateView.as_view(), name='blogpost_edit'),
    path('post/<slug:slug>/delete/', BlogPostDeleteView.as_view(), name='blogpost_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
