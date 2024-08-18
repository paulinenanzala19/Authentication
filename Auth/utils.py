from django.core.cache import cache
from django.contrib.auth import get_user_model

User = get_user_model()

def get_user_from_cache_or_db(user_id):
    user = cache.get(f'user_{user_id}')
    if not user:
        user = User.objects.get(id=user_id)
        cache.set(f'user_{user_id}', user, timeout=60*60*24)
    return user
