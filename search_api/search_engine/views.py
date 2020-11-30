from django.views import View
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from datetime import timedelta, datetime
from search_api.settings import env
from .helpers import get_client_ip

from .models import Query

from .google_api import GoogleService


# Create your views here.

class SearchView(View):

    def get(self, request):
        ip = get_client_ip(request)
        time_delta = int(env('QUERY_TIME_DELTA_SECONDS'))
        expiration_date = datetime.now(
            tz=timezone.utc) - timedelta(seconds=time_delta)
        query = request.GET.get('query', None)
        result = []

        if not query:
            return HttpResponse('Bad request, not found query', 400)

        result = Query.objects.filter(
            name=query, created__gte=expiration_date, client_ip=ip).order_by('-created').first()

        if not result:
            GOOGLE_API_KEY = env('GOOGLE_API_KEY')
            GOOGLE_CSE_ID = env('GOOGLE_CSE_ID')

            try:
                g_api = GoogleService(GOOGLE_API_KEY, GOOGLE_CSE_ID)
                res = g_api.search(query)
                result = g_api.save_query(res, query, ip)

            except Exception as e:
                return HttpResponse(f'Google service is not available - {e}', 404)

        serialized_query = serialize('python', [result])
        serialized_items = serialize('python', result.items.all())

        response = {
            'query': serialized_query[0]['fields'],
            'items': serialized_items,
            'popular_words': result.get_popular_words()
        }
        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})
