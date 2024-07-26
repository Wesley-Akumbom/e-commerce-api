# custom_schema.py

from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg import openapi
from rest_framework import serializers

from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view


class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
    def get_paths(self, endpoints, components, request, public):
        paths = super().get_paths(endpoints, components, request, public)
        # Customize paths here if needed
        return paths


# Define a custom SwaggerAutoSchema that handles generic serialization
class CustomSwaggerAutoSchema(SwaggerAutoSchema):
    def get_request_serializer(self):
        serializer_class = self.get_request_serializer_class()
        if serializer_class is None:
            return None
        return serializer_class()

    def get_request_serializer_class(self):
        # Return a generic serializer if needed
        return serializers.Serializer

    def get_responses(self):
        responses = super().get_responses()
        # Customize responses here if needed
        return responses

