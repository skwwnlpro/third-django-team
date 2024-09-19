from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from rest_framework.reverse import reverse
from utils.token import user_activation_token


def message(domain, uidb64, token):
    activation_link = reverse("activate_email", kwargs={"uidb64": uidb64, "token": token})
    return f"아래 링크를 클릭.\n\n회원가입 링크 : http://{domain}{activation_link}"


def send_verification_email(user, domain):
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = user_activation_token.make_token(user)
    message_data = message(domain, uidb64, token)

    mail_title = "이메일 인증을 완료해주세요"
    mail_to = user.email
    email = EmailMessage(mail_title, message_data, to=[mail_to])
    email.send()