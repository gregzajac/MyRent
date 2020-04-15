from django.urls import path
from MyRent import views


urlpatterns = [
    path('', views.FlatListView.as_view(), name="flat-list"),
    path('add_flat/', views.CreateFlatView.as_view(), name="add-flat"),
    path('agreement/', views.AgreementListView.as_view(), name="agreement-list"),
    path('add_agreement/', views.AgreementCreateView.as_view(), name="add-agreement"),
    path('agreement/delete/<int:pk>/', views.AgreementDeleteView.as_view(), name="delete-agreement"),
    path('agreement/modify/<int:pk>/', views.AgreementUpdateView.as_view(), name="modify-agreement"),
    path('flat/<int:pk>/', views.FlatDetailView.as_view(), name="flat-detail"),
    path('add_image/<int:flat_id>/', views.ImageCreateView.as_view(), name="add-image"),
    path('delete_image/<int:pk>/', views.ImageDeleteView.as_view(), name="delete-image"),
    path('flat/delete/<int:pk>/', views.FlatDeleteView.as_view(), name="delete-flat"),
    path('flat/modify/<int:pk>/', views.FlatUpdateView.as_view(), name="modify-flat"),
    path('agreement/<int:pk>/', views.AgreementDetailView.as_view(), name="agreement-detail"),
    path('add_operation/<int:agreement_id>/', views.OperationCreateView.as_view(), name="add-operation"),
    path('operation/delete/<int:pk>/', views.OperationDeleteView.as_view(), name="delete-operation"),
    path('operation/modify/<int:pk>/', views.OperationUpdateView.as_view(), name="modify-operation"),
    path('add_obligations/<int:id_agreement>/', views.AddObligationsView.as_view(), name="add-obligations"),
    path('tenant/', views.TenantListView.as_view(), name="tenant-list"),
    path('add_tenant/', views.TenantCreateView.as_view(), name="add-tenant"),
    path('tenant/delete/<int:pk>/', views.TenantDeleteView.as_view(), name="delete-tenant"),
    path('tenant/modify/<int:pk>/', views.TenantUpdateView.as_view(), name="modify-tenant"),

]
