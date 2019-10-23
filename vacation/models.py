from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown # markdownx 모듈 사용


        
class Vacation(models.Model):
    vacation_type = models.CharField("출타 종류", max_length=10) # 출타종류, 길이 제한 10
    # content = models.TextField() # 글에 들어갈 내용
    content = MarkdownxField("출타 계획서") # 마크다운x 모듈 사용함.


    created = models.DateTimeField(auto_now_add=True) # 언제 작성 되었는지, auto_now_add=True를 넣으면 자동으로 현재 시간 채워짐.
    start_date = models.DateTimeField("출발 일자")
    end_date = models.DateTimeField("도착 일자")
    author = models.ForeignKey(User, on_delete=True) # 어떤 사용자가 사용 했는지, 사용자가 삭제(탈퇴) 됐을때 글도 삭제 = True
    rank = models.CharField("계급", max_length=10)
    destination = models.CharField("행선지", max_length=10)
    is_approval = models.CharField("승인 여부", blank=True, null=True, max_length=10)
    days = models.CharField("휴가 일수", blank=True, null=True, max_length=10)




    class Meta:
        ordering = ['-created', ] # 작성날짜 역순(최신순)으로 표시, 이거 Meta 없애면 작성일 순서대로 표시.

    def __str__(self):
        return '{} :: {}'.format(self.vacation_type, self.author) # 제목 미리보기 형식

    def get_absolute_url(self): # admin 페이지의 VIEW ON SITE 정의
        return '/vacation/{}/'.format(self.pk)
    
    def get_update_url(self):
        return self.get_absolute_url() + 'update/'

    def get_markdown_content(self): # 드래그엔 드롭으로 사진넣은거 보여주기 위해 html로 넘겨줄거임.
        return markdown(self.content)