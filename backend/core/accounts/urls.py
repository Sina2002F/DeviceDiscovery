from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path('profile/<str:username>',views.profileAPI.as_view(),name="profile"),
    path("sign-up/", views.signUpAPI.as_view(), name="signUp"),
    path("login/", views.loginAPI.as_view(), name="login"),
    path("logout/", views.logoutAPI.as_view(), name="logout"),
    path("delete-account/", views.deleteAccountAPI.as_view(), name="deleteAccount"),
    path("password-recovery/", views.passwordRecoveryAPI.as_view(), name="passwordRecovery"),
    path("password-recovery/<str:email>/<int:code>", views.passwordRecoveryVerificationAPI.as_view(), name="passwordRecoveryVerification")
]
