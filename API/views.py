from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Stair
from .serializers import StairSerializer


@csrf_exempt
def stair_list(request):

    if request.method == 'GET':
        snippets = Stair.objects.all()
        serializer = StairSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def stair_detail(request, pk):
    try:
        snippet = Stair.objects.get(pk=pk)
    except Stair.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StairSerializer(snippet)
        return JsonResponse(serializer.data)