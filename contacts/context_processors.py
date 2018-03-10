from .models import *


def contacts(request):
    email = Email.objects.filter(primary=True)
    phone = Phone.objects.filter(primary=True)
    address = Address.objects.filter(primary=True)
    return {
        'emails': email,
        'phones': phone,
        'address': address
    }