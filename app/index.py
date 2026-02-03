from flask import session
from app.routes.index import route_web
from app.routes.api.index import route_api
from app._init_ import create_app, login_manager, db
from app.models.model import User
from app import admin

from app.utils.cart_util import count_cart

app = create_app()

route_web(app)
route_api(app)
admin.init_admin(app,db)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.context_processor
def common_response():
    cart = session.get('cart', {})
    return {
        'cart_stats': count_cart(cart)
    }

if __name__ == "__main__":
    app.run(debug=True)
    print(app.url_map)