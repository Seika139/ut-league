from django.urls import path
from .views import HelloView

urlpatterns = [
    # path( アクセスするアドレス, 呼び出す処理, htmlで {% url 'name' % として使う})
    path('', HelloView.as_view() , name='index'),
]
