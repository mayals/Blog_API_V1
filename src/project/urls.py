from django.contrib import admin
from django.urls import path,include

# Simple JWT
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls',namespace='blog')),
    
    # ---- API ---------------------------
    path('api/',include('blog_api.urls',namespace='blog_api')),
    
    path('api-auth/', include('rest_framework.urls')), # login   # logout
    path('api/rest-auth/', include('rest_auth.urls')), #rest_password_reset_confirm  .....
    path('api/rest-auth/registration/',include('rest_auth.registration.urls')), #registeration


    # Simple JWTauthentication
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

]
