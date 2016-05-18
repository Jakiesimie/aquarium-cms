# -*- coding: utf-8 -*-

import os
from subprocess import check_output

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.test import APIRequestFactory
from rest_framework.generics import ListAPIView
from rest_framework import mixins
from rest_framework import generics

from django.conf import settings
from django.core import serializers
from django.core.files import File
from django.http import Http404
from django.http.response import HttpResponse
from django.template.response import TemplateResponse
from django.test import RequestFactory
from django.views.generic.base import TemplateView

from aquarium.models import Map, Tank, Habitat, Trivia, Species
from quiz.models import Grade, Quiz, Image, Test
from .serializers import (MapSerializer, TankSerializer, HabitatSerializer, TriviaSerializer, SpeciesSerializer,
                          GradeSerializer, QuizSerializer, ImageSerializer, TestSerializer)
from isolve.settings import BASE_DIR, MEDIA_ROOT


# Generic ClassViews for API
class CustomList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    def get_serializer_class(self):
        serializer = self.kwargs.get('model', None).title()
        return eval(serializer+'Serializer')

    def get_queryset(self):
        arg = self.kwargs.get('model', None)
        model = arg.title()
        queryset = eval(model+'.objects.all()')
        tank = self.request.query_params.get('tank', None)
        dump = self.request.query_params.get('dump', None)
        if tank is not None:
            queryset = queryset.filter(tank=tank)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CustomDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    def get_queryset(self):
        model = self.kwargs.get('model', None).title()
        queryset = eval(model+'.objects.all()')
        return queryset

    def get_serializer_class(self):
         model = self.kwargs.get('model', None).title()
         return eval(model+'Serializer')


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



# TODO: Merge ClassViews to make the code DRY.
# ClassViews only for API Backup
class MapList(ListAPIView):
    # authentication_classes = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = MapSerializer
    model = Map

    def post(self, request, *args, **kwargs):
        """https://techcave.atlassian.net/browse/BOK-181"""
        return self.get(request, args, kwargs)

    def get_queryset(self):
        return self.model.objects.all()



class TankList(ListAPIView):
    # authentication_classes = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = TankSerializer
    model = Tank

    def post(self, request, *args, **kwargs):
        """https://techcave.atlassian.net/browse/BOK-181"""
        return self.get(request, args, kwargs)

    def get_queryset(self):
        return self.model.objects.all()


class SpeciesList(ListAPIView):
    # authentication_classes = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = SpeciesSerializer
    model = Species

    def post(self, request, *args, **kwargs):
        """https://techcave.atlassian.net/browse/BOK-181"""
        return self.get(request, args, kwargs)

    def get_queryset(self):
        return self.model.objects.all()


class HabitatList(ListAPIView):
    # authentication_classes = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = HabitatSerializer
    model = Habitat

    def post(self, request, *args, **kwargs):
        """https://techcave.atlassian.net/browse/BOK-181"""
        return self.get(request, args, kwargs)

    def get_queryset(self):
        return self.model.objects.all()

class TriviaList(ListAPIView):
    # authentication_classes = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = TriviaSerializer
    model = Trivia

    def post(self, request, *args, **kwargs):
        """https://techcave.atlassian.net/browse/BOK-181"""
        return self.get(request, args, kwargs)

    def get_queryset(self):
        return self.model.objects.all()


class GradeList(ListAPIView):
    # authentication_classes = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = GradeSerializer
    model = Grade

    def post(self, request, *args, **kwargs):
        """https://techcave.atlassian.net/browse/BOK-181"""
        return self.get(request, args, kwargs)

    def get_queryset(self):
        return self.model.objects.all()


class QuizList(ListAPIView):
    # authentication_classes = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = QuizSerializer
    model = Quiz

    def post(self, request, *args, **kwargs):
        """https://techcave.atlassian.net/browse/BOK-181"""
        return self.get(request, args, kwargs)

    def get_queryset(self):
        return self.model.objects.all()


class ImageList(ListAPIView):
    # authentication_classes = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = ImageSerializer
    model = Image

    def post(self, request, *args, **kwargs):
        """https://techcave.atlassian.net/browse/BOK-181"""
        return self.get(request, args, kwargs)

    def get_queryset(self):
        return self.model.objects.all()


# Copyright (c) 2010-2014 Mariusz Smenzyk <mariusz.smenzyk@sizeof.pl>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""

@author: Mariusz Smenzyk
@license: MIT License
@contact: mariusz.smenzyk@sizeof.pl
"""

class BackupView(TemplateView):

    def render_to_response(self, context, **response_kwargs):
        """
        Creates a CSV response if requested, otherwise returns the default
        template response.
        """

        site_url = self.request.GET.get('site_url')
        api_dir = os.path.join(settings.MEDIA_ROOT, 'upload')
        resources = {
            'map/list/': MapList,
            'tank/list/': TankList,
            'species/list/': SpeciesList,
            'habitat/list/': HabitatList,
            'trivia/list/': TriviaList,
            'grade/list/': GradeList,
            'quiz/list/': QuizList,
            'image/list/': ImageList,
        }

        for link, view_class in resources.iteritems():
            request = APIRequestFactory().post(link +  "?format=json&site_url=127.0.0.1", format='json')
            view = view_class.as_view()
            response = view(request)


            data = response.rendered_content
            # content = self.FILE_TEMPLATE.format(data=data, parse_func=self.FILE_TEMPLATE_PARSE_FUNC)

            #TO DO####################
            name = link
            filename = os.path.join(api_dir, 'api', link, 'data.json')
            directory = os.path.dirname(filename)

            if not os.path.exists(directory):
                os.makedirs(directory)

            with open(filename, 'w') as f:
                myfile = File(f)
                myfile.write(data)


        # Compres backup
        backup_file = os.path.realpath('%s/../data/media.zip' % settings.MEDIA_ROOT)
        output = check_output("cd %s " % settings.MEDIA_ROOT + "&& zip -r " + backup_file + ' .', shell=True)


        if not os.path.exists(os.path.dirname(backup_file)):
            os.mkdir(os.path.dirname(backup_file))

        # text_response = HttpResponse("OK:"+backup_file, content_type="text/plain")

        # Out
        response = HttpResponse(open(backup_file), content_type="application/zip")
        response["Content-Disposition"] = "attachment; filename=%s.zip" % 'media'

        return response
