import datetime
import socket


class myget:
    @staticmethod
    def get_ip():
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        return ip

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        send_time = now.strftime("%Y-%m-%d %H:%M:%S")
        return send_time