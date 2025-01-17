# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApphorariosActividad(models.Model):
    id_actividad = models.AutoField(primary_key=True)
    nombre_actividad = models.CharField(max_length=1500)

    class Meta:
        managed = False
        db_table = 'apphorarios_actividad'


class ApphorariosAmbientes(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_ambiente = models.CharField(max_length=50)
    zona = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'apphorarios_ambientes'


class ApphorariosCompetenciaAprendizaje(models.Model):
    id_competencia = models.AutoField(primary_key=True)
    nombre_competencia = models.CharField(max_length=1500)
    codigo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'apphorarios_competencia_aprendizaje'


class ApphorariosFichas(models.Model):
    id = models.BigAutoField(primary_key=True)
    programa_de_formacion = models.CharField(max_length=1500)
    numero = models.CharField(max_length=50)
    jefe_ficha = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    jornada_de_ficha = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'apphorarios_fichas'


class ApphorariosInstructor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    programa_de_formacion = models.CharField(max_length=10)
    tipo_instructor = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'apphorarios_instructor'


class ApphorariosResultadoAprendizaje(models.Model):
    id_resultado = models.AutoField(primary_key=True)
    nombre_resultado = models.CharField(max_length=1500)
    actividad = models.ForeignKey(ApphorariosActividad, models.DO_NOTHING)
    competencia = models.ForeignKey(ApphorariosCompetenciaAprendizaje, models.DO_NOTHING)
    trimestres = models.ForeignKey('ApphorariosTrimestres', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apphorarios_resultado_aprendizaje'


class ApphorariosTrimestres(models.Model):
    id = models.BigAutoField(primary_key=True)
    trimestres = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'apphorarios_trimestres'


class ApphorariosUsuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    is_instructor = models.IntegerField()
    is_coordinador = models.IntegerField()
    is_jgrupo = models.IntegerField(db_column='is_JGrupo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'apphorarios_usuario'


class ApphorariosUsuarioGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(ApphorariosUsuario, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apphorarios_usuario_groups'
        unique_together = (('usuario', 'group'),)


class ApphorariosUsuarioUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(ApphorariosUsuario, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apphorarios_usuario_user_permissions'
        unique_together = (('usuario', 'permission'),)


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(ApphorariosUsuario, models.DO_NOTHING)

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


class Filtros(models.Model):
    id_resultado = models.IntegerField()
    nombre_resultado = models.CharField(max_length=1500)
    actividad_id = models.IntegerField()
    competencia_id = models.IntegerField()
    trimestres_id = models.BigIntegerField()
    id_competencia = models.IntegerField()
    nombre_competencia = models.CharField(max_length=1500)
    codigo = models.IntegerField()
    id = models.BigIntegerField()
    trimestres = models.CharField(max_length=3)
    id_actividad = models.IntegerField()
    nombre_actividad = models.CharField(max_length=1500)

    class Meta:
        managed = False
        db_table = 'filtros'
