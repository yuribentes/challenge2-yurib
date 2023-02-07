from django.urls import path

from . import views

urlpatterns = [
    path("transactions/", views.upload_file, name='upload'),
    path("transactionslist/", views.TransactionsList.as_view(), name='list')
]