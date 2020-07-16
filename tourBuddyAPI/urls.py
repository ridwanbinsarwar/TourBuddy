from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from tourBuddyAPI.views.blog_api_views import ArticleAPIView, ArticleDetails
from tourBuddyAPI.views.accounts_api_views import RegistrationAPIView
urlpatterns = [
    path('article/', ArticleAPIView.as_view(), name="ArticleAPIView"),
    path('api-token-auth/', obtain_jwt_token, name='create-token'),
    path('detail/<int:id>/', ArticleDetails.as_view()),

    # accounts App Api urls
    path('account/register/', RegistrationAPIView.as_view(), name="RegistrationAPIView"),

]