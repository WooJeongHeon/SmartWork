from django.shortcuts import render, redirect
from .models import Post, Category, Tag, Comment # 현재 경로에서 models 에서 Post, Category, Tag, Comment를 import
from .forms import CommentForm
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class PostList(ListView):
    model = Post
    paginate_by = 5 # 5개 넘어가면 pagination 해라.


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        # .all 은 다가져오는거, .get은 1개만 가져오는거, .filter은 어떤 조건에 만족하는 경우만 가져오는거
        context['posts_without_category'] = Post.objects.filter(category=None).count()

        return context
    


class PostSearch(PostList): # PostList 클래스에서 한가지만 변하기 때문에 PostList를 가져옴.
#     원래 def get_queryset(self)는 ListView에 있지만 PostList에서 이미 가져왔기때문에 사용 가능.
    def get_queryset(self):
        q = self.kwargs['q']
        object_list = Post.objects.filter(Q(title__contains=q) | Q(content__contains=q))
        return object_list
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostSearch, self).get_context_data()
        context['search_info'] = 'Search: "{}"'.format(self.kwargs['q']) # post_list.html에서 search_info에 값 넣어줌.
        return context
    
    

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
    #         .all 은 다가져오는거, .get은 1개만 가져오는거, .filter은 어떤 조건에 만족하는 경우만 가져오는거
        context['posts_without_category'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm() # CommentForm()를 html로 넘겨준다.

        return context

    
class PostCreate(LoginRequiredMixin, CreateView): # LoginRequiredMixin: 로그인한사람만 접속할 수 있게 해줌
    model = Post
    fields = [
        'title', 'content', 'head_image', 'category', 'tags'
        # models.py에서 Post class에서 필요한것들만 가져옴, 'fields = __all__'하면 모두 가져오는건데 날짜랑 작성자는 일반 사용자가 수정하면 안되니까 빼고 나머지들만 가져옴.
    ]

    def form_valid(self, form):
        current_user = self.request.user # 현재 user을 current_user로 담음
        if current_user.is_authenticated: # 로그인 되어있을때
            form.instance.author = current_user
            return super(type(self), self).form_valid(form)
        else: # 로그인 하지 않은 user가 https://maindomain.com/blog/create/ 링크타고 올수 있으니까 예외 처리, 이렇게 들어와서 글쓰기 누르면 에러뜸.
            return redirect('/')
    
    
class PostUpdate(UpdateView):
    model = Post
    fields = [
        'title', 'content', 'head_image', 'category', 'tags' # models.py에서 Post class에서 필요한것들만 가져옴, 'fields = __all__'하면 모두 가져오는건데 날짜랑 작성자는 일반 사용자가 수정하면 안되니까 빼고 나머지들만 가져옴.
    ]
    
    
    
class PostListByTag(ListView):
    def get_queryset(self):
        tag_slug = self.kwargs['slug']
        tag = Tag.objects.get(slug=tag_slug)

        return tag.post_set.order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(type(self), self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count()
        tag_slug = self.kwargs['slug']
        context['tag'] = Tag.objects.get(slug=tag_slug)

        return context


class PostListByCategory(ListView):

    def get_queryset(self):
        slug = self.kwargs['slug'] # urls.py에서 <str:slug> slug를 가져옴.

        if slug == '_none':
            category = None
        else:
            category = Category.objects.get(slug=slug)

        return Post.objects.filter(category=category).order_by('-created')
    

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(type(self), self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count()

        slug = self.kwargs['slug']

        if slug == '_none':
            context['category'] = '미분류'
        else:
            category = Category.objects.get(slug=slug)
            context['category'] = category # post_list.html에 category로 넘겨줌.

        # context['title'] = 'Blog - {}'.format(category.name)
        return context
    



def new_comment(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST) #CommentForm에 포스트로 넘긴 데이터를 가져온다. (지금은 text밖에 없음.) -> forms.py에서 text만 넘겨줬으니까.
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # post와 author도 채워줘야하기때문에 comment_form을 저장하지 말고 가져와라
            comment.post = post
            comment.author = request.user
            comment.save() #3개 다 채웠으니까 이제 저장.
            return redirect(comment.get_absolute_url())
    else:
        return redirect('/blog/')
    

class CommentUpdate(UpdateView):
    model = Comment
    form_class = CommentForm # forms.py에서 CommentForm을 사용함

    def get_object(self, queryset=None):
        comment = super(CommentUpdate, self).get_object()
        if comment.author != self.request.user: # 댓글 작성자와 현재 로그인 자가 같지 않은 경우.
            raise PermissionError('Comment 수정 권한이 없습니다.') # 에러를 발생.
        return comment
    
    
def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    post = comment.post
    if request.user == comment.author: # 댓글 작성자가 로그인 했을 때.
        comment.delete()
        return redirect(post.get_absolute_url() + '#comment-list')
    else: #로그인을 다른 사람이 했을때.
        # return redirect('/blog/') # /blog/로 리다이렉드
        raise PermissionError('Comment 삭제 권한이 없습니다.') #에러 발생하게 만듬.
    

