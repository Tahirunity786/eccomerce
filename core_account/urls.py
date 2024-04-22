from django.urls import path
from core_account.views import Profile, Address_Book, Orders, Orders_Cancelation, Orders_Return, Saved
# REST APIs
from core_account.views import GetProfile, UserCartDetailsAgent, UpdatePassword, UserRegistration, UserLogin, EmailAvailability, Profile, Profile_Viewer, ProfileUpdate

urlpatterns = [
    # URLs for user profile views
    path('user/profile', Profile.as_view(), name="Profile"),  # View user profile
    path('user/profile/orders', Orders.as_view(), name="Orders"),  # View user orders
    path('user/profile/items/saved', Saved.as_view(), name="Saved"),  # View saved items
    path('user/profile/address-book', Address_Book.as_view(), name="Address"),  # View address book
    path('user/profile/order-return', Orders_Return.as_view(), name="Order-return"),  # View order return
    path('user/profile/order-cancelation', Orders_Cancelation.as_view(), name="Order-Cancelation"),  # View order cancelation

    # REST APIs
    path('user/get/profile', GetProfile.as_view(), name="Get-Profile"),  
    path('user/cart/', UserCartDetailsAgent.as_view(), name="User-Cart"),  
    path('account/login-user', UserLogin.as_view(), name="LOGIN"),  # User login
    path('create/user', UserRegistration.as_view(), name="REG"),  # User registration
    path('account/user/available', EmailAvailability.as_view(), name="Available"),  # Check email availability
    path('account/user/profile', Profile_Viewer.as_view(), name="profile-view"),  # View user profile (API)
    path('account/user/profile/update', ProfileUpdate.as_view(), name="profile-update-view"),  # Update user profile (API)
    path('account/user/profile/pass/update', UpdatePassword.as_view(), name="profile-pass-update-view"),  # Update user password (API)
]
