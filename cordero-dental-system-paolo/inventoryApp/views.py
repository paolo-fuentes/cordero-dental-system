from django.shortcuts import render

# Create your views here.
def hello_world(request):
	return render(request, 'inventoryApp/hello_world.html')