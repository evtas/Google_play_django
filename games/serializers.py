from django.contrib.auth.models import User
from django_grpc_framework import proto_serializers
from google_play_games.proto import games_pb2


class GameProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = User
        proto_class = games_pb2.Game
        fields = ['id', 'name', 'author', 'star_content', 'download_times', 'content_rating', 'introduction',
                  'update_time', 'genre', 'groups']
