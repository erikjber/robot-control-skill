from mycroft import MycroftSkill, intent_file_handler


class RobotControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.robot.intent')
    def handle_control_robot(self, message):
        self.speak_dialog('control.robot')


def create_skill():
    return RobotControl()

