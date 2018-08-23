from django.shortcuts import render, render_to_response
from django.template import loader
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm
 
# Create your views here.

def home(request):
    notes = Note.objects
    template = loader.get_template('note.html')
    form = NoteForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save() 
 
    context = {'notes': notes, 'form': form}
    return HttpResponse(template.render(context, request))
    # return render(request, 'note.html', context)
    #return render_to_response("note.html", notes)

# def home(request):
#     notes = Note.objects
#     template = loader.get_template('note.html')
#     context = {'notes': notes}
#     return render(request, 'note.html', context)
#     #return render_to_response("note.html", notes)

# def home(request):
#     notes = Note.objects
#     # return HttpResponse(notes)
#     template = loader.get_template('note.html')
#     context = {'notes': notes,}
#     return HttpResponse(template.render(context, request))
#     # return render(request, 'note.html', context)
#     # return render_to_response("note.html", notes)
