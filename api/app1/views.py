from django.shortcuts import render, redirect
from .models import Productos
from .forms import Inventarios

def item_list(request):
    items = Productos.objects.all()
    return render(request, 'app1/item_list.html', {'items': items})

def item_create(request):
    if request.method == 'POST':
        form = Inventarios(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = Inventarios()
    return render(request, 'app1/item_form.html', {'form': form})

def item_update(request, pk):
    item = Productos.objects.get(pk=pk)
    if request.method == 'POST':
        form = Inventarios(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = Inventarios(instance=item)
    return render(request, 'app1/item_form.html', {'form': form})

def item_delete(request, pk):
    item = Productos.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'app1/item_confirm_delete.html', {'item': item})