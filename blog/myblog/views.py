from django.shortcuts import render, render_to_response
from myblog.models import Articles

# Create your views here.
def index(request):
	article_list = Articles.objects.all()
	return render_to_response('posts.html', {'article_list': article_list})
