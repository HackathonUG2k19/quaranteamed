from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from .models import Article,Comment,Like,Bid
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.models import Notif
from django.contrib.auth.models import User
from random import random
# Create your views here.

def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
    articles = Article.objects.all()
    for article in articles:
        article.joined = False
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        bids = user.bid_set.all()
        print(bids)
        for bid in bids:
            for article in articles:
                if article.id == bid.article.id:
                    article.joined = True 
    return render(request,"articles.html",{"articles":articles})
def index(request):
    return render(request,"index.html")
    
def about(request):
    return render(request,"about.html")
@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)
def typeview(request, art_type):
    articles = Article.objects.filter(article_type=art_type)
    context = {
        "articles":articles, "article_type":art_type
    }
    return render(request,"lostboard.html",context)
@login_required(login_url = "user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"Post added successfully")
        return redirect("article:dashboard")
    return render(request,"addarticle.html",{"form":form})
def detail(request,id):
    #article = Article.objects.filter(id = id).first()   
    article = get_object_or_404(Article,id = id)

    comments = article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})
@login_required(login_url = "user:login")
def updateArticle(request,id):

    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"Post updated successfully")
        return redirect("article:dashboard")


    return render(request,"update.html",{"form":form})
@login_required(login_url = "user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)
    if article.article_type == "give" or article.article_type == "give_away":
        # Add notification feature
        article.delete()
        messages.success(request, "Winner selected.. Yay!")
    else:
        article.delete()
        messages.success(request,"Post deleted successfully")

    return redirect("article:dashboard")
def addComment(request,id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        # comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = request.user, comment_content = comment_content)

        newComment.article = article

        newComment.save()
        n = Notif(user_sender=request.user,user_reciever=article.author,statement=f' commented on the post {article.title} of ')
        n.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))

@login_required(login_url="user:login")
def join_giveaway(request):
    article_id = request.GET['article_id']
    user_id = request.GET['user_id']
    article = get_object_or_404(Article, id=article_id)
    user = get_object_or_404(User,id= user_id)
    bid=Bid(user=user,article=article)
    bid.save()
    if( article.winner != -1):
        rand = random()
        if rand>0.26:
            article.winner = user_id
    else:
        article.winner=user_id
    print(article.winner)
    return HttpResponse('nothing')

@login_required
def like(request):
    if request.method=='GET':
        post_id = request.GET['post_id']
        likedpost = Article.objects.get(id=post_id)
        print(Like.objects.filter(article=likedpost,user=request.user).count())
        if  Like.objects.filter(article=likedpost,user=request.user).count()==1:
            Like.objects.filter(article=likedpost,user=request.user).delete()
            n = Notif(user_sender=request.user,user_reciever=likedpost.author,statement=f' liked the post {likedpost.title} of ')
            n.save()
            return HttpResponse(likedpost.like_set.count())
        else:
            m=Like(user=request.user,article=likedpost)
            m.save()
            return HttpResponse(likedpost.like_set.count())

    else:
        return HttpResponse('failed')
@login_required
def liked(request):
    if request.method=='GET':
        post_id = request.GET['post_id']
        likedpost = Article.objects.get(id=post_id)
        c  = Like.objects.filter(user=request.user,article=likedpost).count()
        if  c==1:
            return HttpResponse(1)
        else:
            return HttpResponse(0)

    else:
        return HttpResponse('failed')
