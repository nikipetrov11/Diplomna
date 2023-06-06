from django.contrib import admin as django_admin
from django.urls import path, include

from cars import views, service_info_views
from cars.forms import CustomLoginAuthenticationForm

handler404 = 'cars.views.handler404'
handler403 = 'cars.views.handler403'

service_info_urls = [
    path('', service_info_views.ServicesInfoView.as_view(), name='index_service_info'),
    path('1/', service_info_views.ServicesInfoView1.as_view(), name='1_service_info'),
    path('2/', service_info_views.ServicesInfoView2.as_view(), name='2_service_info'),
    path('3/', service_info_views.ServicesInfoView3.as_view(), name='3_service_info'),
    path('4/', service_info_views.ServicesInfoView4.as_view(), name='4_service_info'),
    path('5/', service_info_views.ServicesInfoView5.as_view(), name='5_service_info'),
    path('6/', service_info_views.ServicesInfoView6.as_view(), name='6_service_info'),
    path('7/', service_info_views.ServicesInfoView7.as_view(), name='7_service_info'),
    path('8/', service_info_views.ServicesInfoView8.as_view(), name='8_service_info'),
    path('9/', service_info_views.ServicesInfoView9.as_view(), name='9_service_info'),
]

urlpatterns = [
    path('django-admin/', django_admin.site.urls),
    path('admin/', include('app_admin.urls')),
    path('login/', views.UserLoginView.as_view(authentication_form=CustomLoginAuthenticationForm), name='login'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('register-success/', views.RegisterSuccess.as_view(), name='reg_success'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.IndexView.as_view(), name='index'),
    path('my-cars/', views.UserCarListView.as_view(), name='user_car_list'),
    path('live-car/<int:pk>/', views.LiveCarView.as_view(), name='live_car'),
    path('service-request/', views.ServiceRequestCreateView.as_view(), name='service_request'),
    path('success-service-request/',
         views.SuccessServiceRequestView.as_view(),
         name='success_service_request'
         ),
    path('invited-user-request/',
         views.InvitedUserCarRequestView.as_view(),
         name='invited_user_request'
         ),
    path('about/', views.AboutView.as_view(), name='about'),
    path('price-and-discounts/', views.PriceAndDiscountView.as_view(), name='price_and_discount'),
    path('service-info/', include(service_info_urls)),
    path('contacts/', views.ContactView.as_view(), name='contacts'),
    path('contact-success/', views.ContactSuccessView.as_view(), name='contact_success'),
    path('shop/', views.ShopView.as_view(), name='shop'),
]
