from django.contrib import admin
from django.urls import path,include

# Simple JWT
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# schema
# from rest_framework.schemas import get_schema_view

# swagger
from rest_framework_swagger.views import get_swagger_view


# documentation 
from rest_framework.documentation import include_docs_urls


API_TITLE = 'Blog API'
API_DESCRIPTION = 'A Web API for creating and editing blog posts.'
# schema_view = get_schema_view(title=API_TITLE)
schema_view = get_swagger_view(title=API_TITLE)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls',namespace='blog')),
    
    # ---- API ---------------------------
    path('api/',include('blog_api.urls',namespace='blog_api')),
    
    path('api-auth/', include('rest_framework.urls')), # login   # logout
    path('api/rest-auth/', include('rest_auth.urls')), #rest_password_reset_confirm  .....
    path('api/rest-auth/registration/',include('rest_auth.registration.urls')), #registeration

    # SimpleJWT authentication
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

    # schema
    # path('api/schema/', schema_view),
    
    
    # swagger
    path('swagger-docs/', schema_view),


    # Documentation
    path('api/docs/', include_docs_urls(title=API_TITLE,description=API_DESCRIPTION)),
   
]
