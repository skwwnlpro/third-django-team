from config.urls.base_urls import urlpatterns as base_urlpatterns

production_urlpatterns: list[str] = [
    # production 환경 에서의 urls ...
]

urlpatterns = base_urlpatterns + production_urlpatterns
