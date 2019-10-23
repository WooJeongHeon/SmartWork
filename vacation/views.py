from django.shortcuts import render, redirect
from .models import Vacation
from AdminPages.models import MsgBoards
from MessageBoards.models import Category
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

class VacationList(ListView):
    model = Vacation
    paginate_by = 5 # 5개 넘어가면 pagination 해라.



    
class VacationDetail(DetailView):
    model = Vacation



    
class VacationCreate(LoginRequiredMixin, CreateView): # LoginRequiredMixin: 로그인한사람만 접속할 수 있게 해줌
    model = Vacation
    fields = [
        'rank', 'vacation_type', 'content', 'start_date', 'end_date', 'destination'
        # models.py에서 Vacation class에서 필요한것들만 가져옴, 'fields = __all__'하면 모두 가져오는건데 날짜랑 작성자는 일반 사용자가 수정하면 안되니까 빼고 나머지들만 가져옴.
    ]

    def form_valid(self, form):
        current_user = self.request.user # 현재 user을 current_user로 담음
        if current_user.is_authenticated: # 로그인 되어있을때
            form.instance.author = current_user
            # form.instance.category = Category.objects.filter(category=None)
            return super(type(self), self).form_valid(form)
        else: # 로그인하지 않은 사용자 처리
            return redirect('/')
	

    
class VacationUpdate(UpdateView):
    model = Vacation
    fields = [
        'vacation_type', 'content', 'start_date', 'end_date' # models.py에서 Vacation class에서 필요한것들만 가져옴, 'fields = __all__'하면 모두 가져오는건데 날짜랑 작성자는 일반 사용자가 수정하면 안되니까 빼고 나머지들만 가져옴.
    ]
	
class VacationSearch(VacationList):
    def get_queryset(self):
        q = self.kwargs['q']
        object_list = Vacation.objects.filter(Q(vacation_type__contains=q) | Q(content__contains=q))
        return object_list
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VacationSearch, self).get_context_data()
        context['search_info'] = 'Search: "{}"'.format(self.kwargs['q']) # post_list.html에서 search_info에 값 넣어줌.
        return context
    
    
