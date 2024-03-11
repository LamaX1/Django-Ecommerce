from django.shortcuts import render
from .models import  Pcs
from django.http import HttpResponse
from django.template import loader
from store.models import Item, Order
from django.contrib.auth.decorators import login_required

def show_pcs(request):
    computers = Pcs.objects.all()
    return render(request, 'computers.html',{'computers': computers})

def pc_details(request,id):
    pc = Pcs.objects.select_related('pc_category').filter(id=id)
    return render(request, 'computerDetails.html',{'pc' : pc})

@login_required(login_url='/login/')    
def pc_checkout(request,id):
    template=loader.get_template('checkout.html')
    current_user = request.user
    selected_item = Pcs.objects.select_related('pc_category').filter(item_id=id)
    print(selected_item.query)
    print(selected_item)
    for product in selected_item:
        order = Order(
            item_id = product.item_id.id,
            item_name = product.pc_category.name,
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