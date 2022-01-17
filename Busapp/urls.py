
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from Busapp.views import inicio
from Busapp import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('perfil/<email>', views.perfil, name="perfil"),
    path('cerrando/', views.cerrando, name="cerrando"),
    path('editar/<email>', views.editar, name="editar"),
    path('movimientos/<email>', views.movimientos, name="movimientos"),
    path('PDF/<email>', views.PDF, name="PDF"),
    path('panel/', views.panel, name="panel"),
    path('Usu/', views.Usu, name="Usu"),
    path('Reporte/', views.Reporte, name="Reporte"),
    path('repostar/', views.repostar, name="repostar"),
    path('vista/', views.vista, name="vista"),
    path('grafico/', views.grafico, name="grafico"),
    path('detalle/<campo>', views.detalle, name="detalle"),
    path('reportedetalle/<campo>', views.reportedetalle, name="reportedetalle"),
    path('individual/<campo>', views.individual, name="individual"),
    path('reporteindi/<campo>', views.reporteindi, name="reporteindi"),
    path('indisu/<email>', views.indisu, name="indisu"),
    path('report/<email>', views.report, name="report"),
    path('eliminar/<email>', views.eliminar, name="eliminar"),
    path('eliminarindi/<email>', views.eliminarindi, name="eliminarindi"),
    path('politica', views.politica, name="politica"),
    path('reportlines/', views.reportlines, name="reportlines"),
    path('eliminarlinea/<nombre>', views.eliminarlinea, name="eliminarlinea"),
    path('lineasola/<nombre>', views.lineasola, name="lineasola"),
    path('reportesolo/<nombre>', views.reportesolo, name="reportesolo"),



    
    
  

]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)