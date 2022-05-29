from django.urls import path

from . import views

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('automobiliai/', views.automobiliai, name='automobiliai'),
    path('automobiliai/<int:automobilis_id>', views.automobilis, name='automobilis'),
    path('užsakymai/', views.UžsakymaiListView.as_view(), name='užsakymai'),
    path('užsakymai/<int:pk>', views.UžsakymasDetailView.as_view(), name='užsakymas'),
]