from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm
 
# Create your views here.

def note(request):
    notes = Note.objects
    '''Write down into the "unique words" variable
    the length of the set (unique list) of words in 
    the text field'''
    for x in notes.all():
    	if not x.u_words:
    		x.u_words = len(set(x.text.lower().split()))
    		x.save()
    '''Sort the queryset by the amount of unique words'''
    notes = Note.objects.order_by('u_words')
    template = loader.get_template('note.html')
    form = NoteForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    context = {'notes': notes, 'form': form,}
    return HttpResponse(template.render(context, request))
