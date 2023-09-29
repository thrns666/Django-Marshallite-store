from django.conf import settings


class Cart(object):

    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        print(self.request, 'CART PY')

    def add(self, product):
        # Add a product to the cart or update its quantity.
        product_id = product.id

        if str(product_id) not in self.cart.keys():
            self.cart[product_id] = {
                'userid': self.request.user.id,
                'product_id': product_id,
                'name': product.title,
                'quantity': 1,
                'price': product.price.split()[0],
                'image': product.photo.url,
                'total_price': round(float(product.price.split()[0]), 2)
            }
        else:
            for key, value in self.cart.items():
                if key == str(product.id):
                    value['quantity'] = value['quantity'] + 1
                    value['total_price'] = round(value['quantity'] * float(value['price'].split()[0]), 2)
                    self.save()
                    break

        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        # Remove a product from the cart.
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def decrement(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            if self.cart[product_id]['quantity'] == 1:
                self.remove(product=product)
            else:
                self.cart[product_id]['quantity'] -= 1
            self.save()


    def __len__(self):
        return len(self.cart.values())

    def __iter__(self):
        for i in self.cart.values():
            yield i

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True
