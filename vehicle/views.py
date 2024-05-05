from django.shortcuts import render
from rest_framework import generics 
import requests 
from rest_framework.response import Response
import json
from database.models import *
from .database_opertaions import *
import time
from .utils import *
# Create your views here.


class DeviceDetailsView(generics.GenericAPIView):

    def get(self, request):
        refresh_token = refresh_access_token()
        response = get_device_Data(refresh_token)
        if response.status_code == 200:
            devices_data = json.loads(response.content).get('data')
            
            device_locations = []
            deviceStatus_details = []
            canInfo_details = []
            alerts_details = []
            todaysDrive_details = []
            links_details = []
            dinputs_details = []

            for data in devices_data:
                device_id = data.get("id")


                if "deviceDetails" in data:
                    create_device_object(data)
                
                
                try:
                    if "active" in data and "status" in data:
                        deviceStatus_details.append(create_device_status(device_id, data))
                    else:
                        deviceStatus_details.append(create_device_status(device_id, data))
                except:
                    print("Error creating device status")
                    pass
                

                if "location" in data:
                    device_locations.append(create_device_location(device_id, data))
                if "canInfo" in data:
                    canInfo_details.append(create_canInfo_object(device_id, data))
                if "alerts" in data:
                    alerts_details.append(create_alerts_object(device_id, data))
                if "todaysDrive" in data:
                    todaysDrive_details.append(create_todaysDrive_object(device_id, data))
                if "links" in data:
                    links_details.append(create_links_object(device_id, data))
                if "dinputs" in data:
                    dinputs_details.append(create_dinputs_objects(device_id, data))

            location_object = deviceLocation.objects.bulk_create(device_locations)
            deviceStatus_object = deviceStatus.objects.bulk_create(deviceStatus_details)
            canInfo_object = canInfo.objects.bulk_create(canInfo_details)
            alerts_object = alerts.objects.bulk_create(alerts_details)
            todaysDrive_object = todaysDrive.objects.bulk_create(todaysDrive_details)
            links_object = links.objects.bulk_create(links_details)
            dinputs_object = dinputs.objects.bulk_create(dinputs_details)

            return Response({"message": "device data created successfully"}, status=200)

        else:
            return Response(devices_data, status=response.status_code)
        
        
