import decimal
from random import choices
from django.core.management.base import BaseCommand
from secondapp.models import Client, Product, Order


LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. " \
"Accusamus accusantium aut beatae consequatur consequuntur cumque, delectus et illo iste maxime " \
"nihil non nostrum odio officia, perferendis placeat quasi quibusdam quisquam quod sunt " \
"tempore temporibus ut voluptatum? A aliquam culpa ducimus, eaque eum illo mollitia nemo " \
"tempore unde vero! Blanditiis deleniti ex hic, laboriosam maiores odit officia praesentium " \
"quae quisquam ratione, reiciendis, veniam. Accusantium assumenda consectetur consequatur " \
"consequuntur corporis dignissimos ducimus eius est eum expedita illo in, inventore " \
"ipsum iusto maiores minus mollitia necessitatibus neque nisi optio quasi quo quod, " \
"quos rem repellendus temporibus totam unde vel velit vero vitae voluptates."

class Command(BaseCommand):
    help = "Generate fake clients and orders and products."
        
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')
    
    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Author_{i}',
            email=f'mail{i}@mail.ru', phone_number=f'number_{i}', adress=f'adress_{i}')
            client.save()
            product = Product(
                name=f'Name-{i}',
                description=" ".join(choices(text, k=64)),
                price=i,
                quant=i
                )
            product.save()
            for j in range(1, count + 1):
                order = Order(
                            customer=client, 
                            total_price=j
                )
                
                order.save()
        for i in range(1, count+1):
            products = Product.objects.all()[:i]
            order = Order.objects.get(id=i)
            order.products.set(products)
