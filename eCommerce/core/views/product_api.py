from django.conf import settings
from django.db import connections

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.user import Profile, Store, Seller, Customer
from ..models.product import Item, Category, ItemSpecification, ItemFavorit, ItemPicture, ItemReturn, ItemReview, ItemReviewPictures, Order
from ..models.others import Shiper
from ..serializers.product import ItemSerializer, OrderSerializer, ItemReturnSerializer, ItemReviewSerializer, ItemPictSerializer
from ..utils import dictfetchall

cursor = connections['default'].cursor()

class ItemView(APIView):
    """
    requestBody = {
        "store_id": 2,
        "name": "Macbook Pro 2020",
        "stock": 15,
        "price": 7999000,
        "desc": "Macbook Pro 2020 with touchbar",
        "category": "Computer",
        "specifications": {
            "Operating System": "MacOs Big Sur",
            "RAM": "16gb",
            "Proccessor": "Intel i7"
        },
        // this is optional
        "pictures": [
            <pict1>,
            <pict2>
        ]
    }
    """
    def post(self, request):
        try:
            data = request.data
            store_id = data.get('store_id')
            try:
                # checking store
                store = Store.objects.get(id = int(store_id))
                # initiate object
                category = None
                item = None
                try:
                    try:
                        category = Category.objects.get(store_id = store_id, category = data.get('category'))
                    except:
                        category = Category.objects.create(store_id = store_id, category = data.get('category'))
                    # lastly make item from data request
                    serializer = ItemSerializer(data = data)
                    if serializer.is_valid():
                        # save item
                        saved = serializer.save()
                        # check for item specifications
                        if 'specifications' in data and data.get('specifications') != '':
                            specifications = data.get('specifications')
                            values = []
                            for key, value in specifications.items():
                                temp = "('{}', '{}', '{}')".format(saved.id, key, value)
                                values.append(temp)
                            sql = """
                                INSERT INTO core_itemspecification (`item_id`, `key`, `value`) VALUES {}
                            """.format(','.join(values))
                            try:
                                # save specifications of item
                                # cursor = connections['default'].cursor()
                                specification = cursor.execute(sql)
                                print(specification)
                                print('saved')
                            except:
                                pass
                        # insert data pictures if exist
                        # have implement yet

                        return Response({"msg":"item success created!", "data":ItemSerializer(saved).data}, status = 201)
                    else:
                        raise
                
                # if there are exception then delete all saved data
                except:
                    if category != None:
                        category.delete()
                    if item != None:
                        item.delete()
                    raise
            except:
                return Response({"error":"store not found"}, status = 404)

        except:
            return Response({"error":"Bad Request"}, status = 400)

    def get(self, request):
        try:
            query = """
                SELECT core_item.id, core_item.name, core_item.stock, core_item.price, core_item.desc, core_item.category, core_item.date_created, core_store.name as store_name
                FROM ((core_item INNER JOIN core_seller ON core_item.store_id=core_seller.store_id) 
                INNER JOIN core_store ON core_store.id=core_seller.store_id)
            """
            cursor.execute(query)
            result = dictfetchall(cursor)
            return Response({"data":result})

        except:
            return Response({"error":"data not found"}, status=404)