from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect

from poems.models import Poem, Comment, Stropha
from poems.forms import PoemForm, CommentForm, StrophaAddForm

def poems(request):
    return render_to_response('poems/poems.html', {'poems':Poem.objects.all().order_by('like').reverse()})	


def poem(request, dupa = 1):
	return render_to_response('poems/poem.html', {'poem':Poem.objects.get(id = dupa) })


def comment(request, poem_id, comment_id):
	if request.POST:
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('poems')
	return HttpResponseRedirect('poems/poem.html',{'comment':Comment.objects.get(id = comment_id)})


def create(request):
	if request.POST:
		form = PoemForm(request.POST)
		if form.is_valid():
			form.save()
		
			return HttpResponseRedirect('/poems/all')	
	else:
		form = PoemForm()

	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('poems/create.html', args)


def like_poem(request, poem_id):
    if poem_id:
        a = Poem.objects.get(id = poem_id)
        count = a.like
        count += 1
        a.like = count
        a.save()
        return HttpResponseRedirect('/poems/get/%s' % poem_id)


def social_poem(request):
	if request.method == "POST":
		form = StrophaAddForm(request.POST)
		if form.is_valid():
			my_model = Stropha()
			my_model.stropha = form.cleaned_data['add_stropha']
			my_model.save()

	form = StrophaAddForm()
	poetry = Stropha.objects.all()
	c ={'poetry': poetry, 'form':form}
	c.update(csrf(request))
	return render_to_response('poems/social_poem.html', c)	    


			
