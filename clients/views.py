from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm
from django.contrib.auth.decorators import login_required

@login_required
def people_list(request):
    clients = Client.objects.all()
    return render(request, "human.html", {"clients": clients})

@login_required
def people_new(request):
    form = ClientForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("people_list")
    return render(request, "peopleform.html", {"form": form})

@login_required
def people_update(request, id):
    client = get_object_or_404(Client, pk = id)
    form = ClientForm(request.POST or None, request.FILES or None, instance = client)

    if form.is_valid():
        form.save()
        return redirect("people_list")
    return render(request, "peopleform.html", {"form": form})

@login_required
def people_delete(request, id):
    client = get_object_or_404(Client, pk = id)

    if request.method == "POST":
        client.delete()
        return redirect("people_list")
    return render(request, "people_confirm_delete.html", {"client": client})

# Create your views here.
