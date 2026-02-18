from django.shortcuts import render

from contact.admin import *


def index(request):
	return render(
		request,
		'contact/index.html',
	)
