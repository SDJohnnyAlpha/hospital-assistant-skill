from mycroft import MycroftSkill, intent_file_handler


class HospitalAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('assistant.hospital.intent')
    def handle_assistant_hospital(self, message):
        self.speak_dialog('assistant.hospital')


def create_skill():
    return HospitalAssistant()

