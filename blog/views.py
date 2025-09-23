from django.shortcuts import render
from .models import Post, Tag, Comment,Category
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from django.db.models import Q

# Create your views here.


#POSt LIST
#Category , Tag, Search 

def post_list(request):
    categoryQ = request.GET.get('category')
    tagQ = request.GET.get('tag')
    searchQ = request.GET.get('search')
    
    posts = Post.objects.all()
    
    if categoryQ:
        posts = posts.filter(category__name = categoryQ) 
    if  tagQ:
        posts = posts.filter(tag__name = tagQ)
    if searchQ :
        posts = posts.filter(
            Q(title__icontains = searchQ) |
            Q(content__icontains = searchQ) |
            Q(category__name__icontains = searchQ) |
            Q(tag_name_icontains = searchQ)
        ).distinct()
        
    paginator = Paginator(posts,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj' : page_obj,
        'categories':Category.objects.all(),
        'tags':Tag.objects.all(),
        'search_query': searchQ,
        'category_query':categoryQ,
        'tag_query': tagQ
        
    }
    
    return render(request,'blog_posts.html',context)