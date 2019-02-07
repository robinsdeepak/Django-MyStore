from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from shop.models import Shop


def ShopListView(request):
    # Need to show the nearest shop using ML
    shops = Shop.objects.all()[:50]
    return render(request, 'shop/shop_list.html', {'shops': shops})


def ShopDetailView(request, pk):
    shop = Shop.objects.get(pk=pk)
    products = shop.product_set.all()
    # shop = get_object_or_404(Shop, pk)

    context = {
        'shop': shop,
        'products': products,
    }
    return render(request, 'shop/Shop.html', context)


class AddNewShop(CreateView):
    model = Shop
    fields = ['title',
              'address_line_1',
              'address_line_2',
              'address_State',
              'location',
              'about',
              'Shop_icon', 'Shop_icon_2']

#
# def AddNewShop(request):
#     if request.method == 'GET':
#         return render(request, 'shop/addNewShop.html',)
#
#     if request.method == 'POST':
#         title = request.GET['title']
#         address_line_1 = request.GET['address_line_1']
#         address_line_2 = request.GET['address_line_2']
#         address_State = request.GET['address_State']
#         location = request.GET['location']
#         about = request.GET['about']
#         Shop_icon = request.FILES['Shop_icon']
#         Shop_icon_2 = request.FILES['Shop_icon_2']
#
#         new_shop_obj = Shop(title=title,
#                             address_line_1=address_line_1,
#                             address_line_2=address_line_2,
#                             address_State=address_State,
#                             location=location,
#                             about=about,
#                             Shop_icon=Shop_icon,
#                             Shop_icon_2=Shop_icon_2
#                             )
#         new_shop_obj.save()


def ShopDetailContextView(request, pk):
    shop = Shop.objects.get(pk=pk)
    # shop = get_object_or_404(Shop, pk)
    context = {
        'Title': shop.title,
        'Address_line_1': shop.address_line_1,
        'Address_line_2': shop.address_line_2,
        'Address_State': shop.address_State,
        'Location': shop.location,
        'About': shop.about,
        'Rating': shop.rating,
        'Shop_icon': shop.Shop_icon,
        'Shop_icon_2': shop.Shop_icon_2,
        'Number_of_reviews': shop.number_of_reviews,
    }

    return render(request, 'shop/shop_context.html',
                  {'context': context,
                   'products': shop.product_set.all()})


def ShopAddReview(request, pk):

    if request.method == 'GET':
        return render(request, 'shop/add_rating.html', {})

    if request.method == 'POST':

        shop = Shop.objects.get(pk=pk)
        rating = float(request.POST['rating'])
        comment = request.POST['comment']
        shop.add_review(rating, comment)
        return HttpResponse('Rating Saved')



































