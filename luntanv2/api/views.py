from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from api.models import *
import json
from copy import deepcopy
from api.jwt_auth import create_token, parse_payload
from django.db.models import Q
from django.db.models.functions import Lower

# 注册接口
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if UserInfo.objects.filter(username=username):
            return JsonResponse({'msg': 'register user is having', 'code': 204})
        UserInfo.objects.create(username=username, password=password).save()
        return JsonResponse({'msg': 'register successfully', 'code': 200})


# 登录接口
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if UserInfo.objects.filter(username=username, password=password):
            user_id = UserInfo.objects.filter(username=username, password=password).last().id
            info = UserInfo.objects.get(id=int(user_id))
            dict1 = {}
            try:
                dict1['headurl'] = UserInfo.objects.get(id=int(user_id)).headurl[1:]
            except:
                dict1['headurl'] = ''
            dict1['level'] = info.level
            dict1['is_vip'] = info.is_vip
            dict1['author'] = info.author
            dict1['username'] = info.username
            dict1['city'] = info.city
            dict1['sign'] = info.sign
            dict1['nickname'] = info.nickname
            token = create_token(payload={'user_id': user_id}, timeout=60 * 60 * 24 * 365)

            return JsonResponse({'msg': 'login success', 'info': dict1, 'data': token, 'code': 200})
        else:
            return JsonResponse({'msg': 'login failed', 'info': '', 'data': '', 'code': 204})


# 重置接口
def re_password(request):
    if request.method == 'POST':
        try:
            user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
        except Exception as e:
            return JsonResponse({'data': 'token error', 'code': 208})

        try:
            result_get = json.loads(request.body)
        except:
            result_get = request.POST
        systemDict = {}
        for key in result_get:
            systemDict[key] = result_get.get(key)
        print(systemDict)
        if systemDict.get('old_password') == UserInfo.objects.get(id=user_id).password:
            new_password = systemDict.get('new_password')
            UserInfo.objects.filter(id=user_id).update(password=new_password)
            return JsonResponse({'msg': 'repass success', 'code': 200})
        else:
            return JsonResponse({'msg': 'old_password error', 'code': 204})
