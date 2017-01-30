from django.shortcuts import redirect,render
from django.http import HttpResponse
from superlists.models import Item, List

# Create your views here.

#First Page that loaded
def home_page(request):
    #If the page accessed without any parameter passed
    return render(request, 'home.html')


#Page that show the list
def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

#Page for submitting new to do lists
def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')

