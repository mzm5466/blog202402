from django.db import models
from django.utils.timezone import now


class UserInfo(models.Model):
    headurl = models.CharField(max_length=255, null=True, blank=True)
    level = models.IntegerField(default=0)
    is_vip = models.IntegerField(default=0)  # 0 notvip #1is vip
    author = models.CharField(max_length=20, null=True, blank=True)
    nickname = models.CharField(max_length=255, null=True, blank=True)
    sign = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    is_talk = models.BooleanField(default=True,verbose_name='是否允许评论')
    def __str__(self):
        if self.username:
            return self.username
        else:
            return ''
class Banner(models.Model):
    banner = models.ImageField(verbose_name='banner', upload_to='banner/', default=None)


# Create your models here.
class Posts(models.Model):
    postId = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('UserInfo', null=True, blank=True, on_delete=models.CASCADE)
    author = models.CharField(max_length=20, null=True, blank=True)
    publish_date = models.DateTimeField(default=now)
    likes = models.IntegerField(null=True)
    types = models.CharField(max_length=50, null=True)  # 论坛分类
    post_title = models.CharField(max_length=50, null=True, blank=True)
    shared = models.BooleanField(default=False)
    top = models.BooleanField(default=False)
    view = models.IntegerField(default=0)
    newer_post = models.IntegerField(null=True)
    jinghua = models.IntegerField(null=True)
    content = models.TextField()
    likes = models.PositiveIntegerField("喜欢", default=0, editable=False)
    zhiding = models.BooleanField("置顶", default=False, editable=False)
    continent = models.ForeignKey('Continent', on_delete=models.CASCADE,null='')
    country = models.ForeignKey('Country', on_delete=models.CASCADE,null='')
    location = models.ForeignKey('Location', on_delete=models.CASCADE,null='')
    is_publish = models.IntegerField(verbose_name='是否草稿',default=1)
    pic = models.CharField(null=True,max_length=255)
    def __str__(self):
        if str(self.postId):
            return str(self.postId)
        else:
            return None

# class Comment(models.Model):
#     post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
#     user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
#     content = models.TextField(null=True)
#     comment_date = models.DateTimeField(default=now)
#     is_read = models.IntegerField(default=0)

# class ReComment(models.Model):
#     post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
#     user_id_re = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
#     comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
#     content = models.TextField(null=True)
#     comment_date = models.DateTimeField(default=now)
#     is_read = models.IntegerField(default=0)

class Comment(models.Model):  
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)  
    content = models.TextField(max_length=500)  
    post = models.ForeignKey('Posts', on_delete=models.CASCADE, related_name='comments')  # 假设你有一个帖子模型  
    created_at = models.DateTimeField(auto_now_add=True)  
      
    def __str__(self):  
        return f'Comment by {self.user.username}: {self.content[:50]}...'  
  
class Reply(models.Model):  
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)  
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')  
    content = models.TextField(max_length=500)  
    created_at = models.DateTimeField(auto_now_add=True)  
      
    def __str__(self):  
        return f'Reply by {self.user.username} to {self.comment}: {self.content[:50]}...'


class Posts_kind(models.Model):
    types = models.CharField(max_length=50, null=True)  # 论坛分类

    def __str__(self):
        return self.types


# 问题反馈接口
class Feedback(models.Model):
    question = models.CharField(max_length=255, null=True)  # 论坛分类
    created = models.DateTimeField(default=now)

    def __str__(self):
        return self.question


# 喜欢数
class LikeNum(models.Model):
    user = models.ForeignKey(UserInfo, null=True, on_delete=models.SET_NULL)
    discussion = models.ForeignKey('Posts', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'user'


class Continent(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)
    pic = models.ImageField(verbose_name='country_pic', upload_to='country_pic/', default=None)
    info = models.TextField(null=True)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name