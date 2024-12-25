from django.test import SimpleTestCase
from django.urls import reverse,resolve
from accounts import views

class testAccountsUrls(SimpleTestCase):
    def test_profile_is_resolve(self):
        url=reverse('accounts:profile',kwargs={'username':'test'})
        self.assertEqual(resolve(url).func.view_class,views.profileAPI)

    def test_sign_up_is_resolve(self):
        url=reverse('accounts:signUp')
        self.assertEqual(resolve(url).func.view_class,views.signUpAPI)

    def test_sign_up_is_resolve(self):
        url=reverse('accounts:login')
        self.assertEqual(resolve(url).func.view_class,views.loginAPI)

    def test_sign_up_is_resolve(self):
        url=reverse('accounts:logout')
        self.assertEqual(resolve(url).func.view_class,views.logoutAPI)    

    def test_sign_up_is_resolve(self):
        url=reverse('accounts:deleteAccount')
        self.assertEqual(resolve(url).func.view_class,views.deleteAccountAPI)

    def test_sign_up_is_resolve(self):
        url=reverse('accounts:changePass')
        self.assertEqual(resolve(url).func.view_class,views.changePassAPI)

    def test_sign_up_is_resolve(self):
        url=reverse('accounts:passwordRecovery')
        self.assertEqual(resolve(url).func.view_class,views.passwordRecoveryAPI)

    def test_sign_up_is_resolve(self):
        url=reverse('accounts:passwordRecoveryVerification',kwargs={"email":"test@test.com",'code':123})
        self.assertEqual(resolve(url).func.view_class,views.passwordRecoveryVerificationAPI)