import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class Departamento(Model):
    __tablename__ = 'departamento'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    descripcion = Column(String(255), nullable=True)

    def __repr__(self):
        return self.nombre


class Empleado(Model):
    __tablename__ = 'empleado'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    cargo = Column(String(100), nullable=True)
    ubicacion = Column(String(150), nullable=True)  # Ej: Bloque B - Oficina 204
    departamento_id = Column(Integer, ForeignKey('departamento.id'), nullable=False)
    departamento = relationship("Departamento")

    def __repr__(self):
        return f"{self.nombre} ({self.departamento.nombre if self.departamento else 'Sin Depto'})"


class Tecnico(Model):
    __tablename__ = 'tecnico'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    especialidad = Column(String(100), nullable=True)  # Ej: Redes, Hardware, Software
    disponible = Column(Boolean, default=True)

    def __repr__(self):
        return f"{self.nombre} - {self.especialidad or 'General'}"


class CategoriaFalla(Model):
    __tablename__ = 'categoria_falla'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    descripcion = Column(String(255), nullable=True)

    def __repr__(self):
        return self.nombre


class Ticket(Model):
    __tablename__ = 'ticket'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(150), nullable=False)
    descripcion = Column(Text, nullable=False)
    
    # Estados del ticket
    prioridad = Column(String(20), default='Media')
    prioridad_sugerida_ia = Column(String(20), nullable=True)
    estado = Column(String(20), default='Abierto')
    
    # Análisis e Integración IA (Groq API)
    sugerencia_ia = Column(Text, nullable=True)
    resumen_ia = Column(String(255), nullable=True)
    
    # Fechas para métricas y reportes
    fecha_creacion = Column(DateTime, default=datetime.datetime.now)
    fecha_resolucion = Column(DateTime, nullable=True)

    # Relaciones principales
    empleado_id = Column(Integer, ForeignKey('empleado.id'), nullable=False)
    empleado = relationship("Empleado")

    tecnico_id = Column(Integer, ForeignKey('tecnico.id'), nullable=True)
    tecnico = relationship("Tecnico")

    categoria_id = Column(Integer, ForeignKey('categoria_falla.id'), nullable=False)
    categoria = relationship("CategoriaFalla")

    def __repr__(self):
        return f"Ticket #{self.id} - {self.titulo} [{self.estado}]"


class HistorialTicket(Model):
    __tablename__ = 'historial_ticket'
    id = Column(Integer, primary_key=True)
    ticket_id = Column(Integer, ForeignKey('ticket.id'), nullable=False)
    ticket = relationship("Ticket")
    
    tecnico_id = Column(Integer, ForeignKey('tecnico.id'), nullable=True)
    tecnico = relationship("Tecnico")

    nota_diagnostico = Column(Text, nullable=False)
    estado_anterior = Column(String(20), nullable=True)
    estado_nuevo = Column(String(20), nullable=True)
    fecha_registro = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f"Avance Ticket #{self.ticket_id} ({self.fecha_registro.strftime('%d/%m/%Y %H:%M')})"
