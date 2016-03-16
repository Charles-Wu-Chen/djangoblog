from django.shortcuts import render, get_object_or_404
from .models import ZhihuUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SearchUserForm
# Create your views here.

def zhihuuser_list (request):
    allUsers = ZhihuUser.objects.all()
    paginator = Paginator(allUsers, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        zUsers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        zUsers = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        zUsers = paginator.page(paginator.num_pages)

    return render (request, 'web/user/list.html', {'page': page, 'users': zUsers})

def user_search(request):
    user = None
    if request.method == 'POST':
        form = SearchUserForm(request.POST )
        if form.is_valid():
            cd = form.cleaned_data
            user = get_object_or_404(ZhihuUser, userLinkId=cd['userlink'])
    else:
        form = SearchUserForm()
    return render(request, 'web/user/search.html', {'user':user,
                                                    'form':form})
