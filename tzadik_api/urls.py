from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_token_views
from django.urls import path, include
from tzadik_api import views


router = DefaultRouter(trailing_slash=False)
router.register(r'albums', views.AlbumView, 'album')
router.register(r'album-performers', views.AlbumPerformerView, 'albumperformer')
router.register(r'artists', views.ArtistView, 'artist')
router.register(r'artist-performers', views.ArtistPerformerView, 'artistperformer')
router.register(r'categories', views.CategoryView, 'category')
router.register(r'orders', views.OrderView, 'order')
router.register(r'performers', views.PerformerView, 'performer')
router.register(r'performer-instruments', views.PerformerInstrumentView, 'performerinstrument')
router.register(r'my-profile', views.ProfileView, 'profile')
# router.register(r'', views., '')

urlpatterns = [
    path('', include(router.urls)),
    path('login', auth_token_views.obtain_auth_token),
    path('register', views.register_user)
]
