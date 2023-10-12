import asyncio

async def handel_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send : {message!r}")
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()
    await writer.wait_closed()

async def main():
    sever = await asyncio.start_server(handel_echo,'127.0.0.1',2355)
    addrs = ', '.join(str(sock.getsockname()) for sock in sever.sockets())
    print(f"Serving on {addrs}")

    async with sever:
        await sever.serve_forever()

asyncio.run(main())