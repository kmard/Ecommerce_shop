from django.shortcuts import render
from .models import ShippingAddress,Order,OrderItems
from cart.cart import Cart

# Create your views here.

def checkout(request):

    #Users with account -- pre-fill the form

    if request.user.is_authenticated:

        try:
           #Authenticated user with shipping information
           shipping_address = ShippingAddress.objects.get(request.user.id)
           context = {'shipping':shipping_address}

           return render(request, 'payment/checkout.html',context=context)

        except:
            #no authenticated user
            return render(request,'payment/checkout.html')

    #Guest user
    return render(request, 'payment/checkout.html')

def complete_order(request):

    if request.POST.get('action') == 'post':

        name = request.POST.get('name')
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')

        #All-in-one shipping address
        shipping_address = (address1+ '\n'+address2+'\n'+
                            city+'\n'+state+'\n'+zipcode
                            )

        #Shopping cart information
        cart = Cart(request)

        #Get the total price of the items
        total_cost = cart.get_total()

        """
          Order variations
          
          1) Create order -> Account users WITH+WITHOUT shipping information
          
          2) Create order -> Guest users without an account
          
        """



def payment_success(request):

    return render(request,'payment/payment-success.html')

def payment_failed(request):
    return render(request, 'payment/payment-failed.html')