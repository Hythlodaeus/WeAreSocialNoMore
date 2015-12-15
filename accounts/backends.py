from models import User
import arrow

class EmailAuth(object):
    def authenticate(self, email=None, password=None):
        try:
            user = User.objects.get(email=email)
            subscription_not_ended = arrow.now() < arrow.get(user.subscription_end)
            if user.check_password(password) and subscription_not_ended:
                return user
        except User.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
