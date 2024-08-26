from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),  # Redirect root URL to employee_list view
    path('add/', views.add_employee, name='add_employee'),
    path('update/<int:employee_id>/', views.update_employee, name='update_employee'),
    path('delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('invoice/excel/<int:employee_id>/', views.create_invoice_excel, name='create_invoice_excel'),
    path('invoice/pdf/<int:employee_id>/', views.create_invoice_pdf, name='create_invoice_pdf'),
]
