from django.shortcuts import render


def ListView(request):
    return render(request, 'user_basket/basket-page.html',)
