from django.db import models


class Poem(models.Model):
	title = models.CharField(max_length = 200)
	text = models.TextField()
	pub_date = models.DateTimeField(auto_now_add = True)
	like = models.IntegerField(default = 0)


	def __str__(self):
		return self.title

class Comment(models.Model):
	title = models.CharField(max_length = 200)
	text = models.TextField()
	pub_date = models.DateTimeField(auto_now_add = True)
	nick = models.CharField(max_length= 100)
	poem = models.ForeignKey(Poem, null=True)


class Stropha(models.Model):
	stropha = models.CharField(max_length=200)
