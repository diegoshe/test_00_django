from django.urls import path, include
from .views import IndexView, InputView, OutputView

app_name = 'input_output'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('input/', InputView.as_view(), name='input'),
    path('output/', OutputView.as_view(), name='output'),
]