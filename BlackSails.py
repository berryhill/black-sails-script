from __future__ import with_statement
import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/')

from OSC import OSCClient, OSCMessage
import time
import Live

from _Framework.ControlSurface import ControlSurface
from _Framework.SessionComponent import SessionComponent
from _Framework.ButtonElement import ButtonElement

class BlackSails(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
            self.session = SessionComponent(5, 1)
            self.session.set_offsets(0, 0)
            self.session.scene(0).clip_slot(0).set_launch_button(ButtonElement(False, 1, 6, 2))
            self.session.scene(0).clip_slot(1).set_launch_button(ButtonElement(False, 0, 6, 0))
            self.set_highlighting_session_component(self.session)

        client = OSCClient()
        client.connect(("127.0.0.1", 5555))

        client.send(OSCMessage("/hello"))