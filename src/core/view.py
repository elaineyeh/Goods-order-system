from django.http import JsonResponse
from django.shortcuts import redirect


def root(request):
    if request.user.is_authenticated:
        return redirect('/docs')

    return JsonResponse({'name': 'Good order system'})
