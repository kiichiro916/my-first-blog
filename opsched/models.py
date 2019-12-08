from django.db import models
from django.utils import timezone
import uuid

class OperationSchedule(models.Model):
	operation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#	operation_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
	operation_name = models.CharField(max_length=255)
	patient_name = models.CharField(max_length=20)
	operation_start_time = models.DateTimeField(default=timezone.now)
	operation_finish_estimation_time = models.DateTimeField(default=timezone.now)
	file_path = models.FilePathField(path="/", null=True)

	def get_operation_id(self):
		return self.operation_id

	def to_dic(self):
		return {"operation_name": self.operation_name,
				"patient_name": self.patient_name,
				"operation_start_time": self.operation_start_time,
				"operation_finish_estimation_time": self.operation_finish_estimation_time,
				"file_path": self.file_path,}

	def __str__(self):
		return self.operation_name

