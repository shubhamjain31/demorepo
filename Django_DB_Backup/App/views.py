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
	collector = NestedObjects(using="default") # database name
	collector.collect([User.objects.get(pk=1)])

	objects = list(chain.from_iterable(collector.data.values()))
	with open("backup_export.json", "w") as f:
		s = serializers.serialize("json", objects, use_natural_foreign_keys=True, use_natural_primary_keys=True)
		s = re.sub('"pk": [0-9]{1,5}', '"pk": null', s)
		f.write(s)

	return HttpResponse('DOne')


def custom_command(request):
	# call_command("flush", verbosity=0, interactive=False)
	# apps = ','.join(map(str, app_name))
	filename = 'backup_export2'  # output filename here
	saveDir = open("{}.json".format(filename), 'w')

	# change application_name with your django app which you want to get backup from it
	call_command('dumpdata', 'App', stdout=saveDir, indent=4)
	saveDir.close()

	return HttpResponse('DOne')