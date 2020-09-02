from mycroft import MycroftSkill, intent_file_handler


class CommandToMqtt(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mqtt.to.command.intent')
    def handle_mqtt_to_command(self, message):
        self.speak_dialog('mqtt.to.command')


def create_skill():
    return CommandToMqtt()

