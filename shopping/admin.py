from django.contrib import admin
from shopping.models import  Contact,Product,Orders,OrderUpdate

admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)