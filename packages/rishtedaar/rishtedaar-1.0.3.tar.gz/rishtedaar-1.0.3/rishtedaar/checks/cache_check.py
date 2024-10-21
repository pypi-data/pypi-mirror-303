import warnings


def check_cache(cache_alias='default', test_key='health_check_key', test_value='health_check_value'):
    from django.core.cache import caches
    from django.core.cache.backends.base import CacheKeyWarning
    try:
        warnings.simplefilter("ignore", CacheKeyWarning)
        cache = caches[cache_alias]
        cache.set(test_key, test_value, timeout=5)
        value = cache.get(test_key)
        
        if value == test_value:
            return True, "Cache is healthy"
        else:
            return False, "Cache is unhealthy: Unexpected value retrieved"
    
    except Exception as e:
        return False, f"Cache error: {str(e)}"
