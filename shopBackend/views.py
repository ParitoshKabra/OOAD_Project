from re import A
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response
import json
from .models import *
from .serializers import *
from django.contrib.auth import login, authenticate, logout
from rest_framework.decorators import api_view, permission_classes, action
# Create your views here.
from rest_framework.settings import api_settings
from django.middleware.csrf import get_token

from .fetchUtils import ajioScraping, flipkartWebScraping, myntraScraping
from .oauth import exchange_code
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination


class CustomApiViewSet(viewsets.ModelViewSet):
    custom_object = None

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        new_cmnt = json.dumps(
            {"info": "created", "object": self.custom_object, "data": serializer.data})
        Log.objects.create(history_log=new_cmnt, history_user=request.user)
        print(f"{self.custom_object} create audited to logs!")
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        Log.objects.create(history_log=json.dumps(
            {"info": "deleted", "object": self.custom_object, "data": serializer.data}))
        print(f"{self.custom_object} delete audited to logs!",
              history_user=request.user)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

    def dispatch(self, *args, **kwargs):
        response = super(CustomApiViewSet, self).dispatch(*args, **kwargs)
        response['Access-Control-Allow-Origin'] = 'http://127.0.0.1:3000'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response


class ItemApiViewSet(CustomApiViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated, ]
    custom_object = "Item"


class UserApiViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]


class NotificationApiViewSet(CustomApiViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated, ]
    custom_object = "Notifications"


class CommentApiViewSet(CustomApiViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ]
    custom_object = "Comment"


class LogApiViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

    permission_classes = [IsAuthenticated, ]


def getItem(url):
    item = None
    if "ajio" in url:
        item = ajioScraping.fetchFromAjio(url)
        # print(User.objects.get(username=User))
        # Item.objects.create(title= item["title"],apiLink= item["apiLink"], price=item["price"], added_by= User,image=item["image"])
        # request1= request
        # request1.data= item
        # ItemApiViewSet.create(request1)
        # return item

    elif "myntra" in url:
        item = myntraScraping.fetchFromMyntra(url)
        # Item.objects.create(title= item["title"],apiLink= item["apiLink"], price=item["price"], added_by= User, image=item["image"])
        # return item

    elif "flipkart" in url:
        item = flipkartWebScraping.fetchFromFlipkart(url)
    else:
        return "null"
    return item


@api_view(("POST", ))
def admin_login(request):
    user = authenticate(username=request.data.get(
        'username'), password=request.data.get('password'))
    if user is not None:
        login(request, user)
        res = Response({"sessionid": request.session._session_key, "csrftoken": get_token(
            request)}, status=status.HTTP_202_ACCEPTED)
        return res
    else:
        return Response({"error": "user not found"}, status=status.HTTP_202_ACCEPTED)


@api_view(("GET",))
def get_csrf_token(request):
    return Response({"csrftoken": get_token(request)}, status=status.HTTP_202_ACCEPTED)


@api_view(("GET", ))
def check_login(request):
    print(request.user)
    msg = {
        "loggedin": True
    }

    # return JsonResponse({'status': 'successful'})
    if not request.user.is_authenticated:
        msg = {
            "loggedin": False
        }
    res = Response(msg, status=200)
    res['Access-Control-Allow-Origin'] = 'http://127.0.0.1:3000'
    res['Access-Control-Allow-Credentials'] = 'true'
    return res


@api_view(("GET", ))
def fetchItem(request):
    url = request.GET.get("url")
    item = getItem(url)
    if item == "null":
        return Response({"error": "Service unreachable at this url", "status": status.HTTP_404_NOT_FOUND})

    if item is not None:
        item["added_by"] = request.user.id
        return Response({"item": item, "status": status.HTTP_202_ACCEPTED})
    else:
        return Response({"error": "Item not found", "status": status.HTTP_404_NOT_FOUND})


@api_view(("GET", ))
def google_oauth(request):
    try:
        msg = "login already"
        if request.user.is_authenticated:
            return Response({"success": msg}, status=200)
        code = request.GET.get('code')
        print(code)
        user = exchange_code(code)

        user_ = authenticate(request=request, user_json=user)
        print("inside oauth:", user_)
        if user_ is not None:
            login(request, user_)
        return Response({"sessionid": request.session._session_key, "csrftoken": get_token(
            request)}, status=status.HTTP_200_OK)

    except Exception as e:
        print(e)
        return Response({"error": e}, status=500)


@api_view(("GET", ))
def info(request):
    info = UserSerializer(request.user)
    res = Response(info.data, status=status.HTTP_202_ACCEPTED)
    res['Access-Control-Allow-Origin'] = 'http://127.0.0.1:3000'
    res['Access-Control-Allow-Credentials'] = 'true'
    return res


@api_view(("GET",))
def log_out(request):
    logout(request)
    return Response({"msg": "logged out successfully"}, status=status.HTTP_202_ACCEPTED)

# Items jinpe notifenabled hain alag alag
# Model extNotif ---> info, content, info : availability| price-change (refresh-item/patch request from front-end) item (apiLink)(comparison or change), info : discount, content, foreignKey


def get_ext_notif_object(item, info, content):
    data = {
        "assoc_item": item,
        "ext_notif_info": info,
        "ext_notif_content": content
    }
    return ExternalNotification.objects.create(**data)


@api_view(("GET",))
@permission_classes(['IsAuthenticated', ])
def get_ext_notifs(request):
    items = Item.objects.all()
    for item in items:
        if item.availability_notif_enabled == True or item.price_notif_enabled == True:
            item_pres = getItem(item.apiLink)

            if item_pres.price != item.price:
                if item.price_notif_enabled == True:
                    get_ext_notif_object(
                        item, "price", f"Changed price: from {item.price} to {item_pres.price}")
            else:
                if item_pres.availability_status != item.availability_status:
                    get_ext_notif_object(
                        item, "available", not item.availability_status)

        elif item.discount_schemes_notif_enabled:
            item_pres = getItem(item.apiLink)
            if item_pres.discount_offers != item.discount_offers:
                get_ext_notif_object(
                    item, "discount", item_pres.discount_offers)

    ext_notif = ExternalNotification.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 5
    result_page = paginator.paginate_queryset(ext_notif, request)
    serializer = ExternalNotificationSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# not tested until item_pres and item have changes // TODO: out of stock, discount
