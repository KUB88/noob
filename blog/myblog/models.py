from django.db import models
from django.contrib import admin

# Create your models here.
class Articles(models.Model):
	STATUS_CHOICES = (
		('d', '草稿'),
		('p', '发表'),
	)

	title = models.CharField("标题", max_length = 150)
	article = models.TextField('正文')
	created_time = models.DateTimeField('创建时间', auto_now_add=True)
	last_mod_time = models.DateTimeField('修改时间', auto_now=True)
	status = models.CharField('文章状态', max_length = 1, choices = STATUS_CHOICES)
	tag = models.ManyToManyField('Tag', verbose_name = '标签', blank = True)

	def __str__(self):
		return self.title

class Tag(models.Model):
	name = models.CharField('标签名', max_length=30)

	def __str__(self):
		return self.name
	
	class Meta:
		ordering = ['name']
		verbose_name = '标签'
		verbose_name_plural = verbose_name

class ArticlesAdmin(admin.ModelAdmin):
	list_display = ('title',  'created_time', 'last_mod_time', 'status')

class TagAdmin(admin.ModelAdmin):
	list_display = ['name']

admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Tag, TagAdmin)