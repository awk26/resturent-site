from django.urls import path
from .import views as v
app_name="cart"
urlpatterns = [
    path("product",v.product_list,name="product1"),
    path("showcart",v.show_Cart,name="showcart"),
    path("addtocart",v.Add_cart,name="addtocart"),
    path("del/<int:proid>",v.delete,name="delete"),
    path("pluscart/<int:pid>",v.plus_cart,name="pluscart"),
    path("minuscart/<int:pid>",v.minus_cart,name="minuscart"),
    path("search",v.search, name="srch"),
    path("order",v.order,name="order"),
    path("address",v.address,name="address")
    
   
]