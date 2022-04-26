import asyncio
import websockets
import base64

async def media_receiver(websocket):
    media = await websocket.recv()
    try:
        fh = open(f"video.mp4","wb")
        fh.write(base64.b64decode(media))
        #text = open(f'error.txt','w')
        #text.write(chunk)
        fh.close()
        print('success!')
        
    except Exception as er:
        raise(er)
            


async def main():
    async with websockets.serve(media_receiver, "localhost", 8765, max_size=None):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())