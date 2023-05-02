from mycroft import MycroftSkill, intent_file_handler
from pybotvac import Robot
from mycroft.util import LOG
import json
from os.path import dirname, join

class RobotControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        auth_path = join(dirname(__file__),"NEATOROBOT")
        with open(auth_path) as f:
            lines = f.read().split(",")
            self.serial = lines[0]
            self.secret = lines[1]
            self.traits = lines[2]
        self.robot = None
        self._init_robot()


    def _init_robot(self):
        try:
            self.robot = Robot(self.serial,self.secret,self.traits)
        except:
            self.robot = None

    @intent_file_handler('control.robot.locate')
    def handle_locate_robot(self, message):
        if not self.robot:
            self._init_robot()
        res = self.robot.locate()
        parsed = json.loads(res.text)
        if parsed['result'] == 'command_rejected':
            self.speak_dialog('control.robot.unable')


    @intent_file_handler('control.robot.start')
    def handle_start_robot(self, message):
        if not self.robot:
            self._init_robot()
        res = self.robot.start_cleaning(category=4)
        parsed = json.loads(res.text)
        if parsed['result'] == 'command_rejected':
            self.speak_dialog('control.robot.unable')


    @intent_file_handler('control.robot.stop')
    def handle_stop_robot(self, message):
        if not self.robot:
            self._init_robot()
        res = self.robot.stop_cleaning()
        parsed = json.loads(res.text)
        if parsed['result'] == 'command_rejected':
            self.speak_dialog('control.robot.unable')


    @intent_file_handler('control.robot.home')
    def handle_park_robot(self, message):
        if not self.robot:
            self._init_robot()
        res = self.robot.send_to_base()
        parsed = json.loads(res.text)
        if parsed['result'] == 'command_rejected':
            self.speak_dialog('control.robot.unable')

def create_skill():
    LOG.info("RobotControl.create_skill called")
    return RobotControl()

