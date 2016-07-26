from django.shortcuts import render, render_to_response
from myblog.models import Articles
from django.http import Http404

# Create your views here.
def index(request):
	article_list = Articles.objects.all()
	return render_to_response('home.html', {'article_list': article_list})

def detail(request, id):
    try:
        post = Articles.objects.get(id = str(id))
    except Articles.DoesNotExist:
        raise Http404
    return render_to_response('post.html', {'post': post})

