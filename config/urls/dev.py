from config.urls.base_urls import urlpatterns as base_urlpatterns

development_urlpatterns: list[str] = [
    # 개발 환경 에서의 urls ...
]

urlpatterns = base_urlpatterns + development_urlpatterns
