from django.contrib import admin
from django.urls import path
from . import views
app_name = "article"

urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('lost/',views.lostboard,name = "lostboard"),
    path('found/',views.foundboard,name = "foundboard"),
    path('req/',views.reqboard,name = "reqboard"),
    path('give/',views.giveboard,name = "giveboard"),
    path('sell/',views.sellboard,name = "sellboard"),
    path('addarticle/',views.addArticle,name = "addarticle"),
    path('article/<int:id>',views.detail,name = "detail"),
    path('update/<int:id>',views.updateArticle,name = "update"),
    path('delete/<int:id>',views.deleteArticle,name = "delete"),
    path('',views.articles,name = "articles"),
    path('comment/<int:id>',views.addComment,name = "comment"),
    
]
