"""
 * Copyright (C) Caleb Marshall and others... - All Rights Reserved
 * Written by Caleb Marshall <anythingtechpro@gmail.com>, May 23rd, 2017
 * Licensing information can found in 'LICENSE', which is part of this source code package.
"""

from curionet import network

class ExampleHandler(network.NetworkHandler):
    """
    An example connection handler derived from NetworkHandler
    """

    async def handle_connected(self):
        print ('Connected.')

    async def handle_received(self, data):
        print ('Data recieved from (%s: %r)!' % (self.address, data))

        # send the data back to the client.
        await self.handle_send(data)

    async def handle_disconnected(self):
        print ('Disconnected.')

if __name__ == '__main__':
    factory = network.NetworkFactory('0.0.0.0', 8080, ExampleHandler)
    factory.run()