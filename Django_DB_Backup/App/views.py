from django.shortcuts import render
from django.http import HttpResponse

from itertools import chain      

from django.contrib.auth.models import User
from django.core import serializers
from django.contrib.admin.utils import NestedObjects

from django.core.management import call_command
import re
from App.models import *

# Create your views here.

def index(request):
	return render(request, 'index.html')

def create_backup(request):

	# NestedObjects is admin contrib package which is used as a Collector subclass.
	collector = NestedObjects(using="default") # database name

	# create an object of NestedObjects
	collector.collect([User.objects.get(pk=7)])

	# create a list of all objects of all tables with foreign keys
	objects = list(chain.from_iterable(collector.data.values()))

	# store a data in file
	with open("backup_export1.json", "w") as f:
		s = serializers.serialize("json", objects, use_natural_foreign_keys=True, use_natural_primary_keys=True, indent = 4)
		s = re.sub('"pk": [0-9]{1,5}', '"pk": null', s)
		f.write(s)

	# delete user
	User.objects.get(pk=7).delete()
	return HttpResponse('DOne')


def restore_backup(request):

	# file name
	filename = 'backup_export1'

	# use call command for restore a data
	call_command('loaddata', '{}'.format(filename))

	return HttpResponse('DOne')