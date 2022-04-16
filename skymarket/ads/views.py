from rest_framework import pagination, viewsets

from ads.models import Ad
from ads.serializers import AdSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class CommentViewSet(viewsets.ModelViewSet):
    pass

