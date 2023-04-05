

from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.store,name='store'),
    path('product/<slug:slug>/',views.product_info,name='product-info'),
]