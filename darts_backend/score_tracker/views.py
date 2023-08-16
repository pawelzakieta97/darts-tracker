from django.shortcuts import render
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for task
from .serializers import ScoreSerializer
# Task model
from .models import Score
# Create your views here.

@csrf_exempt
def scores(request):
    '''
    List all task snippets
    '''
    if(request.method == 'GET'):
        # get all the tasks
        all_scores = Score.objects.all()
        # serialize the task data
        serializer = ScoreSerializer(all_scores, many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)


    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = ScoreSerializer(data=data)
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def score_detail(request, pk):
    try:
        # obtain the task with the passed id.
        score = Score.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)

    if (request.method == 'GET'):
        serializer = ScoreSerializer(score, many=False)
        return JsonResponse(serializer.data, status=200)

    elif (request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = ScoreSerializer(score, data=data)
        # check whether the sent information is okay
        # check whether the sent information is okay
        if (serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)

    elif (request.method == 'DELETE'):
        # delete the task
        score.delete()
        # return a no content response.
        return HttpResponse(status=204)