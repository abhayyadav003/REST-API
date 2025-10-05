from django.shortcuts import render
from products.models import ProductsModel
from products.serializers import ProductsSerializers
from products.permissions import IsStaffEditorPermission
from rest_framework import authentication, generics, mixins, permissions

# Create your views here.
# ----------------------------------------------------------------------------------------------------

# class based detail view
# ----------------------------------------------------------------------------------------------------

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializers

product_detail_view = ProductDetailAPIView.as_view()


# class based create view
# ----------------------------------------------------------------------------------------------------

class ProductsCreateAPIView(generics.CreateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializers

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')

        if ((content is None) or (content == '')):
            content = "Content" + title[5:]
        serializer.save(content=content)

product_create_view = ProductsCreateAPIView.as_view()


# class based list view
# ----------------------------------------------------------------------------------------------------

class ProductsListAPIView(generics.ListAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializers

product_list_view = ProductsListAPIView.as_view()


# class based list create view
# ----------------------------------------------------------------------------------------------------

class ProductsListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializers
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')

        if ((content is None) or (content == '')):
            content = "Content" + title[5:]
        serializer.save(content=content)

product_list_create_view = ProductsListCreateAPIView.as_view()


# class based update view
# ----------------------------------------------------------------------------------------------------

class ProductsUpdateAPIView(generics.UpdateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializers
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
           instance.content = "Content" + instance.title[5:]
        serializer.save(content=instance.content)

product_update_view = ProductsUpdateAPIView.as_view()


# class based delete view
# ----------------------------------------------------------------------------------------------------

class ProductsDestroyAPIView(generics.DestroyAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializers
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

product_delete_view = ProductsDestroyAPIView.as_view()


# mixins view
# ----------------------------------------------------------------------------------------------------

class ProductsMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializers
    lookup_field = 'pk'

    # list and detail

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
   
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
   
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

product_mixin_view = ProductsMixinView.as_view()