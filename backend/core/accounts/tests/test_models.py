from django.test import TestCase
from django.contrib.auth import get_user_model

class TestAccountModels(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="test@test.com",password="waoojfdoiij@3324ADF")
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_validator)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_admin)
        self.assertFalse(user.is_staff)

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="",password="asfopahsfi@#4589Sljf")


    def test_create_super_user(self):
        User=get_user_model()
        user=User.objects.create_superuser(email="test@test.com",password="wodojfoadsji@#o5u08ASDF")

        self.assertTrue(user.is_active)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_admin)
        self.assertTrue(user.is_validator)
        self.assertTrue(user.is_staff)

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='test@test.com',password='pwijsd@#$123SF',is_superuser=False)