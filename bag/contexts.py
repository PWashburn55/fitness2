from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    shipping = 0
    
    grand_total = shipping + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'shipping': shipping,
        'grand_total': grand_total,
    }

    return context