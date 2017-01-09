from __future__ import with_statement
import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/')

# from OSC import OSCClient, OSCMessage
import time
import Live

transport_play_button = None
transport_stop_button = None
# transport_record_button = None

from _Framework.ControlSurface import ControlSurface
from _Framework.SessionComponent import SessionComponent
from _Framework.ButtonElement import ButtonElement
from _Framework.TransportComponent import TransportComponent

class BlackSails(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
            self._configure_transport_buttons()
            self._make_transport()

        # VVV would like the try to see if the following code works VVV

        # client = OSCClient()
        # client.connect(("127.0.0.1", 5555))
        #
        # with self.compontent_guard():
        #     self._make_session_box(16, 16)

        # client.send(OSCMessage("/hello"))


    def _configure_hardware_functions(self):
        pass


    def _request_hardware_functions(self):
        pass


    def _handle_hardware_function_calls(self):
        pass


    def _configure_transport_buttons(self):
        global transport_play_button
        transport_play_button = ButtonElement(False, 0, 10, 0)
        global transport_stop_button
        transport_stop_button = ButtonElement(False, 0, 10, 1)
        # global transport_record_button
        # transport_record_button = ButtonElement(False, 0, 10, 2)


    def _make_transport(self):
        transport = TransportComponent()
        transport.set_play_button(transport_play_button)
        transport.set_stop_button(transport_stop_button)
        # transport.set_record_button(transport_record_button)


    def _configure_sesssion_box_buttons(self):
        pass

    def _make_session_box(self, scenes, tracks):
        self.session = SessionComponent(scenes, tracks)
        self.session.set_offsets(0, 0)
        # self.session.scene(0).clip_slot(0).set_launch_button(ButtonElement(False, 1, 6, 2))
        # self.session.scene(0).clip_slot(1).set_launch_button(ButtonElement(False, 0, 6, 0))
        self.set_highlighting_session_component(self.session)