from django.http import JsonResponse
from rishtedaar.checks import run_health_checks

def health_check_view(request):
    overall_health, details = run_health_checks()
    status_code = 200 if overall_health else 500
    return JsonResponse({
        "healthy": overall_health,
        "details": details,
    }, status=status_code)
