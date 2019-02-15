from mycroft import MycroftSkill, intent_file_handler


class HospitalAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('assistant.hospital.intent')
    def handle_assistant_hospital(self, message):
        self.speak_dialog('assistant.hospital')

    @intent_file_handler('whereami.intent')
    def handle_whereami(self, message):
        self.speak_dialog('where.am.i')

    @intent_file_handler('diet.intent')
    def handle_diet(self, message):
        self.speak_dialog('diet.update')

    @intent_file_handler('doctorvisit.intent')
    def handle_doctorvisit(self, message):
        self.speak_dialog('doctor.rounds.update')

    @intent_file_handler('gohome.intent')
    def handle_gohome(self, message):
        self.speak_dialog('release.request')

    @intent_file_handler('medication.intent')
    def handle_medication(self, message):
        self.speak_dialog('medication.update')

    @intent_file_handler('thedoctoris.intent')
    def handle_thedoctoris(self, message):
        self.speak_dialog('who.is.the.doctor')

    @intent_file_handler('thenurseis.intent')
    def handle_thenurseis(self, message):
        self.speak_dialog('who.is.the.nurse')


def create_skill():
    return HospitalAssistant()
