from django.db import models
from django.utils import timezone

class OperationSchedule(models.Model):
	operation_name = models.CharField(max_length=255)
	patient_name = models.CharField(max_length=20)
	operation_start_time = models.DateTimeField(default=timezone.now)
	operation_finish_estimation_time = models.DateTimeField(default=timezone.now)
	file_path = models.FilePathField(path="/Users/Kiichiro/djangogirls")

	def __str__(self):
		return self.operation_name

