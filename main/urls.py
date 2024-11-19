from django.urls import path
from main.views import show_home, create_cat_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_cat, delete_cat, create_cat_entry_ajax, create_cat_flutter

app_name = 'main'
urlpatterns = [
    path('', show_home, name='show_home'),
    path('create-cat-entry', create_cat_entry, name='create_cat_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-mood/<uuid:id>', edit_cat, name='edit_cat'),
    path('delete/<uuid:id>', delete_cat, name='delete_cat'),
    path('create-cat-entry-ajax', create_cat_entry_ajax, name='create_cat_entry_ajax'),
    path('create-cat-flutter/', create_cat_flutter, name='create_mood_flutter'),

]
