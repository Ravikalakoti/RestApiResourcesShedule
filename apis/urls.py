from django.urls import include,path
from rest_framework import routers
from .views import *
router=routers.DefaultRouter()
router.register(r'ravi',MyViewSet)
urlpatterns=[
	path('',include(router.urls)),
	path('api/',include('rest_framework.urls')),
]