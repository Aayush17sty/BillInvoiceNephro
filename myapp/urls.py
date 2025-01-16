from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('add/',views.add,name="add"),
    path("addrec/",views.addrec,name="addrec"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('update/uprec/<int:id>/',views.uprec,name="uprec"),
    path('wrong/', views.wrong_invoice_page, name='incorrect_invoices'),
    path('wrong/delete_wrong/<int:id>/',views.delete_wrong,name="delete_wrong"),
    path('update/wrong/<int:id>/',views.update_wrong,name="update_wrong"),
    path('update/uprec/wrong/<int:id>/',views.uprec_wrong,name="uprec_wrong"),
    path('register/',views.Register,name="register_view"),
    path('login/',views.Login,name="login")
]
