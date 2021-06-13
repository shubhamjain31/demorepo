##------------------------------------------------------Demo File --------------------------------------##

def create_backup(request):
	_pk = 11

	# NestedObjects is admin contrib package which is used as a Collector subclass.
	collector = NestedObjects(using="default") # database name

	# create an object of NestedObjects
	collector.collect([User.objects.get(pk=_pk)])

	# create a list of all objects of all tables with foreign keys
	objects = list(chain.from_iterable(collector.data.values()))

	# store a data in file
	with open("dbfiles/backup_export3.json", "w") as f:
		s = serializers.serialize("json", objects, use_natural_foreign_keys=True, use_natural_primary_keys=True, indent = 4)
		
		# make all tables objects pks null
		# s = re.sub('"pk": [0-9]{1,5}', '"pk": null', s)
		f.write(s)

	# user object
	user = User.objects.get(pk=_pk)

	# delete all relation of user object
	Post.objects.filter(author=user).delete()
	Description.objects.filter(post_desc=user).delete()
	return HttpResponse('DOne')


def restore_backup(request):

	# file name
	filename = 'dbfiles/backup_export3'

	# use call command for restore a data
	call_command('loaddata', '{}'.format(filename))

	return HttpResponse('DOne')