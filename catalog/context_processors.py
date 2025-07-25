from datetime import datetime

def cart_count(request):
    cart = request.session.get('cart', {})
    return {'cart_count': sum(cart.values()), 'year': datetime.now().year} 