from django.conf import settings

def check_rmq():
    from kombu import Connection
    connection = Connection(settings.CELERY_BROKER_URL, ssl=True)
    try:
        connection.connect()
        print("Connection successful")
        connection.release()
        return True, "Connection successful"
    except Exception as e:
        print(f"Connection failed: {str(e)}")
        connection.release()
        return False, str(e)

