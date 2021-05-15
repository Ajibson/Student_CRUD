from django.contrib import admin
from django.urls import path,include


handler404 = 'first_model.views.view_404'
handler500 = 'first_model.views.view_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("first_model.urls")),
]



