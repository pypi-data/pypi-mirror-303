# Rishtedaar: The Nosey Neighbor for Your Django Health

Welcome to **Rishtedaar**—the Django package that’s like that one relative who just can’t resist sticking their nose into everyone’s business and pointing out every little flaw. Whether they’re scrutinizing your wardrobe choices or your career decisions, Rishtedaar is here to make sure every component of your Django application is living up and let you know if it's not!

## Why "Rishtedaar"?

Ever had a relative who knows a little too much about everyone’s life? They’re always ready with unsolicited advice and are quick to point out anything that’s slightly off. That’s exactly what Rishtedaar does for your Django project. It's the ultimate busybody, keeping an eye on your application’s health.

## Features

- **Database Health Check:** Keeps a nosy eye on your database. If it’s not up to snuff, you’ll hear about it.
- **Cache Health Check:** Checks if your cache is working properly—because, of course, a cache that isn’t caching is practically a scandal.
- **Celery Health Check:** Makes sure your Celery workers are on their best behavior and not slacking off.
- **RabbitMQ Health Check:** Monitors RabbitMQ’s performance, ensuring it's not acting up or playing games.
- **Configurable Checks:** Enable or disable checks depending on how much oversight you actually want (or don’t want) from your busybody app.

## Installation

Ready for some unsolicited advice? Install Rishtedaar using pip:

```bash
pip install rishtedaar
```

## Configuration

Just like setting up boundaries with a nosy relative, configure Rishtedaar in your Django settings to manage its level of intrusiveness. Add `rishtedaar` to your `INSTALLED_APPS` and tweak the settings:

```python
# settings.py

INSTALLED_APPS = [
    ...
    'rishtedaar',
    ...
]

# Optional: Configure which health checks to enable
RISHTEDAAR_DB_CHECK = True   # Or False, if you’re feeling rebellious
RISHTEDAAR_CACHE_CHECK = True
RISHTEDAAR_CELERY_CHECK = True
RISHTEDAAR_RMQ_CHECK = True
```

## Usage

Add Rishtedaar’s opinionated perspective to your project by including it in your URL patterns. Because everyone needs a little unsolicited advice:

```python
# urls.py

from django.urls import path
from rishtedaar.views import health_check

urlpatterns = [
    ...
    path('rishtedaar/', include('rishtedaar.urls')),
    ...
]
```

Visit `/health/` to get a detailed status report. Rishtedaar will let you know if everything's perfect or if it has found something to gossip about.

## Example

Here’s what a typical health check response might look like:

```json
{
  "overall_health": true,
  "details": {
    "db": true,
    "cache": true,
    "celery": true,
    "rabbitmq": true
  }
}
```

If there’s trouble brewing, the `overall_health` key will be `false`, and the `details` will provide the dirt on what’s not up to snuff.

## Contributing

Think Rishtedaar could be even more nosy or have a better gossip game? We welcome your contributions! Fork the repo, add your enhancements, and send a pull request. Don’t forget to add tests and documentation, so we can all keep an eye on them.

## License

Rishtedaar is licensed under the MIT License. Check out the [LICENSE](LICENSE) file for all the legal jargon.

[![GitHub](https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ramsuthar305/rishtedaar)
