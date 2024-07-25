from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .services import GhostService
from django.middleware.csrf import get_token

ghost_service = GhostService(settings.GHOST_API_URL, settings.GHOST_API_KEY)

def submit_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        response = ghost_service.create_post(title, content)
        print('Title received:', title)
        print('Content received:', content)
        print(request)
        return JsonResponse(response)
    return render(request, 'blog/submit_post.html')

def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})
