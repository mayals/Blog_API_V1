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
    # admin 
    path('admin/', admin.site.urls),
    
    # blog
    path('blog', include('blog.urls', namespace='blog')),
    
    # blog_api
    path('blog_api/', include('blog_api.urls', namespace='blog_api')),
    
    #---------------------------------------------------- 

    # rest_framework
    path('rest_framework/', include('rest_framework.urls')),

    # login in small login box  but go automatically to http://127.0.0.1:8000/accounts/profile/!
    path('rest_framework/login/', include('rest_framework.urls')),
    path('rest_framework/logout/', include('rest_framework.urls')),   # logout then automatically go to admin logout page ! 

 
    ############## rest_auth ###################################
    path('rest_auth/', include('rest_auth.urls')), 
    
    # rest_password_reset
    # work ok but go to error page Password Reset Confirm  need Accepts the following POST parameters: token, uid,new_password1, new_password2
    path('rest_auth/password/reset/', include('rest_auth.urls')),
    # rest_password_reset_confirm
    # work ok but contain field token, uid,new_password1, new_password2 all required to full 
    path('rest_auth/password/reset/confirm/', include('rest_auth.urls')),
    # rest_login
    path('rest_auth/login/', include('rest_auth.urls')), # it is work ok go red page of django rest framework 
    # rest_logout
    path('rest_auth/logout/', include('rest_auth.urls')),  # it is work ok 
    # rest_user_details
    path('rest_auth/user/', include('rest_auth.urls')), # work ok display request user detail information
    # rest_password_change
    path('rest_auth/password/change/',include('rest_auth.urls')), # work ok  give 2 fields new pass new passconfirm to change password in the same page 
   
  
    

    ############## rest_auth.registration ###################################
    path('rest_auth/registration/',include('rest_auth.registration.urls')),  # work ok registeration ad give you long number name it kay !
    

    # SimpleJWT authentication
    path('token_obtain_pair/', TokenObtainPairView.as_view()), # work ok 
    path('token_refresh/', TokenRefreshView.as_view()), # work ok 

    # schema
    # path('api/schema/', schema_view),
    
    
    # swagger
    path('swagger-docs/', schema_view),


    # Documentation
    path('api/docs/', include_docs_urls(title=API_TITLE,description=API_DESCRIPTION)),
   
]
