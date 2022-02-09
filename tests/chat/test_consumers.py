import json

import pytest
from channels.testing import WebsocketCommunicator

from config.asgi import application


@pytest.mark.asyncio
async def test_my_consumer():
    communicator = WebsocketCommunicator(application, "/ws/chat/lobby/")
    connected, _ = await communicator.connect()

    assert connected
    # Test sending text
    await communicator.send_to(text_data=json.dumps({'message': 'hello'}))

    response = await communicator.receive_from()
    assert json.loads(response)['message'] == 'hello'

    # Close
    await communicator.disconnect()
