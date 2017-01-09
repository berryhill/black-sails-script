from __future__ import with_statement
import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/')

# from OSC import OSCClient, OSCMessage
import time
import Live

transport_play_button = None
transport_stop_button = None
# transport_record_button = None
session_box_button_count = 0
session_box_count = 0

from _Framework.ControlSurface import ControlSurface
from _Framework.SessionComponent import SessionComponent
from _Framework.ButtonElement import ButtonElement
from _Framework.TransportComponent import TransportComponent

class BlackSails(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
            self._make_transport()
            self._make_session_box(16, 16)

        # VVV would like the try to see if the following code works VVV

        # client = OSCClient()
        # client.connect(("127.0.0.1", 5555))
        #
        # with self.compontent_guard():
        #     self._make_session_box(16, 16)

        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        # client.send(OSCMessage("/hello"))


    def _configure_hardware_functions(self):
        pass


    def _request_hardware_functions(self):
        pass


    def _handle_hardware_function_calls(self):
        pass


    def _make_transport(self):
        global transport_play_button
        transport_play_button = ButtonElement(False, 0, 10, 0)
        global transport_stop_button
        transport_stop_button = ButtonElement(False, 0, 10, 1)

        transport = TransportComponent()
        transport.set_play_button(transport_play_button)
        transport.set_stop_button(transport_stop_button)
        # transport.set_record_button(transport_record_button)


    def _make_session_box(self, scenes, tracks):
        self.session = SessionComponent(scenes, tracks)
        self.session.set_offsets(0, 0)
        for k in range(session_box_button_count, session_box_button_count + (scenes * tracks)):
            self.session.scene(k - session_box_button_count % scenes).clip_slot(k - session_box_button_count % tracks).\
                set_launch_button(ButtonElement(False, 0, 8, k))
        self.set_highlighting_session_component(self.session)

        global session_box_button_count
        session_box_button_count = session_box_button_count + (scenes * tracks)
        global session_box_count
        session_box_count = session_box_count + 1
