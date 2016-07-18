from django.db import models
from django.contrib import admin

# Create your models here.
class Articles(models.Model):
	title = models.CharField(max_length = 150)
	article = models.TextField()
	timestamp = models.DateTimeField()
	tag = models.CharField(max_length = 150)

class ArticlesAdmin(admin.ModelAdmin):
	list_display = ('title',  'tag', 'timestamp')

admin.site.register(Articles, ArticlesAdmin)