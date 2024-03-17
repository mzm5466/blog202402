"""luntan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from api.views import *
from django.urls import path

urlpatterns = [
    path('register/', register),  # 注册接口
    path('login/', login),  # 登录接口
    path('listposts/', listposts2),  # 帖子列表
    path('posts_detail/', posts_detail),  # 查询帖子详情
    path('createposts/', createposts),  # 新建帖子
    path('editposts/', editposts),  # 修改帖子
    path('delposts/', delposts),  # 删除帖子
    path('update_post/', update_post),  # 发布帖子更新状态
    path('personal_center/', personal_center),  # 个人中信心查询
    path('update_usercenter_heading/', update_usercenter_heading),  # 个人中心更换头像
    path('personal_center_update/', personal_center_update),  # 个人中信心修改
    path('user_post_history/', user_post_history),  # 用户发过的帖子
    path('user_post_likes/', user_post_likes),  # 用户获得的点赞数
    path('comment_api/', comment_api),  # 发表评论api
    path('comment_query/', comment_query),  # 查询指定帖子评论
    path('re_password/', re_password),  # 重置密码
    path('post_kinds/', post_kinds),  # 提交类型
    path('upload_pic/', upload_pic),  # 图片上传
    path('listposts_more/', listposts_more),  # 更多分类帖子
    path('find_password/', find_password),  # 找回密码邮箱
    path('reset_password/', reset_password),  # 重置密码根据邮箱
    path('addLikes/', addLikes),  #喜欢
    path('feedback/', feedback),  # 问题反馈
    path('liuyan_count/', liuyan_count),  # 留言数量统计
    path('liuyan_list/', liuyan_list),  # 留言列表（未读）
    path('is_read_status/', is_read_status),  # 阅读状态更新
    path('read_liuyan/', read_liuyan),  # 阅读指定文章的留言
    path('comment_api_re/', comment_api_re),  # 回复二级
    path('my_posts_history/', my_posts_history),  # 查看个人发帖历史
    path('my_comments_history/', my_comments_history),  # 查看个人回复历史
    path('del_all_posts/', del_all_posts),  # 删除全部某人帖子
    path('get_continent/', get_continent, name='get_continent'),#获取大洲
    path('get_countries/', get_countries, name='get_countries'),#获取国家
    path('get_locations/', get_locations, name='get_locations'),#获取地址
    path('search_posts/', search_posts, name='search_posts'),#模糊查询帖子
    path('post_list/', post_list, name='post_list'),#模糊查询帖子排序
    path('continent_countries/', continent_countries, name='continent_countries'),#字典
    path('country_list/', country_list, name='country_list'),#国家列表
    path('get_drafts/', get_drafts, name='get_drafts'),#查看我的草稿

    # 创建评论的URL  
    path('posts/<int:post_id>/comments/', create_comment, name='create_comment'),  
      
    # 创建回复的URL  
    path('comments/<int:comment_id>/replies/', create_reply, name='create_reply'),  
      
    # 获取评论和回复的URL  
    path('posts/<int:post_id>/comments-and-replies/', get_comments_and_replies, name='get_comments_and_replies'),  
    path('get_country/', get_country, name='get_country'),#获取国家详情


]

