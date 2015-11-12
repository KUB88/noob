from django.db import models
from django.contrib import admin

class spiderGet(models.Model):
    #entry_id = AutoField()
    group = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    title_link = models.TextField()
    download_link = models.TextField()
    time_stamp = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title



class already_download(models.Model):
    #entry_id = AutoField()
    group = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    title_link = models.TextField()
    download_link = models.TextField()
    time_stamp = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.title


admin.site.register(spiderGet)
admin.site.register(already_download)