# 帖子一键删除
def del_all_posts(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        return JsonResponse({'data': 'token error', 'code': 208})
    Posts.objects.filter(user_id_id=user_id).delete()
    return JsonResponse({'msg': 'del all success', 'code': 200})
# 帖子列表
def listposts(request):
    # try:
    #     user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    # except Exception as e:
    #     return JsonResponse({'data': 'token error', 'code': 208})
    try:
        result_post = json.loads(request.body)
    except:
        result_post = request.POST
    systemDict = {}
    for key in result_post:
        systemDict[key] = result_post.get(key)
    print(systemDict)
    results = Posts.objects.filter(is_publish=1).all().order_by('-postId')
    paginator = Paginator(results, 20)
    total_page = paginator.num_pages
    total = results.count()
    results = paginator.page(int(request.GET.get('currentPage',1)))
    try:
        banner = Banner.objects.all().last().banner.url
    except:
        banner = ''
    if results:
        res = []
        for i in results:
            dict1 = model_to_dict(i)
            try:
                user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
                self_like_num = LikeNum.objects.filter(discussion_id=dict1['postId'], user_id=user_id).count()
                dict1['self_like_num'] = self_like_num
            except Exception as e:
                pass
            like_num = LikeNum.objects.filter(discussion_id=dict1['postId']).count()
            dict1['like_num'] = like_num
            try:
                dict1['headurl'] = i.user_id.headurl[1:]
            except:
                dict1['headurl'] = ''
            dict1['comment_count'] = Comment.objects.filter(post_id_id=dict1['postId']).count()
            res.append(dict1)
        return JsonResponse({'code': 200, 'data': res, 'total_page': total_page, 'total': total,
                             'currentPage': int(request.GET.get('currentPage',1)), 'banner': banner})
    else:
        return JsonResponse(
            {'code': 204, 'data': '', 'total_page': total_page, 'total': total,
             'currentPage': int(request.GET.get('currentPage',1)), 'banner': banner})
# 帖子列表2
def listposts2(request):
    # try:
    #     user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    # except Exception as e:
    #     return JsonResponse({'data': 'token error', 'code': 208})
    try:
        result_post = json.loads(request.body)
    except:
        result_post = request.POST
    systemDict = {}
    for key in result_post:
        systemDict[key] = result_post.get(key)
    print(systemDict)
    results = Posts.objects.filter(is_publish=1).all().order_by('-postId')
    paginator = Paginator(results, 20)
    total_page = paginator.num_pages
    total = results.count()
    results = paginator.page(int(request.GET.get('currentPage',1)))
    try:
        banner = Banner.objects.all().last().banner.url
    except:
        banner = ''
    if results:
        res = []
        for i in results:
            dict1 = model_to_dict(i)
            try:
                user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
                self_like_num = LikeNum.objects.filter(discussion_id=dict1['postId'], user_id=user_id).count()
                dict1['self_like_num'] = self_like_num
            except Exception as e:
                pass
            like_num = LikeNum.objects.filter(discussion_id=dict1['postId']).count()
            dict1['like_num'] = like_num
            try:
                dict1['headurl'] = i.user_id.headurl[1:]
            except:
                dict1['headurl'] = ''
            dict1['comment_count'] = Comment.objects.filter(post_id=dict1['postId']).count()
            res.append(dict1)
        return JsonResponse({'code': 200, 'data': res, 'total_page': total_page, 'total': total,
                             'currentPage': int(request.GET.get('currentPage',1)), 'banner': banner})
    else:
        return JsonResponse(
            {'code': 204, 'data': '', 'total_page': total_page, 'total': total,
             'currentPage': int(request.GET.get('currentPage',1)), 'banner': banner})


# 帖子列表
def listposts_more(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        pass
    try:
        result_post = json.loads(request.body)
    except:
        result_post = request.GET
    systemDict = {}
    for key in result_post:
        systemDict[key] = result_post.get(key)
    print(systemDict)
    results = Posts.objects.filter(types=systemDict.get('types')).order_by('-postId')
    paginator = Paginator(results, 20)
    total_page = paginator.num_pages
    total = results.count()
    results = paginator.page(int(systemDict['currentPage']))
    if results:
        res = []
        for i in results:
            dict1 = model_to_dict(i)
            like_num = LikeNum.objects.filter(discussion_id=dict1['postId']).count()
            try:
                user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
                self_like_num = LikeNum.objects.filter(discussion_id=dict1['postId'], user_id=user_id).count()
                dict1['self_like_num'] = self_like_num
            except Exception as e:
                pass

            dict1['like_num'] = like_num
            try:
                dict1['headurl'] = i.user_id.headurl[1:]
            except:
                dict1['headurl'] = ''
            dict1['comment_count'] = Comment.objects.filter(post_id_id=dict1['postId']).count()
            res.append(dict1)
        return JsonResponse({'code': 200, 'data': res, 'total_page': total_page, 'total': total,
                             'currentPage': systemDict['currentPage']})
    else:
        return JsonResponse(
            {'code': 204, 'data': '', 'total_page': total_page, 'total': total,
             'currentPage': systemDict['currentPage']})


# 查询帖子详情
def posts_detail(request):
    # try:
    #     user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    # except Exception as e:
    #     user_id = ''
        # return JsonResponse({'data': 'token error', 'code': 208})
    try:
        result_post = json.loads(request.body)
    except:
        result_post = request.POST
    systemDict = {}
    for key in result_post:
        systemDict[key] = result_post.get(key)
    res = model_to_dict(Posts.objects.get(postId=int(request.GET['postId'])))
    # if res['user_id'] != user_id:
    #     btn_hide = 0
    # else:
    #     btn_hide = 1
    try:
        res['headurl'] = UserInfo.objects.get(id=int(res['user_id'])).headurl[1:]
    except:
        res['headurl'] = ''
    # res['btn_hide'] = btn_hide
    Posts.objects.filter(postId=int(request.GET['postId'])).update(
        view=Posts.objects.get(postId=int(request.GET['postId'])).view + 1)
    return JsonResponse({'code': 200, 'data': res})


# 新建帖子
def createposts(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        return JsonResponse({'data': 'token error', 'code': 208})
    try:
        result_post = json.loads(request.body)
    except:
        result_post = request.POST
    systemDict = {}
    for key in result_post:
        systemDict[key] = result_post.get(key)
    # systemDict['continent'] = Continent.objects.get(id=systemDict['continent']).id
    # systemDict['country'] = Country.objects.get(id=systemDict['country']).id
    if not Location.objects.filter(country_id=Country.objects.get(id=systemDict['country']).id,name=systemDict['location']):
        Location.objects.create(country_id=Country.objects.get(id=systemDict['country']).id,name=systemDict['location'])
    # systemDict['location'] = Location.objects.filter(country=Country.objects.get(id=systemDict['country']),name=systemDict['location']).last().id
    from copy import deepcopy
    systemdict = deepcopy(systemDict)
    del systemdict['continent']
    del systemdict['country']
    del systemdict['location']
    if systemDict['is_publish']:
        systemDict['is_publish']=1

        Posts.objects.create(user_id_id=user_id,continent_id=Continent.objects.get(id=systemDict['continent']).id,country_id=Country.objects.get(id=systemDict['country']).id ,location_id=Location.objects.get(name=systemDict['location']).id,**systemdict).save()
        return JsonResponse({'code': 200, 'data': '帖子创建成功！'})
    else:
        systemDict['is_publish']=0
        Posts.objects.create(user_id_id=user_id,continent_id=Continent.objects.get(id=systemDict['continent']).id,country_id=Country.objects.get(id=systemDict['country']).id ,location_id=Location.objects.get(name=systemDict['location']).id,**systemdict).save()
        return JsonResponse({'code': 200, 'data': '帖子草稿创建成功！'})

# 修改帖子
def editposts(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        return JsonResponse({'data': 'token error', 'code': 208})
    try:
        result_post = json.loads(request.body)
    except:
        result_post = request.POST
    systemDict = {}
    for key in result_post:
        systemDict[key] = result_post.get(key)
    if Posts.objects.get(postId=int(systemDict['postId'])).user_id.id != user_id:
        return JsonResponse({'code': 204, 'data': '你无权修改此贴！'})

    if not Location.objects.filter(country_id=Country.objects.get(id=systemDict['country']).id,name=systemDict['location']):
        Location.objects.create(country_id=Country.objects.get(id=systemDict['country']).id,name=systemDict['location'])   
    location_id=Location.objects.get(name=systemDict['location'])
    del systemDict['location']
    Posts.objects.filter(postId=int(systemDict['postId'])).update(location_id=location_id,**systemDict)
    return JsonResponse({'code': 200, 'data': '帖子修改成功！'})
0

# 删除帖子
def delposts(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        return JsonResponse({'data': 'token error', 'code': 208})
    try:
        result_post = json.loads(request.body)
    except:
        result_post = request.POST
    systemDict = {}
    for key in result_post:
        systemDict[key] = result_post.get(key)
    if Posts.objects.get(postId=int(systemDict['postId'])).user_id.id != user_id:
        return JsonResponse({'code': 204, 'data': '你无权删除此贴！'})
    Posts.objects.filter(postId=int(systemDict['postId'])).delete()
    return JsonResponse({'code': 200, 'data': '帖子删除成功！'})


# 个人中信心查询
def personal_center(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        return JsonResponse({'data': 'token error', 'code': 208})
    info = UserInfo.objects.get(id=int(user_id))
    dict1 = {}
    try:
        dict1['headurl'] = info.headurl[1:]
    except:
        dict1['headurl'] = ''
    dict1['level'] = info.level
    dict1['is_vip'] = info.is_vip
    dict1['author'] = info.author
    dict1['username'] = info.username
    dict1['nickname'] = info.nickname
    return JsonResponse({'code': 200, 'data': dict1})


# 个人中心更换头像
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def update_usercenter_heading(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        print(e)
        return JsonResponse({'data': 'token error', 'code': 208})
    files = request.FILES.get('file', None)
    pic_name = os.path.join(BASE_DIR, 'static/media', 'app')  # 将设置的上传文件保存位置路径和文件名拼接起来。获取文件保存的完整路径
    if not os.path.exists(os.path.join(pic_name, str(user_id))):
        os.mkdir(os.path.join(pic_name, str(user_id)))

    test_path = (os.path.join(pic_name, str(user_id), files.name)).replace('\\',
                                                                           '/')  # 由于是在windows系统下，将文件路径中的“/”转换为“\”。
    with open(test_path, 'wb+') as wdc:
        for i in files.chunks():  # 分块写入文件
            wdc.write(i)
        UserInfo.objects.filter(id=user_id).update(headurl='/static/media/app/' + str(user_id) + '/' + files.name)
    try:
        headurl = UserInfo.objects.get(id=int(user_id)).headurl
    except Exception as e:
        print(e)
        return JsonResponse({'code': 204, 'data': '用户头像更新失败', 'headurl': 'no info'})

    return JsonResponse({'code': 200, 'data': '用户头像更新成功', 'headurl': headurl[1:]})


# 个人中信心修改
def personal_center_update(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        return JsonResponse({'data': 'token error', 'code': 208})
    try:
        result_post = json.loads(request.body)
    except:
        result_post = request.POST
    systemDict = {}
    for key in result_post:
        systemDict[key] = result_post.get(key)
    UserInfo.objects.filter(id=int(user_id)).update(**systemDict)
    try:
        headurl = UserInfo.objects.get(id=int(user_id)).headurl
        systemDict['headurl'] = headurl[1:]
    except:
        systemDict['headurl'] = ''
    return JsonResponse({'code': 200, 'data': systemDict, 'msg': '个人信息修改成功'})


# 用户发过的帖子
def user_post_history(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        return JsonResponse({'data': 'token error', 'code': 208})
    try:
        result_post = json.loads(request.body)
    except:
        result_post = request.POST
    systemDict = {}
    for key in result_post:
        systemDict[key] = result_post.get(key)
    results = Posts.objects.filter(user_id_id=int(user_id)).order_by('-postId')
    paginator = Paginator(results, 20)
    total_page = paginator.num_pages
    total = results.count()
    results = paginator.page(int(request.GET['currentPage']))
    if results:
        res = []
        for i in results:
            dict1 = model_to_dict(i)
            try:
                dict1['headurl'] = i.user_id.headurl[1:]
            except:
                dict1['headurl'] = ''
            dict1['comment_count'] = Comment.objects.filter(user_id=i.user_id).count()
            res.append(dict1)
        return JsonResponse({'code': 200, 'data': res, 'total_page': total_page, 'total': total,
                             'currentPage': request.GET['currentPage']})
    else:
        return JsonResponse(
            {'code': 204, 'data': '', 'total_page': total_page, 'total': total,
             'currentPage': request.GET['currentPage']})


# 用户获得的点赞数
def user_post_likes(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        return JsonResponse({'data': 'token error', 'code': 208})
    counts = Posts.objects.filter(user_id_id=user_id, likes=1).count()
    return JsonResponse({'code': 200, 'data': counts})


# 发表评论api
def comment_api(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        return JsonResponse({'data': 'token error', 'code': 208})
    if not UserInfo.objects.get(id=user_id).is_talk:
        return JsonResponse({'data': '您已经被禁言！', 'code': 208})
    try:
        result_post = json.loads(request.body)
    except:
        result_post = request.POST
    systemDict = {}
    for key in result_post:
        systemDict[key] = result_post.get(key)

    Comment.objects.create(user_id_id=user_id, post_id_id=systemDict.get('post_id'),
                           content=systemDict.get('content')).save()
    return JsonResponse({'code': 200, 'data': '评论成功'})


# 查询指定帖子评论
def comment_query(request):
    try:
        result_post = json.loads(request.body)
    except:
        result_post = request.POST
    systemDict = {}
    for key in result_post:
        systemDict[key] = result_post.get(key)
    list_all = []
    for i in Comment.objects.filter(post_id_id=systemDict.get('post_id')):
        dict1 = {}
        try:
            dict1['headurl'] = i.user_id.headurl[1:]
        except:
            dict1['headurl'] = ''
        dict1['level'] = i.user_id.level
        dict1['is_vip'] = i.user_id.is_vip
        dict1['author'] = i.user_id.author
        dict1['username'] = i.user_id.username
        dict1['content'] = i.content
        dict1['comment_date'] = i.comment_date
        dict1['nickname'] = i.user_id.nickname

        c2 = ReComment.objects.get(post_id_id=systemDict.get('post_id'),
                                   comment_id_id=i.id)
        dict1['comment_user_re'] = c2.user_id.username  # 用户名
        dict1['comment_post_re'] = c2.post_id.post_title  # 文章标题
        dict1['comment_post_id_re'] = c2.post_id.postId  # 文章id
        dict1['comment_id_re'] = c2.id  # 评论id
        dict1['comment_content_re'] = c2.content  # 评论内容
        dict1['comment_date_re'] = c2.comment_date  # 评论时间
        dict1['is_read'] = c2.is_read  # 评论时间
        list_all.append(dict1)
    # result = [model_to_dict(i) for i in Comment.objects.filter(post_id_id=systemDict.get('post_id'))]
    return JsonResponse({'code': 200, 'data': list_all})


def post_kinds(request):
    dict1 = [model_to_dict(i) for i in Posts_kind.objects.all()]
    return JsonResponse({'code': 200, 'data': dict1})


def upload_pic(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        print(e)
        return JsonResponse({'data': 'token error', 'code': 208})
    files = request.FILES.get('file', None)
    # if files.size>200*1024:
    #    return JsonResponse({'code': 204, 'data': '用户图片上传失败，必须小于200KB'})
    pic_name = os.path.join(BASE_DIR, 'static/media', 'pic')  # 将设置的上传文件保存位置路径和文件名拼接起来。获取文件保存的完整路径
    if not os.path.exists(pic_name):
        os.mkdir(pic_name)

    test_path = (os.path.join(pic_name, files.name)).replace('\\', '/')  # 由于是在windows系统下，将文件路径中的“/”转换为“\”。
    with open(test_path, 'wb+') as wdc:
        for i in files.chunks():  # 分块写入文件
            wdc.write(i)
    return JsonResponse({'code': 200, 'data': '用户图片上传成功', 'pic': 'static/media/pic/' + files.name})


from django.core.mail import send_mail


def find_password(request):
    email = request.POST.get('email')
    if UserInfo.objects.filter(email=email):
        user_id = UserInfo.objects.filter(email=email).last().id
        token = create_token(payload={'user_id': user_id}, timeout=60 * 5)
    a = send_mail('密码找回,请点击连接', 'http://8.210.92.129:8888/?token=' + token + '', 'mzm5466@163.com',
                  [email], auth_user='mzm5466@163.com', auth_password='DFNRWBUCYZWNYTSF', fail_silently=False)
    print(a)
    return JsonResponse({'status': 200, 'message': 'success'})


def reset_password(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        return JsonResponse({'data': 'token error', 'code': 208})
    try:
        result_post = json.loads(request.body)
    except:
        result_post = request.POST
    systemDict = {}
    for key in result_post:
        systemDict[key] = result_post.get(key)
    print(systemDict)
    UserInfo.objects.filter(id=user_id).update(password=systemDict.get('password'))
    return JsonResponse({'data': '密码重置成功', 'code': 200})


# 讨论点赞
def addLikes(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        print(e)
        return JsonResponse({'data': 'token error', 'code': 208})
    try:
        result_post = json.loads(request.body)
    except:
        result_post = request.POST
    systemDict = {}
    for key in result_post:
        systemDict[key] = result_post.get(key)
    print(systemDict)
    postId = int(systemDict.get('postId'))
    print(type(postId))
    # 判别点赞的该Discussion是否存在，有可能在你点赞的时候该用户已经删除，注意不能简单的使用if，else当找不到discussion时会出错
    try:
        if Posts.objects.get(postId=postId):
            # 如果Discussion存在
            d = Posts.objects.get(postId=postId)
            # 如果User存在
            if user_id:
                # 判断当前用户是否已经给该Discussion点过赞
                # record 为该记录，不存在时则自动创建
                # flag 为当前是否操作
                record, flag = LikeNum.objects.get_or_create(user_id=user_id, discussion_id=postId)
                # 如果刚刚创建
                if flag:
                    d.likes += 1
                    d.save()
                # 如果没操作，说明之前点过赞，此时再次点赞说明是要取消点赞
                else:
                    d.likes -= 1
                    d.save()
                    # 并且删除掉点赞记录
                    LikeNum.objects.get(user_id=user_id, discussion_id=postId).delete()
                # 跳转到发布页面
            return JsonResponse(
                {'like_count': LikeNum.objects.filter(discussion_id=postId, user_id=user_id).count()})
    except Exception as e:
        import sys
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return JsonResponse({'data': 'error', 'code': 204})


def feedback(request):
    try:
        result_post = json.loads(request.body)
    except:
        result_post = request.POST
    systemDict = {}
    for key in result_post:
        systemDict[key] = result_post.get(key)
    print(systemDict)
    Feedback.objects.create(question=systemDict['question']).save()
    return JsonResponse({'data': '反馈成功', 'code': 200})


# 留言数量
def liuyan_count(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        print(e)
        return JsonResponse({'data': 'token error', 'code': 208})
    posts = Posts.objects.filter(user_id_id=user_id)
    list_all = []
    for p in posts:
        for c in Comment.objects.filter(post_id_id=p.postId, is_read=0):
            dict1 = {}
            dict1['comment_user'] = c.user_id.username  # 用户名
            dict1['comment_post'] = c.post_id.post_title  # 文章标题
            dict1['comment_post_id'] = c.post_id.postId  # 文章id
            dict1['comment_id'] = c.id  # 评论id
            dict1['comment_content'] = c.content  # 评论内容
            dict1['comment_date'] = c.comment_date  # 评论时间
            list_all.append(dict1)
    return JsonResponse({'data': list_all, 'count': len(list_all), 'code': 200})


# 留言列表
def liuyan_list(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        print(e)
        return JsonResponse({'data': 'token error', 'code': 208})
    try:
        result_post = json.loads(request.body)
    except:
        result_post = request.POST
    systemDict = {}
    for key in result_post:
        systemDict[key] = result_post.get(key)
    print(systemDict)
    posts = Posts.objects.filter(user_id_id=user_id)
    list_all = []
    for p in posts:
        for c in Comment.objects.filter(post_id_id=p.postId):
            dict1 = {}
            dict1['comment_user'] = c.user_id.username  # 用户名
            dict1['comment_post'] = c.post_id.post_title  # 文章标题
            dict1['comment_post_id'] = c.post_id.postId  # 文章id
            dict1['comment_id'] = c.id  # 评论id
            dict1['comment_content'] = c.content  # 评论内容
            dict1['comment_date'] = c.comment_date  # 评论时间
            dict1['is_read'] = c.is_read  # 评论时间
            try:

                c2 = ReComment.objects.get(post_id_id=c.post_id.postId,
                                           comment_id_id=c.id)
                dict1['comment_user_re'] = c2.user_id.username  # 用户名
                dict1['comment_post_re'] = c2.post_id.post_title  # 文章标题
                dict1['comment_post_id_re'] = c2.post_id.postId  # 文章id
                dict1['comment_id_re'] = c2.id  # 评论id
                dict1['comment_content_re'] = c2.content  # 评论内容
                dict1['comment_date_re'] = c2.comment_date  # 评论时间
                dict1['is_read'] = c2.is_read  # 评论时间
            except Exception as e:
                pass
            # Comment.objects.filter(post_id_id=p.postId, is_read=0).update(is_read=1)
            list_all.append(dict1)
    return JsonResponse({'data': list_all, 'code': 200})


def is_read_status(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        print(e)
        return JsonResponse({'data': 'token error', 'code': 208})
    try:
        result_post = json.loads(request.body)
    except:
        result_post = request.POST
    systemDict = {}
    for key in result_post:
        systemDict[key] = result_post.get(key)
    print(systemDict)
    Comment.objects.filter(post_id_id=systemDict['comment_post_id'], is_read=0, id=systemDict['comment_id']).update(
        is_read=1)
    return JsonResponse({'data': '消息已阅读', 'code': 200})


def read_liuyan(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        print(e)
        return JsonResponse({'data': 'token error', 'code': 208})
    try:
        result_post = json.loads(request.body)
    except:
        result_post = request.POST
    systemDict = {}
    for key in result_post:
        systemDict[key] = result_post.get(key)
    print(systemDict)
    res = Comment.objects.filter(post_id_id=systemDict['comment_post_id'])
    list_all = []
    for c in res:
        dict1 = {}
        dict1['comment_user'] = c.user_id.username  # 用户名
        dict1['comment_post'] = c.post_id.post_title  # 文章标题
        dict1['comment_post_id'] = c.post_id.postId  # 文章id
        dict1['comment_id'] = c.id  # 评论id
        dict1['comment_content'] = c.content  # 评论内容
        dict1['comment_date'] = c.comment_date  # 评论时间
        dict1['is_read'] = c.is_read  # 评论时间
        Comment.objects.filter(post_id_id=c.post_id.postId, is_read=0,
                               id=c.id).update(is_read=1)
        try:

            c2 = ReComment.objects.get(post_id_id=c.post_id.postId,
                                       comment_id_id=c.id)
            dict1['comment_user_re'] = c2.user_id_re.username  # 用户名
            dict1['comment_post_re'] = c2.post_id.post_title  # 文章标题
            dict1['comment_post_id_re'] = c2.post_id.postId  # 文章id
            dict1['comment_id_re'] = c2.id  # 评论id
            dict1['comment_content_re'] = c2.content  # 评论内容
            dict1['comment_date_re'] = c2.comment_date  # 评论时间
            dict1['is_read'] = c2.is_read  # 评论时间
        except Exception as e:
            print(e)
        list_all.append(dict1)
    return JsonResponse({'data': list_all, 'code': 200})


# 发表评论回复api
def comment_api_re(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        return JsonResponse({'data': 'token error', 'code': 208})
    if not UserInfo.objects.get(id=user_id).is_talk:
        return JsonResponse({'data': '您已经被禁言！', 'code': 208})
    try:
        result_post = json.loads(request.body)
    except:
        result_post = request.POST
    systemDict = {}
    for key in result_post:
        systemDict[key] = result_post.get(key)
    if not ReComment.objects.filter(post_id_id=systemDict.get('comment_post_id'),
                                    comment_id_id=systemDict.get('comment_id')):
        ReComment.objects.create(post_id_id=systemDict.get('comment_post_id'), user_id_re_id=user_id,
                                 comment_id_id=systemDict.get('comment_id'),
                                 content=systemDict.get('content')).save()
        return JsonResponse({'code': 200, 'data': '评论回复成功'})
    else:

        return JsonResponse({'code': 204, 'data': '评论回复过了'})


def my_posts_history(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        return JsonResponse({'data': 'token error', 'code': 208})
    read_posts = Posts.objects.filter(user_id_id=user_id)
    list_all = []
    for rp in read_posts:
        dict1 = {}
        dict1['postId'] = rp.postId
        dict1['title'] = rp.post_title
        list_all.append(dict1)
    return JsonResponse({'code': 200, 'data': list_all})


def my_comments_history(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        return JsonResponse({'data': 'token error', 'code': 208})
    read_comment = Comment.objects.filter(user_id_id=user_id)
    try:
        list_all = []
        for rp in read_comment:
            dict1 = {}
            dict1['postId'] = rp.post_id.postId
            dict1['content'] = rp.content
            dict1['title'] = rp.post_id.post_title
            list_all.append(dict1)
    except:
        list_all = []
    try:
        read_comment_re = ReComment.objects.filter(user_id_re_id=user_id)
        list_all2 = []
        for rp in read_comment_re:
            dict1 = {}
            dict1['postId'] = rp.post_id.postId
            dict1['content'] = rp.content
            dict1['title'] = rp.post_id.post_title
            list_all2.append(dict1)
    except:
        list_all2 = []
    return JsonResponse({'code': 200, 'data': list_all, 'data_re': list_all2})
#国家下拉一个详情
def get_country(request):
    country_id = request.GET.get('country_id')
    country = Country.objects.get(id=int(country_id))
    dict1 = model_to_dict(country,exclude=['pic'])
    dict1['pic'] = country.pic.url if country.pic else None
    # country_list = [model_to_dict(country) for country in countries]
    return JsonResponse({'country': dict1,'code':200})
#国家下拉
def get_countries(request):
    continent_id = request.GET.get('continent_id')
    countries = Country.objects.filter(continent_id=int(continent_id))
    country_data = []

    for country in countries:
        dict1 = model_to_dict(country,exclude=['pic'])
        dict1['pic'] = country.pic.url if country.pic else None
        country_data.append(dict1)
    # country_list = [model_to_dict(country) for country in countries]
    return JsonResponse({'countries': country_data,'code':200})
#地址下拉
def get_locations(request):
    country_id = request.GET.get('country_id')
    locations = Location.objects.filter(country_id=country_id)
    location_list = [model_to_dict(location) for location in locations]
    return JsonResponse({'locations': location_list,'code':200})
#大洲下拉
def get_continent(request):
    continents = [model_to_dict(continent) for continent in  Continent.objects.all()]
    return JsonResponse({'continents': continents,'code':200})
#模糊查询 

def search_posts(request):
    query = request.GET.get('query')  # 获取搜索关键字
    posts = Posts.objects.filter(
        Q(post_title__icontains=query) |  # 根据标题搜索，忽略大小写
        Q(content__icontains=query) |  # 根据内容搜索，忽略大小写
        Q(location__name__icontains=query)  # 根据地点名称搜索，忽略大小写
    )
    p = [model_to_dict(post) for post in posts]
    return JsonResponse({'p': p})

def post_list(request):
    sort_by = request.GET.get('sort_by','')  # 获取排序字段
    order_by = request.GET.get('order_by')  # 获取排序顺序（升序或降序）
    post_title = request.GET.get('post_title','')#模糊标题
    country_id = request.GET.get('country_id','')#国家id
    if sort_by:
        if country_id:
            if sort_by == 'publish_date':
                if order_by == 'desc':
                    posts = Posts.objects.filter(country_id=country_id).filter(post_title__icontains=post_title).order_by('-publish_date')
                else:
                    posts = Posts.objects.filter(country_id=country_id).filter(post_title__icontains=post_title).order_by('publish_date')
            elif sort_by == 'continent':
                if order_by == 'desc':
                    posts = Posts.objects.filter(country_id=country_id).filter(post_title__icontains=post_title).order_by(Lower('continent__name').desc())
                else:
                    posts = Posts.objects.filter(country_id=country_id).filter(post_title__icontains=post_title).order_by(Lower('continent__name'))
            elif sort_by == 'country':
                if order_by == 'desc':
                    posts = Posts.objects.filter(country_id=country_id).filter(post_title__icontains=post_title).order_by(Lower('country__name').desc())
                else:
                    posts = Posts.objects.filter(country_id=country_id).filter(post_title__icontains=post_title).order_by(Lower('country__name'))
            elif sort_by == 'location':
                if order_by == 'desc':
                    posts = Posts.objects.filter(country_id=country_id).filter(post_title__icontains=post_title).order_by(Lower('location__name').desc())
                else:
                    posts = Posts.objects.filter(country_id=country_id).filter(post_title__icontains=post_title).order_by(Lower('location__name'))
            else:
                posts = Posts.objects.filter(country_id=country_id).filter(post_title__icontains=post_title).all()
        else:
            if sort_by == 'publish_date':
                if order_by == 'desc':
                    posts = Posts.objects.filter(post_title__icontains=post_title).order_by('-publish_date')
                else:
                    posts = Posts.objects.filter(post_title__icontains=post_title).order_by('publish_date')
            elif sort_by == 'continent':
                if order_by == 'desc':
                    posts = Posts.objects.filter(post_title__icontains=post_title).order_by(Lower('continent__name').desc())
                else:
                    posts = Posts.objects.filter(post_title__icontains=post_title).order_by(Lower('continent__name'))
            elif sort_by == 'country':
                if order_by == 'desc':
                    posts = Posts.objects.filter(post_title__icontains=post_title).order_by(Lower('country__name').desc())
                else:
                    posts = Posts.objects.filter(post_title__icontains=post_title).order_by(Lower('country__name'))
            elif sort_by == 'location':
                if order_by == 'desc':
                    posts = Posts.objects.filter(post_title__icontains=post_title).order_by(Lower('location__name').desc())
                else:
                    posts = Posts.objects.filter(post_title__icontains=post_title).order_by(Lower('location__name'))
            else:
                posts = Posts.objects.filter(country_id=country_id).filter(post_title__icontains=post_title).all()

    
    else:
        if country_id:
    
            if order_by == 'desc':
                posts = Posts.objects.filter(country_id=country_id).filter(post_title__icontains=post_title)
            else:
                posts = Posts.objects.filter(country_id=country_id).filter(post_title__icontains=post_title)
        else:
            
            if order_by == 'desc':
                posts = Posts.objects.filter(post_title__icontains=post_title)
            else:
                posts = Posts.objects.filter(post_title__icontains=post_title)
    paginator = Paginator(posts, int(request.GET.get('pageSIze',20)))
    total_page = paginator.num_pages
    total = posts.count()
    posts2 = paginator.page(int(request.GET.get('currentPage',1)))
    context = []
    for post in posts2:
        dict1 = model_to_dict(post)
        dict1['country_img'] = Country.objects.get(id=dict1['country']).pic.url
        dict1['country_info'] = Country.objects.get(id=dict1['country']).info
        context.append(dict1)
    return JsonResponse({'code': 200, 'data': context, 'total_page': total_page, 'total': total,
        'currentPage': int(request.GET.get('currentPage',1)),'pageSIze':request.GET.get('pageSIze',20)})

def continent_countries(request):
    continents = Continent.objects.all()
    data = []

    for continent in continents:
        countries = Country.objects.filter(continent=continent)
        country_data = []

        for country in countries:
            dict1 = model_to_dict(country,exclude=['pic'])
            dict1['pic'] = country.pic.url if country.pic else None
            country_data.append(dict1)
        #country_data = [model_to_dict(post) for post in countries]
        data.append({
            'continent_id':continent.id,
            'continent': continent.name,
            'countries':country_data
        })

    return JsonResponse({'data':data,'code':200})

def country_list(request):
    countries = Country.objects.all()
    data = []

    for country in countries:
        dict1 = model_to_dict(country,exclude=['pic'])
        dict1['pic'] = country.pic.url if country.pic else None
        data.append(dict1)

    return JsonResponse({'data':data,'code':200})

def update_post(request):
    post_id = request.POST.get('postId')
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        return JsonResponse({'data': 'token error', 'code': 208})

    try:
        post = Posts.objects.get(postId=post_id,user_id_id=user_id)
        post.is_publish = 1
        post.save()
        return JsonResponse({'data':'帖子发布成功！','code':200})
    except Posts.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Post does not exist.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})
    
def get_drafts(request):
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        return JsonResponse({'data': 'token error', 'code': 208})
    try:
        drafts = [Posts.objects.filter(user_id_id=user_id, is_publish=0).order_by('-postId')[0]]
        paginator = Paginator(drafts, 20)
        total_page = paginator.num_pages
        total = drafts.count()
        drafts = paginator.page(int(request.GET.get('currentPage',1)))
        data = []

        for draft in drafts:
            data.append({
                'postId': draft.postId,
                'author': draft.author,
                'publish_date': draft.publish_date,
                'post_title': draft.post_title,
                'content': draft.content,
            })

        # return JsonResponse({'data':data,'code':200})
        return JsonResponse(
                {'code': 200, 'data': data, 'total_page': total_page, 'total': total,
                 'currentPage': int(request.GET.get('currentPage',1))})
    except:
        return JsonResponse(
        {'code': 200, 'data': 'error'})

#多级评论  
def create_comment(request, post_id):  
    try:
        user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
    except Exception as e:
        return JsonResponse({'data': 'token error', 'code': 208})

    if request.method == 'POST':  
        content = request.POST.get('content')  
        # post = get_object_or_404(Posts, post_id=post_id)  
        comment = Comment.objects.create(user_id=user_id, content=content, post_id=post_id)
        comment.save()
        return JsonResponse({'status': 'success', 'comment_id': comment.id})  
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)  
  
def create_reply(request, comment_id):  
    if request.method == 'POST':  
        try:
            user_id = parse_payload(request.META.get('HTTP_TOKEN'))['data']['user_id']
        except Exception as e:
            return JsonResponse({'data': 'token error', 'code': 208})
        content = request.POST.get('content')  
        # comment = get_object_or_404(Comment, pk=comment_id)  
        reply = Reply.objects.create(user_id=user_id, comment_id=comment_id, content=content)  
        return JsonResponse({'status': 'success', 'reply_id': reply.id})  
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)  
  
def get_comments_and_replies(request, post_id):  
    # post = get_object_or_404(Posts, pk=post_id)  
    comments = Comment.objects.filter(post_id=post_id).order_by('-created_at')  
    comment_data = []  
      
    for comment in comments:  
        try:
            replies = Reply.objects.filter(comment_id=comment.id).order_by('-created_at')  
            reply_data = [{'content': reply.content, 'created_at': reply.created_at,'username':reply.user.username} for reply in replies]  
        except:
            reply_data = []
        comment_data.append({  
            'id': comment.id,  
            'content': comment.content,  
            'user': comment.user.username,  
            'created_at': comment.created_at,  
            'replies': reply_data  
        })  
      
    return JsonResponse({'comments': comment_data}, safe=False)
def login_html(request):
    return render(request,'qianduan/login.html')
def detail_html(request):
    return render(request,'qianduan/detail.html')
def blogDetail_html(request):
    return render(request,'qianduan/blogDetail.html')
def footer_html(request):
    return render(request,'qianduan/footer.htm')
def header_html(request):
    return render(request,'qianduan/header.htm')
def index_html(request):
    return render(request,'qianduan/index.html')
def nationDetail_html(request):
    return render(request,'qianduan/nationDetail.html')
def places_html(request):
    return render(request,'qianduan/places.html')
def pushBlog_html(request):
    return render(request,'qianduan/pushBlog.html')
def signup_html(request):
    return render(request,'qianduan/signup.html')
def user_html(request):
    return render(request,'qianduan/user.html')
def user_profile_html(request):
    return render(request,'qianduan/user_profile.html')