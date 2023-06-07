from django.urls import path
from basicapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='aboutUs'),
    path('contactus/',views.contact,name='contact'),
    path('furnitureitems/',views.furnitureitems,name='furnitureitems'),
    path('book',views.book,name='book'),
    path('modularItems', views.modularItems, name="modularitems"),
    path('chaukos',views.chaukos,name='chaukos'),
]
