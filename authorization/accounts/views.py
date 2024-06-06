from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from django.core.exceptions import ObjectDoesNotExist


# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "email": user.email,
    }


class UserDetailsView(APIView):
    def get(self, request, pk=None, format=None):
        if pk:
            data = User.objects.get(pk=pk)
            serializer = UserDetailsSerializer(data, many=False)
        else:
            data = User.objects.all()
            serializer = UserDetailsSerializer(data, many=True)
        return Response(serializer.data)


class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(
                {"msg": "Registration Success"}, status=status.HTTP_201_CREATED
            )


class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response(
                    {"message": "Login Success", "token": token},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "errors": {
                            "non_fields_errors": ["Email or password is not correct"]
                        }
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )


class ProductView(APIView):
    def get(self, request, pk=None, format=None):
        if pk:
            data = Product.objects.get(pk=pk)
        else:
            data = Product.objects.all()
        serializer = ProductSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        product_delete = Product.objects.get(pk=pk)
        product_delete.delete()
        return Response({"message": "Product Deleted"})


class CartView(APIView):
    def get(self, request, pk=None, format=None):
        if pk:
            data = Cart.objects.get(pk=pk)
        else:
            data = Cart.objects.all()
        serializer = CartSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        cart_delete = Cart.objects.get(pk=pk)
        cart_delete.delete()
        return Response({"message": "Product Deleted"})

    def put(self, request, pk, format=None):
        cart = Cart.objects.get(pk=pk)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class OrderView(APIView):
    def get(self, request, pk=None, format=None):
        if pk:
            data = Order.objects.get(pk=pk)
        else:
            data = Order.objects.all()
        serializer = OrderSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        order_delete = Order.objects.get(pk=pk)
        order_delete.delete()
        return Response({"message": "Product Deleted"})

    def put(self, request, pk, format=None):
        order = Order.objects.get(pk=pk)
        serializers = OrderSerializer(order, data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)


def check_pk_exists(pk):
    try:
        obj = Profile.objects.get(pk=pk)
        return True
    except ObjectDoesNotExist:
        return False


class ProfileView(APIView):
    def get(self, request, pk=None, format=None):
        if check_pk_exists(pk):
            img = Profile.objects.get(pk=pk)
            serializer = ProfileSerializer(img)
            return Response(serializer.data)
        else:
            return Response(None)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"message": "Image Uploaded Successfully!"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        profile_delete = Profile.objects.get(pk=pk)
        profile_delete.delete()
        return Response({"message": "Image Deleted"})

    def put(self, request, pk, format=None):
        profile = Profile.objects.get(pk=pk)
        serializers = ProfileSerializer(profile, data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)
