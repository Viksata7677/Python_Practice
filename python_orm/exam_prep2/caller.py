import os
import django
from django.db.models import Q, Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Order, Product


def get_profiles(search_string=None):
    if search_string is None:
        return ''

    profiles = Profile.objects.filter(Q(full_name__icontains=search_string) | Q(email__icontains=search_string) | Q(phone_number__icontains=search_string)).order_by('full_name')

    if not profiles.exists():
        return ''

    return '\n'.join(f"Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.orders.count()}" for p in profiles)


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()

    if not profiles.exists():
        return ''

    return '\n'.join(f"Profile: {p.full_name}, orders: {p.orders.count()}" for p in profiles)


def get_last_sold_products():
    last_order = Order.objects.prefetch_related('products').last()

    if last_order is None or not last_order.products.exists():
        return ''

    products = ', '.join([p.name for p in last_order.products.order_by('name')])

    return f"Last sold products: {products}"


def get_top_products():
    top_products = Product.objects.annotate(
        orders_count=Count('order')
    ).filter(
        orders_count_gt=0
    ).order_by('-orders_count', 'name')[:5]

    if not top_products.exists():
        return ''

    product_lines = '\n'.join(f"{p.name}, sold {p.orders_count} times" for p in top_products)

    return f"Top products:\n" + product_lines