import asyncio 

async def scan(host, port, semaphore):
	async with semaphore:
		try:
			reader, writer = await asyncio.wait_for(
				asyncio.open_connection(host, port),
				timeout = 0.1
			)
			writer.close()
			await writer.wait_closed()
			return port 
		except ConnectionRefusedError:
			pass
		except asyncio.TimeoutError:
			pass

async def handle_client(Reader, Writer):
	semaphore = asyncio.Semaphore(100)
	addr = Writer.get_extra_info("peername")
	print(f"Connected to client {addr}")
	open_ports = await asyncio.gather(*[asyncio.create_task(scan(addr[0], port, semaphore)) for port in range (50000, 60000)])
	open_ports = [port for port in open_ports if port != None]
	print(f"The ports {open_ports} are open")
	while True:
		data = await Reader.read(1024)
		if not data:
			break
		print(f"	Data from client: {data}")
		Writer.write(data)
		Writer.write(b"Fuck You")
		await Writer.drain()
	

async def main():
	Host, Port = "127.0.0.1", 80
	server = await asyncio.start_server(handle_client, Host, Port)
	try:
		await server.serve_forever()
	finally:
		server.close()
		await server.wait_closed()

try:
	asyncio.run(main())
except KeyboardInterrupt:
	print("Server stopped")