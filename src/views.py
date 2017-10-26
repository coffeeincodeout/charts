from django.shortcuts import render
from .models import BusinessProfile
from django.views.generic import TemplateView

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BusinessProfileSerializer
# Create your views here.


def index(request):
    zip_code_list = []
    profile = BusinessProfile.objects.all()
    for zip in profile:
        zip_code_list.append(zip.zipCode)
    context = {'zip_code_list': zip_code_list}
    return render(request, 'profile.html', context)

class DataView(TemplateView):


    def get_context_data(self, **kwargs):
        context = super(DataView, self).get_context_data()
        context['florida_zip_code'] = self.zipcodes()
        return context

    def zipcodes(self):
        zip_code_list = []
        profile = BusinessProfile.objects.all()
        for zip in profile:
            zip_code_list.append(zip.zipCode)

        return zip_code_list

    def legend(self):
        legend_zip = set()
        sorted(legend_zip)
        profile = BusinessProfile.objects.all()
        for zip in profile:
            legend_zip.add(zip)
        context = super(DataView, self).get_context_data()
        context['legend'] = legend_zip
        return context


class BusinessProfileList(APIView):

    """
    Lists all active companies
    """

    def get(self, request, format=None):
        # Get all objects from database
        company = BusinessProfile.objects.all()
        # Pass all objects through to BusinessProfileSerializer class
        serializer = BusinessProfileSerializer(company, many=True)
        # Return JSON response
        return Response(serializer.data)

