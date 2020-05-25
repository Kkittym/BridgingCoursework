from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item

# Create your views here.

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/to-do')

    items = Item.objects.all()
    if (items.count() > 10):
        items.delete()
    return render(request, 'home.html', {'items': items})