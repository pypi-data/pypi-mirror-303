from django.conf import settings
from concurrent.futures import ThreadPoolExecutor, as_completed
from .db_check import check_db
from .cache_check import check_cache
from .celery_check import check_celery
from .rmq_check import check_rmq

def run_health_checks():
    checks = {}
    futures = []

    # Create a ThreadPoolExecutor to run checks in parallel
    with ThreadPoolExecutor() as executor:
        if getattr(settings, 'RISHTEDAAR_DB_CHECK', False):
            futures.append(('db', executor.submit(check_db)))
        
        if getattr(settings, 'RISHTEDAAR_CACHE_CHECK', False):
            futures.append(('cache', executor.submit(check_cache)))
        
        if getattr(settings, 'RISHTEDAAR_CELERY_CHECK', False):
            futures.append(('celery', executor.submit(check_celery)))
        
        if getattr(settings, 'RISHTEDAAR_RMQ_CHECK', False):
            futures.append(('rabbitmq', executor.submit(check_rmq)))

        for key, future in futures:
            try:
                checks[key] = future.result()
            except Exception as e:
                checks[key] = (False, str(e))

    overall_health = all(status for status, _ in checks.values())
    return overall_health, {key: value[0] for key, value in checks.items()}
