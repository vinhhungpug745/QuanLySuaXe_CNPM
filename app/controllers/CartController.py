from flask import request,session,jsonify
from app.utils.cart_util import count_cart

class CartController:
    def add_to_cart(self):
        data = request.json
        id = str(data.get('id'))
        name = data.get('name')
        price = float(data.get('price'))
        image = data.get('image')

        cart = session.get('cart', {})

        if id in cart:
            cart[id]['quantity'] += 1
        else:
            cart[id] = {
                'id': id,
                'name': name,
                'price': price,
                'image': image,
                'quantity': 1
            }

        session['cart'] = cart
        return jsonify(count_cart(cart=cart))
