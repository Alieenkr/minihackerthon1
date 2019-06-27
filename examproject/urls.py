from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from editorweb import views as editorweb
from joinweb import views as joinweb

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', editorweb.home, name="home"),
    path('new/', editorweb.new, name="new"),
    # path('editorweb/summary/<int:person_id>/', editorweb.summary, name="summary"),
    path('editorweb/read/<int:post_id>/' , editorweb.read,name="read"),
    path('editorweb/renew/<int:post_id>/' , editorweb.renew , name="renew"),
    path('editorweb/update/<int:post_id>/' , editorweb.update, name="update"),
    path('editorweb/delete/<int:post_id>/' , editorweb.delete, name="delete"),
    path('joinweb/signup/', joinweb.signup, name='signup'),
    path('joinweb/login/', joinweb.login, name='login'),
    path('joinweb/logout/', joinweb.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
