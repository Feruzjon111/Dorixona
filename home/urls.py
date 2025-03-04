from django.conf.urls.static import static
from django.urls import path
from Dorixona import settings
from .views import HomeView, AboutView, ProductsView, ContactView, ProductCreateView, ProductDetailView,\
    ProductDeleteView, ProductUpdateView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("products/", ProductsView.as_view(), name="products"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("create/", ProductCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", ProductDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", ProductUpdateView.as_view(), name="update"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)