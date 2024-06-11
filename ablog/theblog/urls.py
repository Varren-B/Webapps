from django.urls import path
# from . import views
from .views import HomeVeiw, ArticleDetailView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeVeiw.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
]
