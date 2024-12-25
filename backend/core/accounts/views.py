from django.shortcuts import render
from rest_framework.generics import GenericAPIView

# Create your views here.
class profileAPI(GenericAPIView):
    pass

class signUpAPI(GenericAPIView):
    pass

class loginAPI(GenericAPIView):
    pass

class logoutAPI(GenericAPIView):
    pass

class deleteAccountAPI(GenericAPIView):
    pass

class changePassAPI(GenericAPIView):
    pass

class passwordRecoveryAPI(GenericAPIView):
    pass

class passwordRecoveryVerificationAPI(GenericAPIView):
    pass