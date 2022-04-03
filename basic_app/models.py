from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#defines a model class to add attributes to model User which it doesn't have
class UserProfileInfo(models.Model):

	#creating a relationship to User model
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	#additional attributes

	portfolio_site = models.URLField(blank=True)

	profile_pic = models.ImageField(upload_to='profile_pics', blank=True)


	def __str__(self):
		return self.user.username