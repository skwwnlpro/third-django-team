from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from .serializers import SignUpSerializer, LoginSerializer
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from utils.token import user_activation_token
from utils.email import send_verification_email
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)

        if serializer.is_valid():
            # 데이터 검증:
            # 시리얼라이저에 정의된 모든 필드에 대해 유효성 검사를 수행합니다.
            # 각 필드의 타입, 필수 여부, 최대/최소 길이 등 기본적인 제약 조건을 확인합니다.
            # 커스텀 유효성 검사:
            # validate_<field_name> 메서드가 정의되어 있다면 해당 필드에 대한 추가 검증을 수행합니다.
            # validate() 메서드가 정의되어 있다면 객체 수준의 유효성 검사를 수행합니다.
            # 검증 결과 처리:
            # 모든 검증을 통과하면 True를 반환합니다.
            # 검증에 실패하면 False를 반환하고, 오류 정보를 serializer.errors에 저장합니다.
            user = serializer.save()

            # Token 생성과 Email 인증
            current_site = get_current_site(request)
            send_verification_email(user, current_site.domain)

            return Response({"message": "SignUp is successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailActivate(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)

            if user_activation_token.check_token(user, token):
                user.is_active = True
                user.save()

                return Response({"message": "Email verification has been confirmed."}, status=status.HTTP_200_OK)

            return Response({"message": "AUTH FAIL"}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({"message": "INVALID_KEY"}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]  # 시리얼라이저에서 인증된 사용자 가져오기
        refresh = RefreshToken.for_user(user)  # 가져온다음 refresh token 생성

        access_token = refresh.access_token  # type: ignore

        response = Response({"message": "로그인이 성공했습니다."}, status=status.HTTP_200_OK)

        # cookies에 access token 저장
        response.set_cookie(
            key="access_token",
            value=str(refresh.access_token),  # type: ignore
            httponly=True,  # 자바스크립트 접근 불가
            secure=True,  # HTTPS에서만 전송
            samesite="Lax",  # CSRF 방지용
            max_age=3600,  # 1시간동안 쿠키 유지
        )
        # cookies에 refresh token 저장
        response.set_cookie(key="refresh_token", value=str(refresh), httponly=True, secure=True, samesite="Lax")
        return response


class LogoutAPIView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"success": "User logged out successfully"}, status=status.HTTP_200_OK)
        except TokenError:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):    
        user = request.user
        
        return Response({'id': user.id, "email":user.email})
