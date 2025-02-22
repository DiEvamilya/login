from django.urls import path
from . import views
from .views import send_email_view

app_name ='blog'

urlpatterns = [
  path('', views.PostListView.as_view(), name='post_list'),
  # path('', views.post_list, name='post_list'),
  path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
  path('<int:post_id>/share/', views.post_share, name='post_share'),
  path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
  path('send-email/', send_email_view, name='send_email'),

]



