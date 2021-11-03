from django.urls import path
from . import views

urlpatterns =[
				path('', views.home, name='home'),
				path('about/', views.about, name='about'),
				path('ships/', views.ships_index, name='index'),
				path('ships/<int:ship_id>/', views.ships_detail, name='detail'),
				path('ships/create/', views.ShipCreate.as_view(),name='ships_create'),
				path('ships/<int:pk>/update/',views.ShipUpdate.as_view(),name='ships_update'),
				path('ships/<int:pk>/delete/',views.ShipDelete.as_view(),name='ships_delete'),
				path('ships/<int:ship_id>/add_resupply/', views.add_resupply, name='add_resupply'),
				path('ships/<int:ship_id>/assoc_equipment/<int:equipment_id>/', views.assoc_equipment, name='assoc_equipment'),
				path('equipment/', views.EquipmentList.as_view(), name='equipment_index'),
				path('equipment/<int:pk>/', views.EquipmentDetail.as_view(), name='equipment_detail'),
				path('equipment/create/', views.EquipmentCreate.as_view(), name='equipment_create'),
				path('equipment/<int:pk>/update/', views.EquipmentUpdate.as_view(), name='equipment_update'),
				path('equipment/<int:pk>/delete/', views.EquipmentDelete.as_view(), name='equipment_delete'),
]