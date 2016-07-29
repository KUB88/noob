from django.shortcuts import render, render_to_response
from myblog.models import Articles
from django.http import Http404,HttpResponse

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

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        results = Articles.objects.filter(title = q)
        return render_to_response('home.html', {'article_list', results})
    else:
        return render_to_response('home.html', 'no such result')

def display_meta(request):
    values = request.META.items()
    html = []
    for k,v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>'%(k,v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
