from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.db.models import Q

class UsernameOrEmailAuthBackend(object):
 
	def authenticate(self, request, username_or_email=None, password=None):
		""" Authenticate a user based on email address or user name. """
		try:
			user = User.objects.get(Q(username=username_or_email) | Q(email=username_or_email))
			if user.check_password(password):
				return user
		except User.DoesNotExist:
			return None

	def get_user(self, user_id):
		""" Get a User object from the user_id. """
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None