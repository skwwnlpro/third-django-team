from django.contrib.auth.tokens import PasswordResetTokenGenerator


class UserActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp: int) -> str:
        return (str(user.pk) + str(timestamp)) + str(user.is_active)


user_activation_token = UserActivationTokenGenerator()
