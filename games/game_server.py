import grpc
import time
from concurrent import futures
import game_pb2_grpc, game_pb2
import psycopg2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = '0.0.0.0'
_PORT = '50051'


class Gamer(game_pb2_grpc.GamerServicer):
    def GetGameDetail(self, request, response):
        print("grpc ask for ", request.id)
        conn = psycopg2.connect(database="google_play_games", user="postgres", password="binshao123", host="127.0.0.1",
                                port="5432")
        cur = conn.cursor()
        sql = "select id, name, author, star_rating, download_times, content_rating, introduction, update_time, image from games_games where id = "+ str(request.id)
        cur.execute(sql)
        game = cur.fetchall()
        game = game[0]
        rep = game_pb2.GameResponse(id=game[0], name=game[1], author=game[2], downloadTimes=str(game[4]), contentRating=game[5], introduction=game[6], updateTime=str(game[7]), image=game[8])
        conn.close()

        return rep


def serve():
    # 定义服务器并设置最大连接数,corcurrent.futures是一个并发库，类似于线程池的概念
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))  # 创建一个服务器
    game_pb2_grpc.add_GamerServicer_to_server(Gamer(), grpc_server)  # 在服务器中添加派生的接口服务（自己实现了处理函数）
    grpc_server.add_insecure_port(_HOST + ':' + _PORT)  # 添加监听端口
    print("start server...")
    grpc_server.start()  # 启动服务器
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpc_server.stop(0)  # 关闭服务器


if __name__ == '__main__':
    serve()
