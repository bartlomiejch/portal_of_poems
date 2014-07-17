# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.contrib import auth


from poems.models import Poem, Comment, Stropha


def poems(request):
    return render_to_response('poems/poems.html', {'poems':Poem.objects.all().order_by('like').reverse()})	

def poem(request, dupa = 1):
	return render_to_response('poems/poem.html', {'poem':Poem.objects.get(id = dupa) })



def comment(request, poem_id): # 403 Forbidden CSRF validation failed - ??
	if poem_id:
		if request.method == 'POST':
			title = request.POST.get('title')
			text_of_comment = request.POST.get('text_of_comment')
			nick = request.POST.get('nick')
			comment = Comment.objects.create(title = title, text = text_of_comment, nick = nick, poem = poem_id)
			comment.save()
			comments = Poem.objects.get(id = poem_id)
			all_comments = comments.poem_set.all()
			args = {}
			args.update(csrf(request))
			args['all_comments'] = all_comments
			return HttpResponseRedirect('/poems/get/%s' % poem_id, args)
		else:
			comments = Poem.objects.get(id = poem_id)
			all_comments = comments.poem_set.all()
			args = {}
			args.update(csrf(request))
			args['all_comments'] = all_comments
			return HttpResponseRedirect('/poems/get/%s' % poem_id, args)
			

def create(request):
	if request.method == 'POST':
		a = request.POST.get('poems_title')
		b = request.POST.get('poems_text')
		if request.user.is_authenticated():
			if a and b is not None: # do poprawki
				di = {}
				di.update(csrf(request))
				poem = Poem.objects.create(title = a, text = b)
				poem.save()
				return HttpResponseRedirect('/poems/all', di)
			else:
				message = 'Oba pola muszą być wypełnione'
				args = {}
				args['message'] = message
				args.update(csrf(request))
				return render_to_response('poems/create.html', args)
		else:
			message_to_not_user = 'Wiersze mogą dodawać tylko zalogowani użytkownicy - '
			arg = {}
			arg['message_to_not_user'] = message_to_not_user
			arg.update(csrf(request))
			return render_to_response('poems/create.html', arg)
			
	else:
		ar = {}
		ar.update(csrf(request))
		return render_to_response('poems/create.html', ar)


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
		a = request.POST.get('strofa')
		nowa_strofa = Stropha.objects.create(stropha = a)

	poetry = Stropha.objects.all()
	c ={'poetry': poetry}
	c.update(csrf(request))
	return render_to_response('poems/social_poem.html', c)	    
