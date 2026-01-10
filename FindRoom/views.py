from django.http import JsonResponse

def root(request):
    return JsonResponse({
        "message": "FindRoom Backend API is running",
        "status": "ok"
    })
