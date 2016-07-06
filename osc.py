import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/')

import OSC

class Osc(object):
    def __init__(self, c_instance):
        client = OSC.Client()
        client.connect(("127.0.0.1", 5555))

    def send_startup_message(self):
        self.client.send(OSC.OSCMessage("/startup/test"))