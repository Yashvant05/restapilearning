from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 2  # Number of items per page
    page_query_param = 'employees'
    page_size_query_param = 'page_size'  # Allow client to set page size
    max_page_size = 1

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data
        })