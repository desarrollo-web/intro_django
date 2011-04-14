#encoding=utf-8
# Create your views here.
from django.template import Context, loader
from pastebin.models import Paste
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse

def manage(request):
    if request.method == 'POST':
        t  = request.POST.get('title', None)
        l  = request.POST.get('lang', None)
        c  = request.POST.get('content', None)

        snippet = Paste(title=t, lang=l, content=c)
        snippet.save()
    
    #Filtrar:
    lang = request.GET.get('l', None)
    query = request.GET.get('q', None)
    #obtener todos los snippets
    snippets = Paste.objects.all()
    #snippets es un QuerySet, y éstos son encadenables (se les
    #pueden aplicar otros querysets)
    if lang:
        snippets = snippets.filter(lang=lang)
    if query:
        snippets = snippets.filter(title__icontains=query)
    #obtener la plantilla
    template = loader.get_template('list.html')    
    context  = Context({'snippets': snippets, 'langs': Paste.LANGS, 'choice':lang})
    return HttpResponse(template.render(context))

def create(request):
    return render_to_response('form.html',
                             {"langs": Paste.LANGS},
                              context_instance=RequestContext(request))

def show(request, snippet_id):
    s = Paste.objects.get(pk=snippet_id)

    return render_to_response('show.html',
                              {'snippet': s },
                              context_instance=RequestContext(request))
