from django.urls import path, include
from .views import ArticleAPIView, ArticleDetails
urlpatterns = [
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    # path('article/', article_list),

]