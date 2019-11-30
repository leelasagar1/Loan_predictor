from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import approvereject,cxcontact,ApprovalsView,welcomeView

router = routers.DefaultRouter()
router.register('MyAPI', ApprovalsView)
urlpatterns = [
    #path('api/',include(router.urls)),
    #path('status/',approvereject),
    path('form/',cxcontact,name='cxform'),
    path('',welcomeView,name='home'),
]




