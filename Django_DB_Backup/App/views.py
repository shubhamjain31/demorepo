from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from itertools import chain      

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from django.core import serializers
from django.contrib.admin.utils import NestedObjects

from django.core.management import call_command
import re
from App.models import *

# Create your views here.

def index(request):
	return render(request, 'index.html')

def dbtable(request):
	all_users = User.objects.all()
	params = {'all_users':all_users}
	return render(request, 'backupandrestore.html', params)

@csrf_exempt
def create_backup(request):
	_pk = request.POST.get('_id')

	# user object
	user_obj = User.objects.get(pk=_pk)

	# NestedObjects is admin contrib package which is used as a Collector subclass.
	collector = NestedObjects(using="default") # database name

	# create an object of NestedObjects
	collector.collect([user_obj])

	# create a list of all objects of all tables with foreign keys
	objects = list(chain.from_iterable(collector.data.values()))

	# store a data in file
	with open("dbfiles/{}.json".format(user_obj.username), "w") as f:
		s = serializers.serialize("json", objects, use_natural_foreign_keys=True, use_natural_primary_keys=True, indent = 4)
		
		# make all tables objects pks null
		# s = re.sub('"pk": [0-9]{1,5}', '"pk": null', s)
		f.write(s)

	# delete all relation of user object
	# Post.objects.filter(author=user).delete()
	# Description.objects.filter(post_desc=user).delete()

	# response = HttpResponse(s, content_type='application/json')
	# response['Content-Disposition'] = 'attachment; filename=export.json'
	# return response
	data = {
        'msg': 'Backup Created Successfully'
    }
	return JsonResponse(data)


def restore_backup(request):

	# file name
	filename = 'dbfiles/backup_export3'

	# use call command for restore a data
	call_command('loaddata', '{}'.format(filename))

	return HttpResponse('DOne')