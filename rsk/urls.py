from django.urls import path
from rsk import views
app_name="rsk"

urlpatterns = [
    path('trail/',views.trail,name="trail"),
    path('profile/',views.profile,name="profile"),

]
