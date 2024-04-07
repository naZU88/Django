from django.urls import path
from .views import add_user, many_fields_form, upload_image, user_form


urlpatterns = [
path('user/add/', user_form, name='user_form'),
path('forms/', many_fields_form, name='many_fields_form'),
path('user/', add_user, name='add_user'),
path('upload/', upload_image, name='upload_image'),

]
