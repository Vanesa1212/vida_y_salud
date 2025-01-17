# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class FacMTarjetero(models.Model):
    historia = models.CharField(unique=True, max_length=20, db_comment='N·mero de historia clÝnica')
    id_persona = models.OneToOneField('GenMPersona', models.DO_NOTHING, db_column='id_persona', db_comment='Identificador de la persona')
    id_regimen = models.ForeignKey('GenPListaopcion', models.DO_NOTHING, db_column='id_regimen', db_comment='Identificador del regimen de afiliaci¾n de la persona.  Variable: RegSegSocial')
    id_eps = models.ForeignKey('GenPEps', models.DO_NOTHING, db_column='id_eps', blank=True, null=True, db_comment='Identificador de la EPS/ERP')
    id_nivel = models.ForeignKey('FacPNivel', models.DO_NOTHING, db_column='id_nivel', blank=True, null=True, db_comment='Identificador del nivel de recuperaci¾n')

    class Meta:
        managed = False
        db_table = 'fac_m_tarjetero'


class FacPCups(models.Model):
    codigo = models.CharField(unique=True, max_length=8, db_comment='C¾digo CUPS de la tecnologÝa en salud')
    nombre = models.CharField(max_length=500, db_comment='Nombre de la tecnologÝa en salud')
    habilita = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fac_p_cups'


class FacPNivel(models.Model):
    id_eps = models.ForeignKey('GenPEps', models.DO_NOTHING, db_column='id_eps', db_comment='Identificador de la EPS/ERP')
    nivel = models.CharField(max_length=4, db_comment='Nivel de recuperaci¾n')
    nombre = models.CharField(max_length=50, db_comment='Nombre del nivel de recuperaci¾n')
    id_regimen = models.ForeignKey('GenPListaopcion', models.DO_NOTHING, db_column='id_regimen', db_comment='Identificador del regÝmen de seguridad social. Variable: RegSegSocial')

    class Meta:
        managed = False
        db_table = 'fac_p_nivel'
        unique_together = (('id_eps', 'nivel'),)


class FacPProfesional(models.Model):
    codigo = models.CharField(unique=True, max_length=4, db_comment='C¾digo del profesional')
    id_persona = models.ForeignKey('GenMPersona', models.DO_NOTHING, db_column='id_persona', blank=True, null=True, db_comment='Identificador de la persona')
    registro_medico = models.CharField(max_length=20, blank=True, null=True, db_comment='N·mero del registro mÚdico del profesional')
    id_tipo_prof = models.ForeignKey('GenPListaopcion', models.DO_NOTHING, db_column='id_tipo_prof', blank=True, null=True, db_comment='Identificador del tipo de profesional. Variable: TipoProf')

    class Meta:
        managed = False
        db_table = 'fac_p_profesional'


class GenMPersona(models.Model):
    id_tipoid = models.ForeignKey('GenPListaopcion', models.DO_NOTHING, db_column='id_tipoid', db_comment='Identificador para el tipo de identificaci¾n de la persona. Variable: TipoIdentificacion')
    numeroid = models.CharField(max_length=20, db_comment='N·mero de identificaci¾n de la persona')
    apellido1 = models.CharField(max_length=20, db_comment='Primer apellido de la persona')
    apellido2 = models.CharField(max_length=20, db_comment='Segundo apellido de la persona')
    nombre1 = models.CharField(max_length=20, db_comment='Primer nombre de la persona')
    nombre2 = models.CharField(max_length=20, db_comment='Segundo nombre de la persona')
    fechanac = models.DateField(blank=True, null=True, db_comment='Fecha de nacimiento')
    id_sexobiologico = models.ForeignKey('GenPListaopcion', models.DO_NOTHING, db_column='id_sexobiologico', related_name='genmpersona_id_sexobiologico_set', blank=True, null=True, db_comment='Identificador del sexo biol¾gico al nacer. Variable: SexoBiologico')
    direccion = models.CharField(max_length=250, blank=True, null=True, db_comment='Direcci¾n de residencia')
    tel_movil = models.CharField(max_length=10, blank=True, null=True, db_comment='TelÚfono m¾vil')
    email = models.CharField(max_length=250, blank=True, null=True, db_comment='Correo electr¾nico')

    class Meta:
        managed = False
        db_table = 'gen_m_persona'

    def __str__(self):
        return f"{self.nombre1} {self.apellido1} - {self.numeroid}"


class GenPDocumento(models.Model):
    codigo = models.CharField(unique=True, max_length=4, db_comment='C¾digo del documento')
    nombre = models.CharField(max_length=254, db_comment='Nombre del documento')
    habilita = models.BooleanField(db_comment='Documento habilitado para su uso en el sistema')

    class Meta:
        managed = False
        db_table = 'gen_p_documento'


class GenPEps(models.Model):
    codigo = models.CharField(unique=True, max_length=8, db_comment='C¾digo de la EPS/ERP')
    razonsocial = models.CharField(max_length=250, db_comment='Nombre de la EPS/ERP')
    nit = models.CharField(max_length=20, blank=True, null=True, db_comment='Nit')
    habilita = models.BooleanField(db_comment='Habilitada para su uso en el sistema')

    class Meta:
        managed = False
        db_table = 'gen_p_eps'


class GenPListaopcion(models.Model):
    variable = models.CharField(max_length=50, db_comment='Variable de grupo de opciones')
    descripcion = models.CharField(max_length=100, db_comment='Descripci¾n del grupo de opciones')
    valor = models.SmallIntegerField(db_comment='Valor de la opci¾n')
    nombre = models.CharField(max_length=100, db_comment='Nombre de la opci¾n')
    abreviacion = models.CharField(max_length=10, db_comment='Abreviaci¾n para la opcion')
    habilita = models.BooleanField(db_comment='Opci¾n habilitada para su uso en el sistema')

    class Meta:
        managed = False
        db_table = 'gen_p_listaopcion'
        unique_together = (('variable', 'valor'),)


