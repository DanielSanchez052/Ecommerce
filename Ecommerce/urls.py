from django.conf import settings 
from django.conf.urls import handler400, handler403, handler404, handler500, include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('dashboard/product/', include(('apps.products.dashboard.urls','products'))),
    path('accouts/', include(('apps.user.dashboard.urls','users'))), 
    path('', include(('apps.core.urls','core')))

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400='apps.core.views.handleErrors.handle400'
handler403='apps.core.views.handleErrors.handle403' 
handler404='apps.core.views.handleErrors.handle404'
handler500='apps.core.views.handleErrors.handle500'