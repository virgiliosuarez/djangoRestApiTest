from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from core.manager.countryManager import CountryManager
from core.utils.paginate import Paginate


class CountryViews:

    @api_view(['GET', 'POST'])
    def country_list_create(request):
        country_manager = CountryManager(request)
        if request.method == 'GET':
            country = country_manager.get_all()
            return Response({'result': country, 'status': status.HTTP_200_OK})

        elif request.method == 'POST':
            serializer = country_manager.create()
            if serializer.errors:
                return Response({'result': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})
            return Response({'result': serializer.data, 'status': status.HTTP_201_CREATED})

    @api_view(['GET'])
    def country_list_paginate(request):
        country_manager = CountryManager(request)
        country = country_manager.get_all()

        paginate = Paginate()
        page = request.GET.get('page', 1)
        paginator = paginate.paginate_model(page, country)

        return Response({'result': country, 'count': paginator.count, 'numpages': paginator.num_pages,
                         'nextlink': '/api/customers/?page=' + str(Paginate.nextPage),
                         'prevlink': '/api/customers/?page=' + str(Paginate.previousPage),
                         'status': status.HTTP_200_OK})

    @api_view(['GET', 'PUT', 'DELETE'])
    def country_detail(request, pk):
        country_manager = CountryManager(request)
        country = country_manager.get(pk)
        if not country:
            return Response({'status': status.HTTP_404_NOT_FOUND})

        if request.method == 'GET':
            return Response({'result': country, 'status': status.HTTP_200_OK})

        elif request.method == 'PUT':
            serializer = country_manager.update(pk)
            if serializer.errors:
                return Response({'result': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})
            return Response({'result': serializer.data, 'status': status.HTTP_426_UPGRADE_REQUIRED})

        elif request.method == 'DELETE':
            country_manager.delete(pk)
            return Response({'status': status.HTTP_200_OK})
