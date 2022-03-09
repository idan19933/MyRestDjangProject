from django.urls import path,include
from . import views
from rest_framework import routers
app_name = 'workers'

router = routers.DefaultRouter()
router.register("workers",views.WorkersView)

urlpatterns = [
    path("",views.home_view,name='home'),
    path('rest/',include(router.urls),name='rest'),
    path('<slug:slug>/', views.detail_view, name="detail"),
]





