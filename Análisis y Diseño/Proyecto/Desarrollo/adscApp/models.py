# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alimento(models.Model):
    id_alimento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    calorias = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alimento'


class AlimentoPlan(models.Model):
    id_plan = models.OneToOneField('Planalimenticio', models.DO_NOTHING, db_column='id_plan', primary_key=True)  # The composite primary key (id_plan, id_alimento) found, that is not supported. The first column is selected.
    id_alimento = models.ForeignKey(Alimento, models.DO_NOTHING, db_column='id_alimento')

    class Meta:
        managed = False
        db_table = 'alimento_plan'
        unique_together = (('id_plan', 'id_alimento'),)


class Asesor(models.Model):
    id_asesor = models.AutoField(primary_key=True)
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    especialidad = models.CharField(max_length=255, blank=True, null=True)
    experiencia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asesor'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Catalogoroles(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogoRoles'


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    objetivo = models.CharField(max_length=255, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    id_asesor = models.ForeignKey(Asesor, models.DO_NOTHING, db_column='id_asesor', blank=True, null=True)
    id_plan = models.ForeignKey('Planalimenticio', models.DO_NOTHING, db_column='id_plan', blank=True, null=True)
    id_rutina = models.ForeignKey('Rutina', models.DO_NOTHING, db_column='id_rutina', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Datoscorporales(models.Model):
    id_datos = models.AutoField(primary_key=True)
    id_asesor = models.ForeignKey(Asesor, models.DO_NOTHING, db_column='id_asesor', blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    altura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    imc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datoscorporales'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ejercicio(models.Model):
    id_ejercicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    duracion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ejercicio'


class EjercicioRutina(models.Model):
    id_rutina = models.OneToOneField('Rutina', models.DO_NOTHING, db_column='id_rutina', primary_key=True)  # The composite primary key (id_rutina, id_ejercicio) found, that is not supported. The first column is selected.
    id_ejercicio = models.ForeignKey(Ejercicio, models.DO_NOTHING, db_column='id_ejercicio')

    class Meta:
        managed = False
        db_table = 'ejercicio_rutina'
        unique_together = (('id_rutina', 'id_ejercicio'),)


class MainServicio(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=150)
    detail = models.TextField()

    class Meta:
        managed = False
        db_table = 'main_servicio'


class Planalimenticio(models.Model):
    id_plan = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    id_asesor = models.ForeignKey(Asesor, models.DO_NOTHING, db_column='id_asesor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'planalimenticio'


class Registroalimenticio(models.Model):
    id_registro = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_alimento = models.ForeignKey(Alimento, models.DO_NOTHING, db_column='id_alimento', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registroalimenticio'


class Registroejercicio(models.Model):
    id_registro = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_ejercicio = models.ForeignKey(Ejercicio, models.DO_NOTHING, db_column='id_ejercicio', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    duracion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registroejercicio'


class Reporteprogreso(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    id_entrenador = models.ForeignKey(Asesor, models.DO_NOTHING, db_column='id_entrenador', blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reporteprogreso'


class Rutina(models.Model):
    id_rutina = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    id_asesor = models.ForeignKey(Asesor, models.DO_NOTHING, db_column='id_asesor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rutina'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    ap_paterno = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    contrasena = models.CharField(max_length=255, blank=True, null=True)
    rol = models.ForeignKey(Catalogoroles, models.DO_NOTHING, db_column='rol', blank=True, null=True)
    ap_materno = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class Valorescorporalesobjetivo(models.Model):
    id_valores = models.AutoField(primary_key=True)
    id_asesor = models.ForeignKey(Asesor, models.DO_NOTHING, db_column='id_asesor', blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    pesoobjetivo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    imcobjetivo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'valorescorporalesobjetivo'
