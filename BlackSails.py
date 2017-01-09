from __future__ import with_statement
import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/')

from OSC import OSCClient, OSCMessage
import time
import Live

play_button = None
stop_button = None
# record_button = None

from _Framework.ControlSurface import ControlSurface
from _Framework.SessionComponent import SessionComponent
from _Framework.ButtonElement import ButtonElement
from _Framework.ButtonElement import TransportComponent

class BlackSails(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
            self.session = SessionComponent(5, 1)
            self.session.set_offsets(0, 0)
            self.session.scene(0).clip_slot(0).set_launch_button(ButtonElement(False, 1, 6, 2))
            self.session.scene(0).clip_slot(1).set_launch_button(ButtonElement(False, 0, 6, 0))
            self.set_highlighting_session_component(self.session)
            self._make_transport_buttons()
            self._configure_transport()

        client = OSCClient()
        client.connect(("127.0.0.1", 5555))

        client.send(OSCMessage("/hello"))


    def _make_transport_buttons(self):
        global play_button
        play_button = ButtonElement(False, 0, 10, 0)
        global stop_button
        stop_button = ButtonElement(False, 0, 10, 1)
        # global record_button
        # record_button = ButtonElement(False, 0, 10, 2)


    def _configure_transport(self):
        transport = TransportComponent()
        transport.set_play_button(play_button)
        transport.set_stop_button(stop_button)
        # transport.set_record_button(record_button)