from django.db import connection

def check_db():
    try:
        connection.ensure_connection()
        return True, "Database connection is healthy"
    except Exception as e:
        return False, f"Database error: {str(e)}"
