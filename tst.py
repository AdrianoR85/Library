from datetime import datetime, timedelta
from app.database.connection import settings
from app.core.security import create_access_token, decode_access_token, hash_password

jonh_smith = hash_password("jonh123")
mary_jones = hash_password("mary123")
sarah_williams = hash_password("sarah123")

#print(f"Jonh Smith's password hash: {jonh_smith}")
#print(f"Mary Jones's password hash: {mary_jones}")
#print(f"Sarah Williams's password hash: {sarah_williams}")


print(settings.database_url)
