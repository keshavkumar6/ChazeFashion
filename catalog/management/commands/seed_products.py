from django.core.management.base import BaseCommand
from catalog.models import Product

class Command(BaseCommand):
    help = 'Seed the database with demo products'

    def handle(self, *args, **kwargs):
        demo_products = [
            # Fila
            {
                'pr_name': 'Fila Classic Tee',
                'pr_cate': 'Men',
                'pr_price': 799.00,
                'pr_reviews': 4.2,
                'pr_stk_quant': 50,
                'pr_brand': 'Fila',
                'pr_images_url': 'https://images.unsplash.com/photo-1512436991641-6745cdb1723f?auto=format&fit=crop&w=400&q=80',
            },
            # Sparkey
            {
                'pr_name': 'Sparkey Sports Shorts',
                'pr_cate': 'Boys',
                'pr_price': 499.00,
                'pr_reviews': 4.0,
                'pr_stk_quant': 40,
                'pr_brand': 'Sparkey',
                'pr_images_url': 'https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=400&q=80',
            },
            # Zara
            {
                'pr_name': 'Zara Summer Dress',
                'pr_cate': 'Women',
                'pr_price': 1599.00,
                'pr_reviews': 4.7,
                'pr_stk_quant': 30,
                'pr_brand': 'Zara',
                'pr_images_url': 'https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?auto=format&fit=crop&w=400&q=80',
            },
            # Adidas
            {
                'pr_name': 'Adidas Running Shoes',
                'pr_cate': 'Men',
                'pr_price': 2999.00,
                'pr_reviews': 4.8,
                'pr_stk_quant': 20,
                'pr_brand': 'Adidas',
                'pr_images_url': 'https://images.unsplash.com/photo-1516574187841-cb9cc2ca948b?auto=format&fit=crop&w=400&q=80',
            },
            # Reebok
            {
                'pr_name': 'Reebok Kids Sneakers',
                'pr_cate': 'Girls',
                'pr_price': 1299.00,
                'pr_reviews': 4.3,
                'pr_stk_quant': 25,
                'pr_brand': 'Reebok',
                'pr_images_url': 'https://images.unsplash.com/photo-1469398715555-76331a6c7b29?auto=format&fit=crop&w=400&q=80',
            },
            # Rupa
            {
                'pr_name': 'Rupa Comfort Vest',
                'pr_cate': 'Men',
                'pr_price': 299.00,
                'pr_reviews': 4.1,
                'pr_stk_quant': 60,
                'pr_brand': 'Rupa',
                'pr_images_url': 'https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=400&q=80',
            },
            # Dollar
            {
                'pr_name': 'Dollar Baby Romper',
                'pr_cate': 'Toddler',
                'pr_price': 399.00,
                'pr_reviews': 4.5,
                'pr_stk_quant': 35,
                'pr_brand': 'Dollar',
                'pr_images_url': 'https://images.unsplash.com/photo-1503602642458-232111445657?auto=format&fit=crop&w=400&q=80',
            },
            # Kothari
            {
                'pr_name': 'Kothari School Uniform',
                'pr_cate': 'Boys',
                'pr_price': 899.00,
                'pr_reviews': 4.0,
                'pr_stk_quant': 45,
                'pr_brand': 'Kothari',
                'pr_images_url': 'https://images.unsplash.com/photo-1469398715555-76331a6c7b29?auto=format&fit=crop&w=400&q=80',
            },
            # Amul
            {
                'pr_name': 'Amul Kids T-shirt',
                'pr_cate': 'Girls',
                'pr_price': 499.00,
                'pr_reviews': 4.2,
                'pr_stk_quant': 38,
                'pr_brand': 'Amul',
                'pr_images_url': 'https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=400&q=80',
            },
            # More variety
            {
                'pr_name': 'Fila Women Hoodie',
                'pr_cate': 'Women',
                'pr_price': 1199.00,
                'pr_reviews': 4.6,
                'pr_stk_quant': 28,
                'pr_brand': 'Fila',
                'pr_images_url': 'https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?auto=format&fit=crop&w=400&q=80',
            },
            {
                'pr_name': 'Adidas Boys Track Pants',
                'pr_cate': 'Boys',
                'pr_price': 799.00,
                'pr_reviews': 4.4,
                'pr_stk_quant': 32,
                'pr_brand': 'Adidas',
                'pr_images_url': 'https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=400&q=80',
            },
        ]

        for prod in demo_products:
            product, created = Product.objects.get_or_create(
                pr_name=prod['pr_name'],
                defaults={
                    'pr_cate': prod['pr_cate'],
                    'pr_price': prod['pr_price'],
                    'pr_reviews': prod['pr_reviews'],
                    'pr_stk_quant': prod['pr_stk_quant'],
                    'pr_dimensions': '',
                    'pr_weights': '',
                    'pr_offers': '',
                    'pr_season': 'All Season',
                    'pr_fabric': '',
                    'pr_texture': '',
                    'pr_brand': prod.get('pr_brand', ''),
                }
            )
            if created and prod['pr_images_url']:
                product.set_image_from_url(prod['pr_images_url'])
        self.stdout.write(self.style.SUCCESS('Demo products seeded!')) 