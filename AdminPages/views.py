from django.shortcuts import render
from .models import MsgBoards
from django.views.generic import ListView

def index(request):
    return render(
        request,
        'admin_index.html'
    )

def msgboards(request):
    return render(
        request,
        'msgboards.html'
    )


class PostList(ListView):
    # model = Post
    paginate_by = 5 # 5개 넘어가면 pagination 해라.


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['category_list'] = MsgBoards.objects.all()
        # .all 은 다가져오는거, .get은 1개만 가져오는거, .filter은 어떤 조건에 만족하는 경우만 가져오는거
        context['posts_without_category'] = Post.objects.filter(category=None).count()

        return context