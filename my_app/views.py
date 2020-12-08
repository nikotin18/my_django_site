from django.shortcuts import render
from django.http import HttpResponse
from .models import Contract
from .forms import ContractForm
from django.utils import timezone
from django.shortcuts import redirect

def contract_new(request):
    if request.method == "POST":
        form = ContractForm(request.POST)

        if form.is_valid():
            contract = form.save(commit=False)
            contract.date_of_conclude = timezone.now()
            contract.save()
            return redirect('contracts_list')
    else:
        form = ContractForm()
        return render(request, 'my_app/contract_edit.html', {'form': form})

def contracts_list(request):
    contracts = Contract.objects.order_by('date_of_conclude')
    return render(request, 'my_app/contracts.html', {'contracts': contracts})
