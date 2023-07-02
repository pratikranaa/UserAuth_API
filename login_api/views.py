from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.hashers import check_password
from rest_framework import status
from .login_serializer import *
from django_filters.rest_framework import DjangoFilterBackend
from . import utils
# from login_api.models import Entities
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API’s endpoint that allows users to be modified.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
#     filterset_fields = ("__all__")
#     ordering_fields = ("__all__")

#     def create(self, request):
#         try:
#             data = request.data
#             email= data.get("email")
#             user=User.objects.filter(email=email) 
#             if user:
#                 return Response(utils.error("User Already Exist With This Email Id"))
#             else:
#                 haveCompany = False
#                 if 'company' in data:
#                     companyIds = data.pop('company')
#                     haveCompany = True
#                 serializer = UserSerializer(data=data, context={'request':request})
#                 if serializer.is_valid(raise_exception=True):
#                     serializer.save()
#                     userId = User.objects.get(id=serializer.data.get('id'))
#                     if haveCompany:
#                         for company in companyIds:
#                             companyRec = Entities.objects.get(id=company)
#                             companyRec.user.add(userId)

#                 newUser = User.objects.get(id=userId)
#                 result = UserSerializer(newUser, context={'request':request})
#                 return Response(utils.success_msg(result.data))
#         except Exception as e:
#             return Response(utils.error(str(e)))

#     def update(self, request, pk):
#         try:
#             data = request.data
#             userRec = User.objects.get(id=pk)
#             haveCompany = False
#             if 'company' in data:
#                 companyIds = data.pop('company')
#                 haveCompany = True
#             if 'password' in data:
#                 msg = "Password Can't be updated through this interface."
#                 return Response(utils.error(msg))
#             else:
#                 serializer = UserSerializer(userRec, data=data, context={'request':request})
#                 if serializer.is_valid(raise_exception=True):
#                     serializer.save()
#                     userId = User.objects.get(id=serializer.data.get('id'))
#                     if haveCompany:
#                         oldCompanyRec = userId.entity_set.all()
#                         for ids in oldCompanyRec:
#                             oldRec = Entities.objects.get(id=ids)
#                             if ids not in companyIds:
#                                 oldRec.user.remove(userId)

#                         for company in companyIds:
#                             companyRec = Entities.objects.get(id=company)
#                             if company not in oldCompanyRec:
#                                 companyRec.user.add(userId)

#                 msg = "User Updation Successful."
#                 return Response(utils.success_msg(msg))
#         except Exception as e:
    #         return Response(utils.error(str(e)))

    # # Change Password
    # @action(detail=False, methods=['post'], url_path = "change-password")
    # def changePassword(self, request):
    #     serializers = ChangePasswordSerializer(data = request.data)
    #     if serializers.is_valid(raise_exception=True):
    #         currPass = serializers.data.get('current_password')
    #         newPassword = serializers.data.get('new_password')
    #         userId = request.user.id
    #         user = User.objects.get(id=userId)
    #         password = user.password
    #         if check_password(currPass, password):
    #             user.set_password(newPassword)
    #             user.save()
    #             msg = "Password changed successfully!"
    #             response = {'status': 'success','code': status.HTTP_200_OK,'message': msg}
    #             return Response(response)
    #         else:
    #             msg = "Enter a valid password and try again!"
    #             response = {'status': 'error','code': status.HTTP_200_OK,'message': msg}
    #             return Response(response)
    #     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # # Logging Users Out
    # @action(detail=False, methods=['get'], url_path = "logout")
    # def user_logout(self, request):
    #     try:
    #         print("request.data--------------->",request.auth.lifetime.total_seconds.__reduce__())
    #         logout(request)
    #         return Response('User Logged out successfully')
    #     except Exception as e:
    #         print("ERROR:- ", str(e))
    #         return Response(utils.error(str(e)))
    
class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer


from rest_framework.parsers import JSONParser
from django.http import JsonResponse


@csrf_exempt 
def request_reset_email(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = SendPasswordResetEmailSerializer(data=data)
        if serializers.is_valid(raise_exception=True):
            msg = "Password Reset link send. Please check your email."
            response = {'status': 'success','code': status.HTTP_200_OK,'message': msg}
            return JsonResponse(response, status=201)
        return JsonResponse(serializers.errors, status=400)

#Reset Password
@csrf_exempt
def resetPassword(request):
    if request.method == 'POST':
        uid = request.GET.get('uid')
        token = request.GET.get('token')
        data = JSONParser().parse(request)
        serializers = UserPasswordResetSerializer(data = data, context = {'uid':uid, 'token': token})
        if serializers.is_valid(raise_exception=True):
            msg = "Password Reset successfully"
            response = {'status': 'success','code': status.HTTP_200_OK,'message': msg}
            return JsonResponse(response, status=201)
        return JsonResponse(serializers.errors, status=400)
    
