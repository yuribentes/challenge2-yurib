from django.shortcuts import render
from .models import Transactions
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from .serieliazers import TransactionsSerializer
from rest_framework import generics
from decimal import Decimal


# Create your views here.
def parse_data(cnabdata):
    type_cnab = int(cnabdata[0:1])
    date_cnab = cnabdata[1:9].decode("utf-8")
    value_cnab = Decimal(int(cnabdata[9:19])/100)
    cpf_cnab = cnabdata[19:30].decode("utf-8")
    card_cnab = cnabdata[30:42].decode("utf-8")
    hour_cnab = cnabdata[42:48].decode("utf-8")
    owner_cnab = cnabdata[48:62].decode("utf-8")
    name_cnab = cnabdata[62:81].decode("utf-8")

    try:
        transaction = Transactions.objects.get(owner=owner_cnab)
    except Transactions.DoesNotExist:
        transaction = Transactions(
            owner=owner_cnab,
            value=0,
        )

    if (type_cnab == 2 or type_cnab == 3 or type_cnab == 9):
        transaction.value -= value_cnab
    else:
        transaction.value += value_cnab 

    transaction.type = type_cnab
    transaction.date = date_cnab
    transaction.cpf = cpf_cnab
    transaction.card = card_cnab
    transaction.hour = hour_cnab
    transaction.name = name_cnab

    transaction.save()


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        lines = request.FILES["file"].readlines()
        # print(lines)
        for line in lines:
            parse_data(line)
        return HttpResponseRedirect("/api/transactions/")
        # return HttpResponseRedirect("sucess.html")
    else:
        form = UploadFileForm()
        return render(request, "upload.html", {"form": form})



class TransactionsList(generics.ListCreateAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

