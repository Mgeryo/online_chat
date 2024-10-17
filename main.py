import asyncio
import websockets

all_clients = [] # список клиентов

async def send_message(message: str):
    for client in all_clients:
        await client.send(message) # отправление сообщений каждому клиенту в списке
        

# client_socket это собственно сам сокет, который открывает соединение между клиентом(JS) и сервером(PY)
async def new_client_connected(client_socket: websockets.WebSocketClientProtocol, path: str):
    print("New client connected!")
    all_clients.append(client_socket) # добавляем нового клиента в список
    
    while True:
        new_message = await client_socket.recv() # recv это recive - то есть метод для получения сообщений
        print("New message from a client", new_message)
        await send_message(message=new_message)

async def start_server():
    # создаем сервер
    await websockets.serve(new_client_connected, "localhost", 12345)  # callback функция - первый аргумент, вызывается когда клиент к нам подключается

if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(start_server())
    event_loop.run_forever()