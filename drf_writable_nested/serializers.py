from rest_framework import serializers

from .mixins import NestedCreateMixin, NestedUpdateMixin, NestedGetOrCreateMixin


class WritableNestedModelSerializer(NestedGetOrCreateMixin, NestedUpdateMixin,
                                    serializers.ModelSerializer):
    pass
