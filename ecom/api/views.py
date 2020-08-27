from django.http import JsonResponse

# Create your views here.

def home(request):
    return JsonResponse({'info': 'Ecommerce Fullstack project', 'name': "Finny Jose DEveloper"})