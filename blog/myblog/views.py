from django.shortcuts import render, render_to_response
from myblog.models import Articles
from django.http import Http404,HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    articles = Articles.objects.filter(status = 'p')
    paginator = Paginator(articles,5)
    page = request.GET.get('page')
    try :
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.paginator(paginator.num_pages)
    return render_to_response('myblog/index.html', {'article_list': article_list})

def detail(request, id):
    try:
        post = Articles.objects.get(id = str(id))
    except Articles.DoesNotExist:
        raise Http404
    return render_to_response('post.html', {'post': post})

def archives(request):
    try:
        post_list = Articles.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list': post_list, 'error': False})

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        results = Articles.objects.filter(title = q)
        if len(results) == 0:
            return render_to_response('archives.html', {'post_list': results, 'error': True})
        else:
            return render_to_response('archives.html', {'post_list': results, 'error': False})
    else:
        return redirect('/')

def display_meta(request):
    values = request.META.items()
    html = []
    for k,v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>'%(k,v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
