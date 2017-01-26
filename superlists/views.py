from django.shortcuts import redirect,render
from django.http import HttpResponse
from superlists.models import Item

# Create your views here.

def home_page(request):

    #If the page using POST Method
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    #If the page accessed without any parameter passed
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})