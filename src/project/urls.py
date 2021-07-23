from django.contrib import admin
from django.urls import path,include

# Simple JWT
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls',namespace='blog')),
    
    #API
    path('api/',include('blog_api.urls',namespace='blog_api')),
    
    path('api-auth/', include('rest_framework.urls')),

    # Simple JWT authentication
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
