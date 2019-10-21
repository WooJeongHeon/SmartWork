from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown # markdownx 모듈 사용


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True) # 글자수 제한: 25, 중복 방지
    description = models.TextField(blank=True) # 카테고리에대한 설명, blank=True: 안써도 됨

    slug = models.SlugField(unique=True, allow_unicode=True) # allow_unicode=True: 한글 가능, 사용자가 카테고리 name을 쓰면 자동으로 slug 만들어지게 할거임.(url에 카테고리 이름 구성하려고)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/msgboards/category/{}/'.format(self.slug)

    class Meta:
        verbose_name_plural = 'categories'


class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/msgboards/tag/{}/'.format(self.slug)


class Post(models.Model):
    title = models.CharField(max_length=30) # 블로그에서 글의 제목, 길이 제한 30
    # content = models.TextField() # 글에 들어갈 내용
    content = MarkdownxField() # 마크다운x 모듈 사용함.

    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)
    # upload_to='blog/%Y/%m/%d/'경로에 사진 업로드, 한 폴더에 이미지파일이 여러개 쌓이면 컴퓨터가 찾는데 오래걸려서 /%Y/%m/%d/ 날짜 단위로 분류
    # blank=True: 사용자가 꼭 채우지 않아도 된다는 뜻

    created = models.DateTimeField(auto_now_add=True) # 언제 작성 되었는지, auto_now_add=True를 넣으면 자동으로 현재 시간 채워짐.
    author = models.ForeignKey(User, on_delete=True) # 어떤 사용자가 사용 했는지, 사용자가 삭제(탈퇴) 됐을때 글도 삭제 = True

    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True) # null=True, blank=True: 테그는 없어도 됨
    
    class Meta:
        ordering = ['-created', ] # 작성날짜 역순(최신순)으로 표시, 이거 Meta 없애면 작성일 순서대로 표시.

    def __str__(self):
        return '{} :: {}'.format(self.title, self.author) # 제목 미리보기 형식

    def get_absolute_url(self): # admin 페이지의 VIEW ON SITE 정의
        return '/msgboards/{}/'.format(self.pk)
    
    def get_update_url(self):
        return self.get_absolute_url() + 'update/'

    def get_markdown_content(self): # 드래그엔 드롭으로 사진넣은거 보여주기 위해 html로 넘겨줄거임.
        return markdown(self.content)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # ForeignKey: 다대 일 구조, Post 한개에 여러개의 댓글이 가능
    text = MarkdownxField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete=models.CASCADE: 사용자가 탈퇴했을때 삭제함.
    created_at = models.DateTimeField(auto_now_add=True) # 작성한 시간 추가
    modified_at = models.DateTimeField(auto_now=True)
    
    def get_markdown_content(self): # 이거 넣으면 댓글에도 마크다운 적용 가능함
        return markdown(self.text)
    
    def get_absolute_url(self):
        return self.post.get_absolute_url() + '#comment-id-{}'.format(self.pk) #해당 댓글 달린 위치로 이동시켜주려고 '#comment-id-{}'.format(self.pk) 붙임, url에 적용.

