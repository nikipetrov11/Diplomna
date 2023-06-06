from django.urls import path

from app_admin import views
from cars.forms import CustomLoginAuthenticationForm

urlpatterns = [
    path('login/', views.LoginAdminView.as_view(authentication_form=CustomLoginAuthenticationForm), name='admin_login'),
    path('', views.AdminPanelView.as_view(), name='admin_panel'),
    path('car-list/', views.AdminCarListView.as_view(), name='admin_car_list'),
    path('add-car/', views.AdminCarCreateView.as_view(), name='admin_add_car'),
    path('car/<int:pk>/', views.AdminCarDetailView.as_view(), name='admin_car_detail'),
    path('car/<int:pk>/delete/', views.AdminCarDeleteView.as_view(), name='admin_car_delete'),
    path('car/<int:pk>/update/', views.AdminCarUpdateView.as_view(), name='admin_car_update'),
    path('car/<int:pk>/add-event/', views.AdminAddEventToCarCreateView.as_view(), name='admin_add_event'),
    path('event-details/<int:pk>/', views.AdminEventDetailView.as_view(), name='admin_event_detail'),
    path('event/<int:pk>/delete/', views.AdminEventDeleteView.as_view(), name='admin_event_delete'),
    path('event/<int:pk>/update/', views.AdminEventUpdateView.as_view(), name='admin_event_update'),
    path('service-request-list/', views.AdminServiceRequestListView.as_view(), name='admin_service_request_list'),
    path('not-seen-service-request-list/',
         views.AdminServiceRequestNotSeenView.as_view(),
         name='not_seen_admin_service_request_list'
         ),
    # TODO: Not needed for now, the view is a comment too
    # path('service-request/<int:pk>/',
    #      views.AdminServiceRequestDetailView.as_view(),
    #      name='admin_service_request_detail'
    #      ),
    path('invited-users-requests-list/',
         views.AdminInvitedUserRequestsListView.as_view(),
         name='invited_user_requests_list'
         ),
    path('account-deatils/', views.AdminAccountDetails.as_view(), name='admin_account_details'),
]
