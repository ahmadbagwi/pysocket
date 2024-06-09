import socket
import os, os.path
import json
def run_server():
  # create a socket object
  server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
  # server_ip = "127.0.0.1"
  # port = 8000
  if os.path.exists("/var/run/dev-test/sock"):
    os.remove("/var/run/dev-test/sock")
  # bind the socket to a specific address and port
  # server.bind((server_ip, port))
  server.bind("/var/run/dev-test/sock")
  # listen for incoming connections
  server.listen(0)
  # print(f"Listening on {server_ip}:{port}")
  print(f"Listening on /var/run/dev-test/sock")
  # accept incoming connections
  client_socket, client_address = server.accept()
  print(f"Accepted connection from {client_socket}:{client_address}")
  isJsonCheck = ['{', '}', 'id', 'method', 'params']
  # receive data from the client
  while True:
    request = client_socket.recv(1024)
    request = request.decode("utf-8") # convert bytes to string
    # if we receive "close" from the client, then we break
    # out of the loop and close the conneciton
    if request.lower() == "close":
      # send response to the client which acknowledges that the
      # connection should be closed and break out of the loop
      client_socket.send("closed by close request".encode("utf-8"))
      break
    if all(string in request for string in isJsonCheck):
      loads = json.loads(request)
      #loads = json.loads(json_object)
      if (loads['method']) == 'echo':
        str_json = '{"id": ' + str(loads['id']) + ', "result" :' + str(loads['params']) + '}' + '\n'
        response = str_json.encode("utf-8") # convert string to bytes
        # convert and send accept response to the client
        client_socket.send(response)
    else:
      response = "Invalid request " + str(request) + '\n'
      client_socket.send(response.encode("utf-8"))
      # client_socket.close()
      break
  # close connection socket with the client
  client_socket.close()
  print("Connection to client closed")
  # close server socket
  server.close()

run_server()
