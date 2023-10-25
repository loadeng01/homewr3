from django.contrib import admin
from django.urls import path
from post.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listing/', products_list_api_view),
    path('details/<int:id>/', get_product_api_view),
    path('create/', create_post_api_view),
    path('update/<int:id>/', update_product_api_view),
    path('delete/<int:id>/', delete_product_api_view)
]
