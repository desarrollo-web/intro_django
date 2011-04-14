# Create your views here.
from django.template import Context, loader
from pastebin.models import Paste
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def manage(request):
    if request.method == 'POST':
        t  = request.POST.get('title', None)
        l  = request.POST.get('lang', None)
        c  = request.POST.get('content', None)

        snippet = Paste(title=t, lang=l, content=c)
        snippet.save()
    
    #obtener todos los snippets
    snippets = Paste.objects.all()
    #obtener la plantilla
    template = loader.get_template('pastebin/list.html')    
    context  = Context({'snippets': snippets})
    return HttpResponse(template.render(context))

def create(request):
    return render_to_response('pastebin/form.html',
                              {},
                              context_instance=RequestContext(request))

def show(request, snippet_id):
    s = Paste.objects.get(snippet_id)

    return render_to_response('pastebin/show.html',
                              {'snippet': s },
                              context_instance=RequestContext(request))
