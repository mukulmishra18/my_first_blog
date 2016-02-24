from django.db import models
from django.utils import timezone


class Post(models.Model):        #models.Model means Post is an django model and it is saves under database
	author = models.ForeignKey('auth.User') # Link to another model
	title = models.CharField(max_length=200) # defining text field of limited characters
	text = models.TextField()    # text field without limitations of text limit
	created_date = models.DateTimeField(   # date and time
			default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):  # return text(string) of title
		return self.title



