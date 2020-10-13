from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models.user import Profile, Store, Seller, Customer
from ..models.product import Item, Category, ItemSpecification, ItemFavorit, ItemPicture, ItemReturn, ItemReview, ItemReviewPictures, Order
from ..models.others import Shiper

class RegisterUser(APIView):
    def post(self, request):
        """
        requestBody = {
            "first_name": "",
            "last_name": "",
            "email": "",
            "username":"",
            "password":"",
            "role":"<customer/seller>"
        }
        if role was customer then request body must be following example:   
        requestBody = {
            "first_name": "",
            "last_name": "",
            "email": "",
            "username":"",
            "password":"",
            "role":"customer",
            "address": "",
            "pict": "<this is optional>"
        }
        and if seller:
        requestBody = {
            "first_name": "",
            "last_name": "",
            "email": "",
            "username":"",
            "password":"",
            "role":"seller",
            "store_name": "",
            "store_address": "",
            "store_pict": "<this is optional>"
        }
        """
        try:
            data = request.data
            role = data.get('role')
            if role.lower() == "customer":
                user = None
                profile = None
                customer = None
                try:
                    # create user
                    user = User(
                        first_name = data.get('first_name'),
                        last_name = data.get('last_name'),
                        email = data.get('email'),
                        username = data.get('username')
                    )
                    user.set_password(data.get('password'))
                    # user.is_staff = True
                    user.save()

                    # create profile
                    profile = Profile.objects.create(user = user, user_type = role)

                    # create customer
                    customer = Customer.objects.create(
                        user_id = user.id,
                        address = data.get('address') if 'address' in data and data.get('address') != '' else None,
                        pict = data.get('pict') if 'pict' in data and data.get('pict') != '' else None
                    )

                    return Response({"msg":"user success created", "id": user.id})

                except:
                    if user != None:
                        user.delete() # delete user
                    if profile != None:
                        profile.delete() # delete profile
                    if customer != None:
                        customer.delete() # delete customer
                    raise

            elif role.lower() == "seller":
                user = None
                store = None
                seller = None
                try:
                    # create user
                    user = User(
                        first_name = data.get('first_name'),
                        last_name = data.get('last_name'),
                        email = data.get('email'),
                        username = data.get('username')
                    )
                    user.set_password(data.get('password'))
                    # user.is_staff = True
                    user.save()

                    # create store
                    store = Store.objects.create(
                        name = data.get('store_name'),
                        address = data.get('store_address'),
                        pict = data.get('store_pict') if 'store_pict' in data and data.get('store_pict') != '' else None
                    )

                    # create seller
                    seller = Seller.objects.create(
                        user_id = user.id,
                        store_id = store.id
                    )

                    return Response({"msg":"user success created", "id": user.id})

                except:
                    if user != None:
                        user.delete() # delete user
                    if store != None:
                        store.delete() # delete store
                    if seller != None:
                        seller.delete() # delete seller
                    raise
                
            else:
                return Response({"error":"role not found"}, status = 400)

        except:
            return Response({"error":"Bad Request"}, status = 400)