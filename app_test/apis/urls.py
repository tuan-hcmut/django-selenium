from django.urls import path
from .views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    #amazon_url
    path("search", search, name="a_search_products"),
]
