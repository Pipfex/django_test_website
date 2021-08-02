from django.shortcuts import render
from .models import Order
from  .forms import OrderForms

# Create your views here.
def first_page(request):
    object_list = Order.objects.all()
    form = OrderForms()
    return render(request, './index.html', {'object_list': object_list,
                                            'form':form})


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    elements = Order(order_name=name, order_phone=phone)
    elements.save()
    return render(request, './thanks_page.html', {'name': name,
                                                  'phone': phone})
