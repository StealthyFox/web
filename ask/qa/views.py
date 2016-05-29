from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question, Answer
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_GET
from qa.forms import AskForm, AnswerForm

def paginate(request, qs):
	try:
		limit = int(request.GET.get('limit',10))
	except ValueError:
		limit = 10

	if limit > 100:
		limit = 10

	try:
		page = int(request.GET.get('page',1))
	except ValueError:
		raise Http404

	paginator = Paginator(qs, limit)

	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)  
	return page, paginator


def test(request, *args, **kwargs):
	return HttpResponse('OK')


def questions_list(request):
	qs = Question.objects.all()
	qs = qs.order_by('-added_at')
	page, paginator = paginate(request, qs)
	paginator.baseurl = reverse('questions_list')
	return render(request,'q_list.html', {'questions': page.object_list, 'paginator': paginator, 'page':page, })
	#return render(request,'questions_list.html', {'user':request.user, 'questions': page.object_list, 'paginator': paginator, 'page':page, })

def popular(request):
	qs = Question.objects.all()
	qs = qs.order_by('-rating')
	page, paginator = paginate(request,qs)
	paginator.baseurl = reverse('popular') + '?page='
	return render(request,'popular_q_list.html', {'questions': page.object_list, 'paginator': paginator, 'page':page, })

def question(request, pk):
	question = get_object_or_404(Question, id=pk)
	answers = Answer.objects.filter(question = question)
	form = AnswerForm(initial={'question': str(pk)})
	#form = AnswerForm(initial={'question': str(id)})
	return render(request, 'question.html', {
		'question' : question,
		'answers':answers, 
		'form': form,
	})

def question_ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            askquestion = form.save()
            url = reverse('question', args=[askquestion.id])
            return HttpResponseRedirect(url)
    else:
        form = AskForm()

    return render(request, 'ask.html', {
        'form': form
    })


def question_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = reverse('question', args=[answer.question.id])
            return HttpResponseRedirect(url)
    return HttpResponseRedirect('/')	
# Create your views here.
