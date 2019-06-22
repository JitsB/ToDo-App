from django.shortcuts import render, redirect, render_to_response
from .models import Lists
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponse

def home(request):
	if request.method == "POST":
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items = Lists.objects.all
			messages.success(request, ('Item has been added to the list!'))
			return render(request, 'home.html', {'all_items': all_items})
		else:
			message = "Code fatt raha hai"
			return render_to_response('home.html', {'form': form})
	
	else:
		all_items = Lists.objects.all
		return render(request, 'home.html', {'all_items' : all_items})


def delete(request, list_id):
	item = Lists.objects.get(pk = list_id)
	item.delete()
	messages.success(request, ("Item has been deleted"))
	return redirect('Home')


def cross_off(request, list_id):
	item = Lists.objects.get(pk = list_id)
	item.completed = True
	item.save()
	return redirect('Home')

def uncross(request, list_id):
	item = Lists.objects.get(pk = list_id)
	item.completed = False
	item.save()
	return redirect('Home')
