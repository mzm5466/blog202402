from django.contrib import admin
from api.models import *
# Register your models here.
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display=('id', 'level', 'is_vip', 'author','nickname','sign','city','username','is_talk')
    list_per_page = 50
    list_editable = ['is_talk']
    search_fields = ['username']
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-id',)

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display=('postId', 'user_id', 'publish_date', 'post_title','shared','top','view','content')
    list_per_page = 50
    search_fields = ['post_title']
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-postId',)


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('post_id', 'user_id', 'content', 'comment_date')
#     list_per_page = 50
#     # ordering设置默认排序字段，负号表示降序排序
#     search_fields = ['content']
#     ordering = ('-id',)

@admin.register(Posts_kind)
class Posts_kindAdmin(admin.ModelAdmin):
    list_display = ('types',)
    list_per_page = 50
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-id',)
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    ordering = ('-id',)
# @admin.register(ReComment)
# class ReCommentAdmin(admin.ModelAdmin):
#     list_display = ('post_id', 'user_id_re', 'content', 'comment_date')
#     list_per_page = 50
#     # ordering设置默认排序字段，负号表示降序排序
#     search_fields = ['content']
#     ordering = ('-id',)


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'continent')
    search_fields = ['name']
    list_filter = ('continent',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ['name']
    list_filter = ('country',)
