from django.shortcuts import render
from .models import *
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from rest_framework.serializers import ModelSerializer, SerializerMethodField

# Create your views here.

@require_GET
@csrf_exempt
def users_data(request):
    users_data=User.objects.all()

    response={}

    class UserSerializer(ModelSerializer):
        activity_periods = SerializerMethodField()
        id = serializers.CharField(source='user_id')
        real_name = serializers.CharField(source='name')
        tz = serializers.CharField(source='address')
        
        class Meta:
            model = User
            depth = 1
            fields = ['id', 'real_name', 'tz', 'activity_periods']

        def get_activity_periods(self, user):
            ''' gets the pending appointments for the given clinician '''
            context=[]

            use = user.activity_user.all()
            for us in use:
                x={}
                x['start_time'] = us.start_time.strftime('%b %d %Y %I:%M %p')
                x['end_time'] = us.end_time.strftime('%b %d %Y %I:%M %p')
                context.append(x)
            return context

    user_serializer = UserSerializer(users_data,many=True).data

    # response['user_serializer'] = user_serializer

    return JsonResponse({
        'ok' : True,
        'Members' : user_serializer,
        })
