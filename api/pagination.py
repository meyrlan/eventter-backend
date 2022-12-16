from rest_framework.pagination import PageNumberPagination as DRFPageNumberPagination


class PageNumberPagination(DRFPageNumberPagination):
    page_size_query_param = "page_size"
    page_size = 20
    max_page_size = 50
