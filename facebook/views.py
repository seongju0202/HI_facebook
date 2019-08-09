from django.shortcuts import render
from django.shortcuts import render, redirect
from facebook.models import Comment

from facebook.models import Article
from facebook.models import Page

def newsfeed(request):
    articles = Article.objects.all()

    return render(request, 'newsfeed.html', { 'articles': articles })
# Create your views here.

def play(request):
    return render(request, 'play.html')


count = 0


def play2(request):
    choidogeun = '최도근'
    age = 20

    global count  # 바깥영역의 변수를 사용할 때 global
    count = count + 1  # 접속할 때마다 방문자 1 증가

    if age > 19:  # age가 19 보다 크면?
        status = '성인'
    else:  # 성인이 아닌 경우
        status = '청소년'

    diary = ['오늘은 날씨가 맑았다. - 4월 3일', '미세머지가 너무 심하다. (4월 2일)', '비가 온다. 4월 1일에 작성']
    return render(request, 'play2.html', {'name': choidogeun, 'diary': diary, 'cnt': count, 'age': status})

def my_profile(request):
    return render(request, 'profile.html')

def event(request):
    choidogeun = '최도근'
    age = 20

    global count # 바깥영역의 변수를 사용할 때 global
    count = count + 1 # 접속할 때마다 방문자 1 증가

    if age > 19: # age가 19 보다 크면?
        status = '성인'
    else: # 성인이 아닌 경우
        status = '청소년'

    if count is 7:
        lottery = '당첨!'
    else:
        lottery = '꽝...'

    return render(request, 'event.html', { 'name': choidogeun, 'cnt': count, 'age': status, 'lottery': lottery })

def fail(request):
    return render(request, 'fail.html')

def help(request):
    return render(request, 'help.html')

def warn(request):
    return render(request, 'warn.html')

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':  # new comment
        Comment.objects.create(
            article=article,
            author=request.POST['nickname'],
            text=request.POST['reply'],
            password=request.POST['password']
        )

        return redirect(f'/feed/{ article.pk }')

    return render(request, 'detail_feed.html', {'feed': article})

def pages(request):
    pages = Page.objects.all()
    return render(request, 'page_list.html', {'pages': pages })

def new_feed(request):
    if request.method == 'POST': # 폼이 전송되었을 때만 아래 코드를 실행
        if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['content'] != '' and request.POST['password'] != '':
            text = request.POST['content']
            text = text + ' - 추신: 감사합니다.'

            new_article = Article.objects.create(
                author=request.POST['author'],
                title=request.POST['title'],
                text=text,
                password=request.POST['password']
            )

            # 새글 등록 끝
            return redirect(f'/feed/{ new_article.pk }')

    return render(request, 'new_feed.html')

def remove_feed(request, pk):
    page = Page.objects.get(pk=pk)

    if request.method == 'POST':
        page.delete()
        return redirect('/pages/')

    return render(request, 'remove_page.html', {'page': page})

def edit_feed(request, pk):
    page = Page.objects.get(pk=pk)

    if request.method == 'POST':
        page.master = request.POST['master']
        page.name = request.POST['name']
        page.text = request.POST['text']
        page.category = request.POST['category']
        page.save()
        return redirect('/pages/')

    return render(request, 'edit_page.html', {'page': page })

def new_page(request):
    if request.method == 'POST': # 폼이 전송되었을 때만 아래 코드를 실행
        new_page = Page.objects.create(
            master=request.POST['master'],
            name=request.POST['name'],
            text=request.POST['text'],
            category=request.POST['category']
        )

        # 새 페이지 개설 완료
        return redirect('/pages/')

    return render(request, 'new_page.html')