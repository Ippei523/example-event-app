import logging

from app.models import User


logger = logging.getLogger(__name__)


def get_current_user(refresh_token):
    current_user = User.objects.get(refresh_token=refresh_token)
    return current_user
