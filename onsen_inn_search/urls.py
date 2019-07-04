from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('onsen_inn_search', TemplateView.as_view(template_name='onsen_inns/index.html')),
]
