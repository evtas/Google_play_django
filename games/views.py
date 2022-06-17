from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, FileResponse, Http404
from .models import Games
from django.core.paginator import Paginator
from django.template.defaulttags import register
import os
import grpc
from . import game_pb2_grpc
from . import game_pb2
# import game_pb2_grpc, game_pb2

_HOST = '0.0.0.0'
_PORT = '50051'


def nginx_view(request):
    html = "<h1>Using port " + request.META["SERVER_PORT"] + "<h1>"
    return HttpResponse(html)


def search(request):
    games = Games.objects.all()
    if 'keywords' in request.GET:
        keywords = request.GET.get('keywords')
        if keywords:
            games = Games.objects.filter(name__icontains=keywords)

    paginator = Paginator(games, 12)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'games': paged_listings,
    }

    return render(request, 'search.html', context)


def details(request, game_id=None):
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = game_pb2_grpc.GamerStub(channel=conn)
    req = game_pb2.GameRequest(id=game_id)
    game = client.GetGameDetail(req)
    print(game)
    # game = get_object_or_404(Games, pk=game_id)
    context = {'game': game}

    return render(request, 'detail.html', context)


def download(request, game_id=None):
    file_path = os.path.abspath("/Users/Ben/download_apks/" + str(game_id) + ".apk ")
    print(file_path)

    try:
        f = open("/Users/Ben/download_apks/" + str(game_id) + ".apk", 'rb')
        response = FileResponse(f)
        return response

    except Exception as e:
        print(e)
        return HttpResponse("文件不存在")


def test(request):
    return render(request, 'test.html')


@register.filter
def get_range(value):
    return range(1, value + 1)


@register.filter
def get_range_tail(value):
    print(1)
    start = value - 4
    print(start, " ", value + 1)
    return range(start, value + 1)

