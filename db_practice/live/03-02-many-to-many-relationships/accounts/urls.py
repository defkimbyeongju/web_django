from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('profile/<str:username>/', views.profile, name='profile'), # 앞에 profile을 넣어준 이유는 <username>만 넣으면 그 뒤에 오는 url을 다 이름으로 인식해버릴 수 있기 때문에
    path('<int:user_pk>/follow/', views.follow, name='follow')
]
