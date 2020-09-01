from django.urls import path

from .views import PersonListView, PersonCreateView, PersonUpdateView

urlpatterns = [
        path('', PersonListView.as_view(), name='person_view'),
        path('add/', PersonCreateView.as_view(), name='person_add'),
        path('<int:pk>/', PersonUpdateView.as_view(), name='person_update'),
    ]

