from django.urls import path
from . import views

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('', views.index, name='home'),
    path('update/<int:post_id>', views.update_post, name='update'),
    path('delete/<int:post_id>', views.delete_post, name='delete'),

    path('api/posts/', views.posts_list_api),
    path('api/posts/add/', views.add_post_api),
    path('api/posts/<int:post_id>', views.post_detail_api, name="post"),
    path('api/posts/update/<int:post_id>/', views.update_post_api),

    # docs
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='api_docs'),

]
