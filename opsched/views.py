from django.shortcuts import render
from django.http.response import JsonResponse
#from django.core import serializers
from .models import OperationSchedule
import json
import logging

logger = logging.getLogger(__name__)

def get_all_operation_schedule(request):
	all_records = OperationSchedule.objects.all()
	logger.info(len(all_records))
	logger.info(type(all_records))
	logger.info(all_records)

	response_json = {}
	for record in all_records:
		response_json[str(record.get_operation_id())] = record.to_dic()
	return JsonResponse(response_json)

# serializersは文字列を返す。この場合、jsonスタイルの文字列を返すので使えない・・・。
#	all_record_list = serializers.serialize('json', all_records)
#	all_record_list = []
#	logger.info(all_record_list)
#	all_record_json = {}
#	logger.info(len(all_record_list))
#	i = 0
#	for record in all_record_list:
#		logger.info(record)
#		all_record_json[i] = record
#		i+=1

#	logger.info(all_record_json)
