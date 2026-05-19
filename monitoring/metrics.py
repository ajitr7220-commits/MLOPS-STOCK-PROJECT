from prometheus_client import start_http_server
import time

start_http_server(9000)

while True:
    time.sleep(1)