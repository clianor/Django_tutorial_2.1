from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published question."""
        return Question.objects.order_by('-pub_date')[:5]
# end class

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
# end class

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
# end class

def vote(request, question_id):
    """polls 투표 뷰"""
    try:
        question = get_object_or_404(Question, pk=question_id)    # 데이터를 가져오고 404 에러를 확인한다.
    except:
        raise Http404("질문이 존재하지 않습니다(vote)")
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])    # choice 데이터를 가져오고 없으면 에러를 띄운다.
    except KeyError:
        # KeyError 발생시 에러 메세지와 함께 detail 뷰를 다시 보여준다.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "아무것도 고르지 않으셨습니다.",
        })
    else:
        selected_choice.votes += 1    # choice 데이터가 있어서 에러가 발생하지 않았을때 1을 더함.
        selected_choice.save()    # choice 데이터를 save 즉 commit 한다.

        # POST 데이터를 성공적으로 처리한 이후에는 무조건 HttpResponseRedirect를 호출하여야 합니다.
        # HttpResponseRedirect를 통해 결과 뷰로의 연결을 해줍니다.
        # 이것은 장고만이 아니라 웹 개발 권장사항입니다.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
# end def