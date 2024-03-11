from store.models import Item


class Cart():
    def __init__(self, request):
        self.session = request.session
        
        cart = self.session.get('session_key')
        
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        self.cart = cart
        
    def add(self,item):
        item_id = str(item.id)
        if item_id in self.cart:
            pass
        else:
            self.cart[item_id] = {'price': str(item.price)}
            
        self.session.modified = True
        
    def get_items(self):
        items_ids = self.cart.keys()
        items = Item.objects.filter(id__in=items_ids)
        return items
        
    def __len__(self):
        return len(self.cart)
    
    def cart_total(self):
        items_ids = self.cart.keys()
        items = Item.objects.filter(id__in=items_ids)
        qty = self.cart
        total = 0
        for key, val in qty.items():
            key = int(key)
            for item in items:
                if item.id == key:
                    total = total + (item.price * val)
        return total