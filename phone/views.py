from django.shortcuts import render
from .models import Phone
from django.http import HttpResponse
from django.template import loader
from store.models import Item, Order
from django.contrib.auth.decorators import login_required


def show_phones(request):
    phones = Phone.objects.all()
    return render(request, 'phones.html',{'phones': phones})

def phone_details(request,id):
    phone = Phone.objects.select_related('phone_category').filter(id=id)
    return render(request, 'phoneDetails.html',{'phone' : phone})

@login_required(login_url='/login/')
def phone_checkout(request,id):
    template=loader.get_template('checkout.html')
    current_user = request.user
    selected_item = Phone.objects.select_related('phone_category').filter(item_id=id)
    print(selected_item.query)
    print(selected_item)
    for product in selected_item:
        order = Order(
            item_id = product.id,
            item_name = product.phone_category.name,
            customer = current_user.id,
            price = product.price
            )
    order.save()
    get_order = Order.objects.filter(customer=current_user.id).order_by('-created_at').first()
    product_name = Item.objects.get(id=get_order.item_id)
    context= {
        'request': request,
        'order': product_name
    }
    return HttpResponse(template.render(context=context)) 