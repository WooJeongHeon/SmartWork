from django.contrib import admin
from .models import MsgBoards, UrlCostum


class MsgBoardsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}




admin.site.register(MsgBoards) # admin site에 객체 MsgBoards 등록
admin.site.register(UrlCostum) # admin site에 객체 UrlCostum 등록
