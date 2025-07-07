from django.db import models
from django.contrib.auth.models import User


# Datos de feriados simulados (mock) para cumplir con REQ06 ante la caída de la API externa.
# Esto hace que el sistema sea robusto y no dependa de un servicio externo.
# Lista de feriados para validación local.
FERIADOS = {
    '2024': [
        {'date': '2024-01-01', 'inalienable': True},
        {'date': '2024-03-29', 'inalienable': False},
        {'date': '2024-05-01', 'inalienable': True},
        {'date': '2024-09-18', 'inalienable': True},
        {'date': '2024-09-19', 'inalienable': True},
        {'date': '2024-10-31', 'inalienable': False},
        {'date': '2024-12-25', 'inalienable': True},
    ]
}

# REQ02: Modelo para Categorías
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre

# REQ02: Modelo para Lugares
class Lugar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Lugar"
        verbose_name_plural = "Lugares"

    def __str__(self):
        return self.nombre

# REQ02: Modelo para Profesores
class Profesor(models.Model):
    nombre_completo = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"

    def __str__(self):
        return self.nombre_completo

# Modelo principal para Talleres
class Taller(models.Model):
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('aceptado', 'Aceptado'),
        ('rechazado', 'Rechazado'),
    )

    nombre = models.CharField(max_length=100) # Corresponde a 'titulo' en la API
    descripcion = models.TextField()
    fecha = models.DateField()
    duracion_horas = models.DecimalField(max_digits=4, decimal_places=2)
    
    # REQ03: Campo de estado
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')
    observacion = models.TextField(blank=True, null=True) # Para justificar rechazos

    # REQ02: Relaciones con otros modelos
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, blank=True)
    lugar = models.ForeignKey(Lugar, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    # REQ04: Quién propone el taller (Junta de Vecinos)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='talleres_creados')

    class Meta:
        verbose_name = "Taller"
        verbose_name_plural = "Talleres"

    def __str__(self):
        return f"{self.nombre} - {self.fecha} ({self.get_estado_display()})"

    def save(self, *args, **kwargs):
        # REQ06: Lógica de feriados al crear un taller nuevo, usando datos locales (mock).
        if self._state.adding:
            year_str = str(self.fecha.year)
            # Consultamos nuestra lista local de feriados.
            feriados_del_ano = FERIADOS.get(year_str, [])
            fecha_taller_str = self.fecha.strftime('%Y-%m-%d')

            for feriado in feriados_del_ano:
                if feriado.get('date') == fecha_taller_str:
                    if feriado.get('inalienable') is True:
                        self.estado = 'rechazado'
                        self.observacion = "No se programan talleres en feriados irrenunciables."
                    else: # Feriado normal
                        categoria_obj = Categoria.objects.get(pk=self.categoria_id)
                        if categoria_obj.nombre != "Aire Libre":
                            self.estado = 'rechazado'
                            self.observacion = "Sólo se programan talleres al aire libre en feriados."
                    # Rompemos el bucle porque ya encontramos el feriado y aplicamos la regla.
                    break
        
        super().save(*args, **kwargs)
