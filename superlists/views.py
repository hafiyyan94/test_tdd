from django.shortcuts import redirect,render
from django.http import HttpResponse
from superlists.models import Item, List
from superlists.forms import ItemForm
from django.core.exceptions import ValidationError

# Create your views here.

#First Page that loaded
def home_page(request):
    #If the page accessed without any parameter passed
    return render(request, 'home.html', {'form': ItemForm()})


#Page for submitting new to do lists
def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            form.save(for_list=list_)
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, "form": form})
