from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .extensions import appbuilder          # <-- antes: from app import appbuilder
from .models import Departamento, Empleado, Tecnico, CategoriaFalla, Ticket, HistorialTicket

class DepartamentoModelView(ModelView):
    datamodel = SQLAInterface(Departamento)
    list_columns = ['id', 'nombre', 'descripcion']

class EmpleadoModelView(ModelView):
    datamodel = SQLAInterface(Empleado)
    list_columns = ['nombre', 'email', 'cargo', 'departamento', 'ubicacion']

class TecnicoModelView(ModelView):
    datamodel = SQLAInterface(Tecnico)
    list_columns = ['nombre', 'email', 'especialidad', 'disponible']

class CategoriaFallaModelView(ModelView):
    datamodel = SQLAInterface(CategoriaFalla)
    list_columns = ['id', 'nombre', 'descripcion']

class TicketModelView(ModelView):
    datamodel = SQLAInterface(Ticket)
    list_columns = ['id', 'titulo', 'prioridad', 'estado', 'empleado', 'tecnico', 'categoria', 'fecha_creacion']
    add_columns = ['titulo', 'descripcion', 'prioridad', 'empleado', 'categoria']
    edit_columns = ['titulo', 'descripcion', 'prioridad', 'estado', 'tecnico', 'sugerencia_ia']

class HistorialTicketModelView(ModelView):
    datamodel = SQLAInterface(HistorialTicket)
    list_columns = ['ticket', 'tecnico', 'nota_diagnostico', 'fecha_registro']

# Registrar las vistas dentro de la categoría "Help Desk" en el menú lateral
appbuilder.add_view(DepartamentoModelView, "Departamentos", icon="fa-building", category="Help Desk")
appbuilder.add_view(EmpleadoModelView, "Empleados", icon="fa-users", category="Help Desk")
appbuilder.add_view(TecnicoModelView, "Técnicos", icon="fa-wrench", category="Help Desk")
appbuilder.add_view(CategoriaFallaModelView, "Categorías de Falla", icon="fa-tags", category="Help Desk")
appbuilder.add_view(TicketModelView, "Tickets", icon="fa-ticket", category="Help Desk")
appbuilder.add_view(HistorialTicketModelView, "Historial de Tickets", icon="fa-history", category="Help Desk")