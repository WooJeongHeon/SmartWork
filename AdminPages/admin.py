from django.contrib import admin
from .models import MsgBoards


class MsgBoardsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}




admin.site.register(MsgBoards) # admin site에 객체 MsgBoards 등록
