import json
import logging

from django.db.models import Q
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
# Create your views here.
from shop.models.clothes import Clothes
from shop.serializers import ClothesSerializer

# logger = logging.getLogger(__name__)


class ClothesViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        if self.request.query_params.get("q", None):
            name = self.request.query_params['q']
            return super().get_queryset().filter(name__icontains=name)
        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        clothes_obj = self.get_queryset()
        page = self.paginate_queryset(clothes_obj)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return Response(serializer.data)

        serializer = self.get_serializer(clothes_obj, many=True)

        # logger.info("Show all Clothes List")
        return Response(serializer.data)

    @action(methods=["GET"], detail=False)
    def search(self, request):
        query = request.GET.get('query', None)
        if query is not None:
            clothes = Clothes.objects.filter(
                Q(name__icontains=query) |
                Q(brand__name__icontains=query)
                # Q(category__name__icontains=query)
            )
            # clothes2 = Clothes.objects.filter(brand__name__icontains=query)
            serializer = ClothesSerializer(instance=clothes, many=True)

            # logger.info(f"list of searches for {query}")
            return Response(serializer.data, status=200)
        else:
            return Response(
                {"message": _("Please enter your search word")
                 },
                status=400
            )

    @action(methods=["GET"], detail=False)
    def filter(self, request):
        name_param = request.GET.get('name', None)
        brand_param = request.GET.get('brand', None)
        color_param = request.GET.get('color', None)
        category_param = request.GET.get('category', None)

        clothes = Clothes.objects.all()
        if name_param is not None:
            clothes = clothes.filter(name__icontains=name_param)
        if brand_param is not None:
            clothes = clothes.filter(brand__name__icontains=brand_param)
        if color_param is not None:
            clothes = clothes.filter(color__name__icontains=color_param)

        serializer = ClothesSerializer(instance=clothes, many=True)

        return Response(serializer.data, status=200)



    # @staticmethod
    # def __filter_valid_key(param_dict: dict):
    #     filter_result = []
    #     for param in param_dict:
    #         filter_result.append(param_dict.get(param))
    #     return filter_result


