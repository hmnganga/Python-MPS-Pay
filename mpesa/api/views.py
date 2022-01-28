from rest_framework.generics import CreateAPIView
from mpesa.api.serializers import LNMOnlineSerializer
from mpesa.models import LNMOnline


from rest_framework.permissions import AllowAny

class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permissions_class = [AllowAny]

    def create(self, request):
        print(request.data,"This is request.data")
