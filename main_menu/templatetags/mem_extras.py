from django import template
from ..models import Like

register = template.Library()


# Убрали takes_context=True. Теперь функция просто ждет аргументы.
@register.simple_tag
def is_liked(user, mem_id):
    # 1. Если пользователь не вошел (Аноним) — лайка нет
    if not user.is_authenticated:
        return False

    # 2. Проверяем базу
    return Like.objects.filter(mem_id=mem_id, author=user).exists()

@register.simple_tag
def is_subscribed(sub, suber):
    if not sub.is_authenticated:
        return False

    # 2. Проверяем базу
    return Like.objects.filter(mem_id=mem_id, author=user).exists()
