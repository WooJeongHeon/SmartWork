from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown # markdownx 모듈 사용


class MsgBoards(models.Model):
    name = models.CharField(max_length=25, unique=True) # 글자수 제한: 25, 중복 방지
    description = models.TextField(blank=True) # 게시판에대한 설명, blank=True: 안써도 됨

    slug = models.SlugField(unique=True, allow_unicode=True) # allow_unicode=True: 한글 가능, 사용자가 게시판 name을 쓰면 자동으로 slug 만들어지게 할거임.(url에 게시판 이름 구성하려고)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return '/msgboards/category/{}/'.format(self.slug)

    class Meta:
        verbose_name_plural = 'MsgBoards'
