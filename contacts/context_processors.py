from .models import *


def contacts(request):
    email = Email.objects.filter(primary=True)
    phone = Phone.objects.filter(primary=True)
    address = Address.objects.filter(primary=True)
    return {
        'emails': list(email),
        'phones': list(phone),
        'address': list(address)
    }