# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
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
    action_flag = models.PositiveSmallIntegerField()
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


class Unyou(models.Model):
    lbc = models.CharField(db_column='LBC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    main_lbc = models.CharField(db_column='Main_LBC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    parent_lbc = models.CharField(db_column='Parent_LBC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    group_top_lbc1 = models.CharField(db_column='group_top_LBC1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    group_lbc1 = models.CharField(db_column='group_LBC1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    group_lbc2 = models.CharField(db_column='group_LBC2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    group_lbc3 = models.CharField(db_column='group_LBC3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    group_lbc_id1 = models.CharField(db_column='group_LBC_id1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    group_lbc_id2 = models.CharField(db_column='group_LBC_id2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    group_lbc_id3 = models.CharField(db_column='group_LBC_id3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    listing_id = models.CharField(db_column='Listing_id', max_length=100, blank=True, null=True)  # Field name made lowercase.
    listing_name = models.CharField(db_column='Listing_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ticker_symbol = models.CharField(db_column='Ticker_symbol', max_length=100, blank=True, null=True)  # Field name made lowercase.
    periodic_report_number = models.CharField(max_length=100, blank=True, null=True)
    company_status_id = models.CharField(max_length=100, blank=True, null=True)
    company_status_name = models.CharField(max_length=100, blank=True, null=True)
    office_status_id = models.CharField(max_length=100, blank=True, null=True)
    office_status_name = models.CharField(max_length=100, blank=True, null=True)
    merged_lbc = models.CharField(db_column='merged_LBC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bankruptcy_date = models.DateField(blank=True, null=True)
    legal_personality = models.IntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    legal_personality_place = models.CharField(max_length=100, blank=True, null=True)
    company_name_sub = models.CharField(max_length=100, blank=True, null=True)
    office_name = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=100, blank=True, null=True)
    prefectures_id = models.CharField(max_length=100, blank=True, null=True)
    municipality_id = models.CharField(max_length=100, blank=True, null=True)
    prefectures_name = models.CharField(max_length=100, blank=True, null=True)
    municipality_name = models.CharField(max_length=100, blank=True, null=True)
    town_name = models.CharField(max_length=100, blank=True, null=True)
    city_block = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    building = models.CharField(max_length=100, blank=True, null=True)
    telephone_number = models.CharField(max_length=100, blank=True, null=True)
    fax_number = models.CharField(max_length=100, blank=True, null=True)
    offices_number = models.CharField(max_length=100, blank=True, null=True)
    establishment_year = models.DateTimeField()
    capital = models.CharField(max_length=100, blank=True, null=True)
    employee_number = models.CharField(max_length=100, blank=True, null=True)
    current_term_settlement = models.CharField(max_length=100, blank=True, null=True)
    sales_current_term = models.CharField(max_length=100, blank=True, null=True)
    sales_ratio = models.CharField(max_length=100, blank=True, null=True)
    profit_term = models.IntegerField(db_column='Profit_term', blank=True, null=True)  # Field name made lowercase.
    profit_ratio = models.CharField(max_length=100, blank=True, null=True)
    dividend_term = models.CharField(max_length=100, blank=True, null=True)
    representative_position = models.CharField(db_column='Representative_position', max_length=100, blank=True, null=True)  # Field name made lowercase.
    representatives_name = models.CharField(db_column='Representatives_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    representatives_name_sub = models.CharField(db_column='Representatives_name_sub', max_length=100, blank=True, null=True)  # Field name made lowercase.
    industry_id1 = models.IntegerField(db_column='Industry_id1', blank=True, null=True)  # Field name made lowercase.
    industry_name1 = models.CharField(max_length=100, blank=True, null=True)
    industry_id2 = models.IntegerField(db_column='Industry_id2', blank=True, null=True)  # Field name made lowercase.
    industry_name2 = models.CharField(max_length=100, blank=True, null=True)
    industry_id3 = models.IntegerField(db_column='Industry_id3', blank=True, null=True)  # Field name made lowercase.
    industry_name3 = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(db_column='URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telephone_call_check = models.CharField(max_length=100, blank=True, null=True)
    relocation_number = models.CharField(db_column='Relocation_number', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fax_call_check = models.CharField(max_length=100, blank=True, null=True)
    relocation_fax = models.CharField(max_length=100, blank=True, null=True)
    company_type_id = models.CharField(max_length=100, blank=True, null=True)
    company_type_name = models.CharField(max_length=100, blank=True, null=True)
    foreign_owned_id = models.CharField(db_column='Foreign_owned_id', max_length=100, blank=True, null=True)  # Field name made lowercase.
    survey_date = models.DateField(db_column='Survey_date', blank=True, null=True)  # Field name made lowercase.
    number_of_employees = models.IntegerField(blank=True, null=True)
    sales = models.CharField(max_length=100, blank=True, null=True)
    profit = models.CharField(max_length=100, blank=True, null=True)
    overseas_expansion_company = models.CharField(db_column='Overseas_expansion_company', max_length=100, blank=True, null=True)  # Field name made lowercase.
    a = models.IntegerField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    b = models.IntegerField(db_column='B', blank=True, null=True)  # Field name made lowercase.
    c = models.IntegerField(db_column='C', blank=True, null=True)  # Field name made lowercase.
    d = models.IntegerField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    e = models.IntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    f = models.IntegerField(db_column='F', blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    i = models.IntegerField(db_column='I', blank=True, null=True)  # Field name made lowercase.
    j = models.IntegerField(db_column='J', blank=True, null=True)  # Field name made lowercase.
    k = models.IntegerField(db_column='K', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    sub11 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unyou'
