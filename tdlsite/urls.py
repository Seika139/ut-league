from django.urls import path
from . import views

urlpatterns = [
    # path( アクセスするアドレス, 呼び出す処理, 名前を指定)
    path('', views.index, name='index'),
]
