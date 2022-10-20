from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import json
import base64
import numpy as np



class ChatConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def connect(self):
        self.room_name = 'Test-Room'
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        print("connected by someone")
        await self.accept()


    async def disconect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

        print('Disconnected!')

    async def receive(self, bytes_data):
        #data = base64.b64decode(bytes_data)
        # print("type of data", data)

        # npdata = np.fromstring(data, dtype=np.uint8)
        # print("type of npdata : ", type(npdata))
        # #print('{} {}'.format(n, npdata))
        # frame = cv2.imdecode(npdata, 1)
        # # self.thread = threading.Thread(target=self.send_data, args=(bytes_data,))
        # # self.thread.daemon = True
        # # self.thread.start()
        # cv2.imshow("receiving video", frame)
        # key = cv2.waitKey(1) & 0xFF
        # if key == ord('q'):
        #     cv2.destroyAllWindows()
        # print("$$$$$$$$$$$$$$$$$$$$$$$$$$")
        # print(type(data))
        # data_dict = {
        #     "data": data,
        # }
        # data_dict = json.dumps(data_dict)
        # text = 'ejwirewji'
        # text = base64.b64encode(text.encode())
        # print(text)
        #
        # print
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'data': bytes_data,
            }
        )

    async def send_data(self, bytedata):
        print("running")



    async def chat_message(self, event):
        #message = event['message']
        print(self.channel_name)
        # Send message to WebSocket
        await self.send(bytes_data=event['data'])


    async def send_sdp(self, event):
        receive_dict = event['receive_dict']

        # Send message to WebSocket
        await self.send(text_data=json.dumps(receive_dict))
