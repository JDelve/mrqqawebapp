from django.db import models
from django.utils import timezone


class AuthGroup(models.Model):
	name = models.CharField(unique=True, max_length=80)

	class Meta:
		db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
	group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
	permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

	class Meta:
		db_table = 'auth_group_permissions'
		unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
	name = models.CharField(max_length=255)
	content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
	codename = models.CharField(max_length=100)

	class Meta:
		db_table = 'auth_permission'
		unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
	password = models.CharField(max_length=128)
	last_login = models.DateTimeField(blank=True, null=True)
	is_superuser = models.IntegerField()
	username = models.CharField(unique=True, max_length=150)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.CharField(max_length=254)
	is_staff = models.IntegerField()
	is_active = models.IntegerField()
	date_joined = models.DateTimeField()

	class Meta:
		db_table = 'auth_user'


class AuthUserGroups(models.Model):
	user = models.ForeignKey(AuthUser, models.DO_NOTHING)
	group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

	class Meta:
		db_table = 'auth_user_groups'
		unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
	user = models.ForeignKey(AuthUser, models.DO_NOTHING)
	permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

	class Meta:
		db_table = 'auth_user_user_permissions'
		unique_together = (('user', 'permission'),)

################################################################################

class ScannerDetails(models.Model):
	scanner_id = models.IntegerField(primary_key=True)
	scanner_name = models.CharField(max_length=100, blank=True, null=True)
	scanner_notes = models.CharField(max_length=8000, blank=True, null=True)

	class Meta:
		db_table = 'scanner_details'
	pass
	def __int__(self):
		return self.scanner_id
	def __int__(self):
		return self.scanner_name
	def __int__(self):
		return self.scanner_notes

class VersionDetails(models.Model):
	version_id = models.IntegerField(primary_key=True)
	version_name = models.CharField(max_length=100)
	version_notes = models.CharField(max_length=8000)

	class Meta:
		db_table = 'version_details'
	pass
	def __int__(self):
		return self.version_id
	def __int__(self):
		return self.version_name
	def __int__(self):
		return self.version_notes

class GradsysDetails(models.Model):
	gradsys_id = models.IntegerField(primary_key=True)
	gradsys_name = models.CharField(max_length=100)
	gradsys_notes = models.CharField(max_length=8000)

	class Meta:
		db_table = 'gradsys_details'
	pass
	def __int__(self):
		return self.gradsys_id
	def __int__(self):
		return self.gradsys_name
	def __int__(self):
		return self.gradsys_notes

class CoilDetails(models.Model):
	coil_id = models.IntegerField(primary_key=True)
	coil_name = models.CharField(max_length=100)
	coil_notes = models.CharField(max_length=8000)

	class Meta:
		db_table = 'coil_details'
	pass
	def __int__(self):
		return self.coil_id
	def __int__(self):
		return self.coil_name
	def __int__(self):
		return self.coil_notes

class PhantomDetails(models.Model):
	phantom_id = models.IntegerField(primary_key=True)
	phantom_name = models.CharField(max_length=100)
	phantom_notes = models.CharField(max_length=8000)

	class Meta:
		db_table = 'phantom_details'
	pass
	def __int__(self):
		return self.phantom_id
	def __int__(self):
		return self.phantom_name
	def __int__(self):
		return self.phantom_notes

class DateDetails(models.Model):
	date_id = models.IntegerField(primary_key=True)
	full_date = models.DateField()
	scanner = models.ForeignKey('ScannerDetails', models.CASCADE)
	version = models.ForeignKey('VersionDetails', models.CASCADE)
	gradsys = models.ForeignKey('GradsysDetails', models.CASCADE)
	coil = models.ForeignKey('CoilDetails', models.CASCADE)
	phantom = models.ForeignKey('PhantomDetails', models.CASCADE)

	class Meta:
		db_table = 'date_details'
	pass
	def __int__(self):
		return self.date_id
	def __int__(self):
		return self.full_date
	def __int__(self):
		return self.scanner_id
	def __int__(self):
		return self.version_id
	def __int__(self):
		return self.gradsys_id
	def __int__(self):
		return self.coil_id
	def __int__(self):
		return self.phantom_id

class SeriesDetails(models.Model):
	series_id = models.IntegerField(primary_key=True)
	series = models.CharField(max_length=100)
	series_notes = models.CharField(max_length=8000)

	class Meta:
		db_table = 'series_details'
	pass
	def __int__(self):
		return self.series_id
	def __int__(self):
		return self.series
	def __int__(self):
		return self.series_notes

class Results(models.Model):
	result_id = models.IntegerField(primary_key=True)
	result = models.CharField(max_length=100)
	date = models.ForeignKey('DateDetails', models.CASCADE)
	series = models.ForeignKey('SeriesDetails', models.CASCADE)

	class Meta:
		db_table = 'results'
	pass
	def __int__(self):
		return self.result_id
	def __int__(self):
		return self.result
	def __int__(self):
		return self.date_id
	def __int__(self):
		return self.series

#################################################################

class DjangoAdminLog(models.Model):
	action_time = models.DateTimeField()
	object_id = models.TextField(blank=True, null=True)
	object_repr = models.CharField(max_length=200)
	action_flag = models.SmallIntegerField()
	change_message = models.TextField()
	content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
	user = models.ForeignKey(AuthUser, models.DO_NOTHING)

	class Meta:
		db_table = 'django_admin_log'


class DjangoContentType(models.Model):
	app_label = models.CharField(max_length=100)
	model = models.CharField(max_length=100)

	class Meta:
		db_table = 'django_content_type'
		unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
	app = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	applied = models.DateTimeField()

	class Meta:
		db_table = 'django_migrations'


class DjangoSession(models.Model):
	session_key = models.CharField(primary_key=True, max_length=40)
	session_data = models.TextField()
	expire_date = models.DateTimeField()

	class Meta:
		db_table = 'django_session'
