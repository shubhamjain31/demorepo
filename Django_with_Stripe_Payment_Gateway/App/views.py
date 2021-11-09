from django.shortcuts import render
from django.conf import settings

# Create your views here.

def index(request):
	params = {"key": settings.STRIPE_PUBLISHABLE_KEY}
	return render(request, "index.html", params)