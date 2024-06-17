import os
from flask_admin import Admin
from models import db, User, Character, Planet, Vehicle, FavoritesCharacters, FavoritesPlanets, FavoritesVehicles
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    class MyFavoritesCharacters(ModelView):
        column_list = ('character_id', 'user_id')
        form_columns = ('character_id', 'user_id')

    class MyFavoritesPlanets(ModelView):
        column_list = ('planet_id', 'user_id')
        form_columns = ('planet_id', 'user_id')

    class MyFavoritesVehicles(ModelView):
        column_list = ('vehicle_id', 'user_id')
        form_columns = ('vehicle_id', 'user_id')

    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Character, db.session))
    admin.add_view(ModelView(Planet, db.session))
    admin.add_view(ModelView(Vehicle, db.session))
    admin.add_view(MyFavoritesCharacters(FavoritesCharacters, db.session))
    admin.add_view(MyFavoritesPlanets(FavoritesPlanets, db.session))
    admin.add_view(MyFavoritesVehicles(FavoritesVehicles, db.session))


    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))