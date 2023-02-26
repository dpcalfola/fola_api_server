from django.urls import path
from .views import Api1View

urlpatterns = [
    path('', Api1View.as_view(), name='api-1'),
    path('<int:number>/', Api1View.as_view(), name='api-1'),
]
