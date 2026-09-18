import asyncio 
import ssl
import websockets

unencryted_clients = set()
encrypted_clients = set()

async def unencrypted_handler(websocket):
    unencryted_clients.add(websocket)
    try:
        async for message in websocket:
            print("[UNENCRYPTED]", message)
            for client in unencryted_clients:
                if client != websocket:
                    await client.send(message)
    finally:
        unencryted_clients.remove(websocket)

async def encrypted_handler(websocket):
    encrypted_clients.add(websocket)
    try:
        async for message in websocket:
            print("[ENCRYPTED]", message)
            for client in encrypted_clients:
                if client != websocket:
                    await client.send(message)
    finally:
        encrypted_clients.remove(websocket)

async def main():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain("cert.pem", "key.pem")

    async with websockets.serve(unencrypted_handler, "0.0.0.0", 8765):
        async with websockets.serve(encrypted_handler, "0.0.0.0", 8766, ssl=ssl_context):
            await asyncio.Future()
        
asyncio.run(main())