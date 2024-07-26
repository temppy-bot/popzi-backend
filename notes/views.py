from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .utils.open_ai import query_openai
from .models import Note
from problems.views import create_problems
import json
@csrf_exempt
def create_note(request):
	if request.method == 'POST':
		# try:
			content = json.loads(request.body)
			response = query_openai(content['content'])
			note = Note(content=content['content'])
			note.save()
			print(response)
			create_problems(response, note.pk)
			return JsonResponse({'message': 'successful', 'content': response})
		# except:
		# 	return HttpResponse('Something went wrong.', status=400)