class LabMOrden(models.Model):
    id_documento = models.ForeignKey(GenPDocumento, models.DO_NOTHING, db_column='id_documento', blank=True, null=True, db_comment='Identificador del documento que respalda la orden de laboratorio')
    orden = models.DecimalField(max_digits=10, decimal_places=0, db_comment='N·mero de la orden de laboratorio')
    fecha = models.DateTimeField(db_comment='Fecha de emisi¾n de la orden de laboratorio')
    id_historia = models.ForeignKey(FacMTarjetero, models.DO_NOTHING, db_column='id_historia', blank=True, null=True, db_comment='Identificador del n·mero de historia clÝnica')
    id_profesional_ordena = models.ForeignKey(FacPProfesional, models.DO_NOTHING, db_column='id_profesional_ordena', blank=True, null=True, db_comment='Identificador del profesional tratante')
    profesional_externo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'lab_m_orden'
        unique_together = (('id_documento', 'orden'),)


class LabMOrdenResultados(models.Model):
    fecha = models.DateTimeField(blank=True, null=True, db_comment='Fecha de procesamiento de la prueba')
    id_orden = models.ForeignKey(LabMOrden, models.DO_NOTHING, db_column='id_orden', db_comment='Identificador de la orden de laboratorio')
    id_procedimiento = models.ForeignKey('LabPProcedimientos', models.DO_NOTHING, db_column='id_procedimiento', db_comment='Identificador del procedimiento de laboratorio')
    id_prueba = models.ForeignKey('LabPPruebas', models.DO_NOTHING, db_column='id_prueba', db_comment='Identificador del c¾digo de prueba')
    id_pruebaopcion = models.ForeignKey('LabPPruebasOpciones', models.DO_NOTHING, db_column='id_pruebaopcion', blank=True, null=True, db_comment='Identificador de la opci¾n de la prueba')
    res_opcion = models.CharField(max_length=250, blank=True, null=True, db_comment='Resultado: Opci¾n m·ltiple')
    res_numerico = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True, db_comment='Resultado n·merico de la prueba')
    res_texto = models.CharField(max_length=60, blank=True, null=True, db_comment='Resultado: texto corto')
    res_memo = models.CharField(max_length=2500, blank=True, null=True, db_comment='Resultado: Texto largo')
    num_procesamientos = models.IntegerField(blank=True, null=True, db_comment='N·mero de procesamientos')

    class Meta:
        managed = False
        db_table = 'lab_m_orden_resultados'


class LabPGrupos(models.Model):
    codigo = models.CharField(unique=True, max_length=2, db_comment='C¾digo del grupo de laboratorio')
    nombre = models.CharField(unique=True, max_length=60, db_comment='Nombre del grupo de examenes de laborario')
    habilita = models.BooleanField(db_comment='Habilitado para su uso en el sistema')

    class Meta:
        managed = False
        db_table = 'lab_p_grupos'


class LabPProcedimientos(models.Model):
    id_cups = models.OneToOneField(FacPCups, models.DO_NOTHING, db_column='id_cups', db_comment='Identificador para tecnologÝa en salud')
    id_grupo_laboratorio = models.ForeignKey(LabPGrupos, models.DO_NOTHING, db_column='id_grupo_laboratorio', db_comment='Identificador del grupo de examenes de laboratorio')
    metodo = models.CharField(max_length=60, blank=True, null=True, db_comment='Metodo bajo el cual se realiza el procedimiento')

    class Meta:
        managed = False
        db_table = 'lab_p_procedimientos'


class LabPPruebas(models.Model):
    id_procedimiento = models.ForeignKey(LabPProcedimientos, models.DO_NOTHING, db_column='id_procedimiento', db_comment='TecnologÝa en salud de laboratorio clÝnico sobre el que se definen las pruebas')
    codigo_prueba = models.CharField(max_length=6, db_comment='C¾digo de la prueba')
    nombre_prueba = models.CharField(max_length=200, db_comment='Nombre de la prueba')
    id_tipo_resultado = models.ForeignKey(GenPListaopcion, models.DO_NOTHING, db_column='id_tipo_resultado', db_comment='Variable: TipoResultado')
    unidad = models.CharField(max_length=20, db_comment='Unidad bajo la cual se expresa el resultado')
    habilita = models.BooleanField(blank=True, null=True, db_comment='Habilitada para su uso en el sistema')

    class Meta:
        managed = False
        db_table = 'lab_p_pruebas'
        unique_together = (('id_procedimiento', 'codigo_prueba'),)


class LabPPruebasOpciones(models.Model):
    id_prueba = models.ForeignKey(LabPPruebas, models.DO_NOTHING, db_column='id_prueba', db_comment='Identificador del c¾digo de procedimiento y la prueba')
    opcion = models.CharField(max_length=250, db_comment='Opci¾n de selecci¾n m·ltiple')
    valor_ref_min_f = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, db_comment='Valor de referencia mÝnimo para gÚnero femenino')
    valor_ref_max_f = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, db_comment='Valor de referencia mßximo para gÚnero femenino')
    valor_ref_min_m = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, db_comment='Valor de referencia mÝnimo para gÚnero masculino')
    valor_ref_max_m = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, db_comment='Valor de referencia mßximo para gÚnero masculino')

    class Meta:
        managed = False
        db_table = 'lab_p_pruebas_opciones'
        unique_together = (('id_prueba', 'opcion'),)
