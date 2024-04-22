from django.shortcuts import render
from django.views.generic import TemplateView
# REST API LIBRARY
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
# Serializer
from core_account.serializers import CreateUserSerializer, UserProfileSerializer, ProductSerializer

# Utiles
from core_account.token import get_tokens_for_user
from core_account.serializers import Product
# Get User model
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password
User = get_user_model()
# Create your views here.

class Profile(TemplateView):

    template_name = 'core_account/account.html'

    def get(self, request):

        return render(request, self.template_name)
    

class Address_Book(TemplateView):

    template_name = 'core_account/accounts/address-book.html'

    def get(self, request):

        return render(request, self.template_name)
    

class Orders(TemplateView):

    template_name = 'core_account/accounts/order.html'

    def get(self, request):

        return render(request, self.template_name)
    

class Orders_Cancelation(TemplateView):

    template_name = 'core_account/accounts/order_cancelation.html'

    def get(self, request):

        return render(request, self.template_name)
    

class Orders_Return(TemplateView):

    template_name = 'core_account/accounts/order-returns.html'

    def get(self, request):

        return render(request, self.template_name)


class Saved(TemplateView):

    template_name = 'core_account/accounts/saved.html'

    def get(self, request):

        return render(request, self.template_name)
    

# Super REST APIs
    
class UserRegistration(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Tokken generate for user
            token = get_tokens_for_user(user)

            profile_url = settings.BACKEND + user.profile.url if user.profile else None
            user_data = {
            "id": user.id,
            "email": user.email,
            "full_name": user.full_name,
            "date_of_birth": user.date_of_birth,
            "gender": user.gender,
            "mobile_number": user.mobile_number,
            "profile": profile_url,
            'token':token,
                 }
            return Response({"user":user_data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmailAvailability(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            email = request.POST.get('email')
    
            try:
                User.objects.get(email=email)
                # User exists, email is taken
                return Response({"Success": "Already Taken"}, status=status.HTTP_302_FOUND)
            except ObjectDoesNotExist:
                # User does not exist, email is available
                return Response({"Success": "Available"}, status=status.HTTP_200_OK)
        except Exception as e:
            # Other exceptions
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        if not email or not password:
            return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Email for this user not found"}, status=status.HTTP_400_BAD_REQUEST)

        authenticated_user = authenticate(request, username=user.email, password=password)
        
        if authenticated_user is None:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        profile_url = authenticated_user.profile.url if authenticated_user.profile else None
        token = get_tokens_for_user(authenticated_user)

        user_data = {
            "id": authenticated_user.id,
            "email": authenticated_user.email,
            "full_name": authenticated_user.full_name,
            "date_of_birth": authenticated_user.date_of_birth,
            "mobile_number": authenticated_user.mobile_number,
            "gender": authenticated_user.gender,
            "profile": profile_url,
            "token": token,
}


        return Response({"message": "Logged in", "user": user_data}, status=status.HTTP_202_ACCEPTED)


class Profile_Viewer(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get the authenticated user
        user_data = request.user
        # Extract the user from the database
        try:
            user = User.objects.get(email=user_data.email)  # Access the email attribute of the user_data
        except User.DoesNotExist:
            return Response({"Error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the user profile data
        serializer = UserProfileSerializer(instance=user)
   
        # Return the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileUpdate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Get the authenticated user
        user_data = request.user
        
        # Extract the user profile from the database
        try:
            user_profile = User.objects.get(email=user_data)

        except User.DoesNotExist:
            return Response({"Error": "User profile does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Check if the request data is empty
        if not request.data:
            return Response({"Error": "No data provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        pic = request.FILES.get("pic")
        fullname = request.data.get("full_name")
        email = request.data.get("email")
        mobile = request.data.get("mobile_number")
        gender = request.data.get("gender")
        date_of_birth = request.data.get("date_of_birth")
       
        # Updating the profile
        if pic:
            user_profile.profile = pic
        if fullname:
            user_profile.full_name = fullname
        if email:
            user_profile.email = email
        if mobile:
            user_profile.mobile_number = mobile
        if gender:
            user_profile.gender = gender
        if date_of_birth:
            user_profile.date_of_birth = date_of_birth
        
        user_profile.save()

        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdatePassword(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Get current user
        user = request.user

        # Get data from request
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')
        print(old_password)
        # Check if old password matches
        if not user.check_password(old_password):
            print("Here is check password error")
            return Response({'error': 'Old password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if new password matches confirm password
        if new_password != confirm_password:
        
            return Response({'error': 'New password and confirm password do not match.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if new password is the same as old password
        if old_password == new_password:
            print("Here checking that if user entering old password")
            return Response({'error': 'New password must be different from old password.'}, status=status.HTTP_400_BAD_REQUEST)

        # Update password
        user.password = make_password(new_password)
        user.save()

        return Response({'message': 'Password updated successfully.'}, status=status.HTTP_200_OK)

class UserCartDetailsAgent(APIView):
    
    permission_classes = [AllowAny]

    def post(self, request):
        product_id = request.POST.get("product_id")
        
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"Error":"Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializers = ProductSerializer(instance=product)

        return Response(serializers.data, status=status.HTTP_200_OK)
        
class GetProfile(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user.id

        try:
            user_profile = User.objects.get(id=user)
        except User.DoesNotExist:
            return Response({"Error": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileSerializer(instance=user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
