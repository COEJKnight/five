from rest_framework.response import Response
from rest_framework.views import APIView
from usaspending_api.common.cache_decorator import cache_response
from usaspending_api.spending_explorer.v2.filters.type_filter import type_filter


class SpendingExplorerViewSet(APIView):

    @cache_response()
    def post(self, request):

        json_request = request.data
        _type = json_request.get('type')
        filters = json_request.get('filters', None)

        # Returned filtered queryset results
        results = type_filter(_type, filters)

        return Response(results)
