from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('download/',include('app.urls')),
    path('download/',views.render_pdf_view),
    path('test/',views.CustomerListView.as_view()),
    path('pdf/<int:pk>/',views.customer_render_pdf,name='customers'),
]
