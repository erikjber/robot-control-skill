from mycroft import MycroftSkill, intent_file_handler
from pybotvac import Robot
from mycroft.util import LOG
import json

class RobotControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        with open("NEATOROBOT") as f:
            lines = f.read().split(",")
            self.robot = Robot(lines[0],lines[1],lines[2])

    @intent_file_handler('control.robot.locate')
    def handle_locate_robot(self, message):
        res = self.robot.locate()
        parsed = json.loads(res.text)
        if parsed['result'] == 'command_rejected':
            self.speak_dialog('control.robot.unable')


    @intent_file_handler('control.robot.start')
    def handle_start_robot(self, message):
        res = self.robot.start_cleaning()
        parsed = json.loads(res.text)
        if parsed['result'] == 'command_rejected':
            self.speak_dialog('control.robot.unable')


    @intent_file_handler('control.robot.stop')
    def handle_stop_robot(self, message):
        res = self.robot.stop_cleaning()
        parsed = json.loads(res.text)
        if parsed['result'] == 'command_rejected':
            self.speak_dialog('control.robot.unable')


    @intent_file_handler('control.robot.home')
    def handle_park_robot(self, message):
        res = self.robot.send_to_base()
        parsed = json.loads(res.text)
        if parsed['result'] == 'command_rejected':
            self.speak_dialog('control.robot.unable')

def create_skill():
    LOG.info("RobotControl.create_skill called")
    return RobotControl()

