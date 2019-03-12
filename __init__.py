from mycroft import MycroftSkill, intent_file_handler


class HospitalAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        breakfastChoice = ""
        lunchChoice = ""
        dinnerChoice = ""
        beverageChoice = ""

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

    @intent_file_handler('menu.intent')
    def handle_menu(self, message):
        self.speak_dialog('breakfast')

    @intent_file_handler('breakfastRequest.intent')
    def handle_breakfastrequest(self, message):
        self.speak_dialog('breakfast')

    @intent_file_handler('lunchrequest.intent')
    def handle_lunchrequest(self, message):
        self.speak_dialog('lunch')

    @intent_file_handler('dinnerrequest.intent')
    def handle_dinnerrequest(self, message):
        self.speak_dialog('dinner')

    @intent_file_handler('beveragerequest.intent')
    def handle_dinnerrequest(self, message):
        self.speak_dialog('beverage')

    @intent_file_handler('ChickenSandwich.intent')
    def handle_chickensandwich(self, message):
         lunchChoice = "Chicken sandwich"
         self.speak_dialog('dinner')

    @intent_file_handler('coffeeRequest.intent')
    def handle_coffee(self, message):
         beverageChoice = "Coffee"
         self.speak_dialog("We will get you a " + beverageChoice)

    @intent_file_handler('tea.intent')
    def handle_coffee(self, message):
         beverageChoice = "Tea"
         self.speak_dialog("We will get you a " + beverageChoice)

    @intent_file_handler('Water.intent')
    def handle_coffee(self, message):
         beverageChoice = "Water"
         self.speak_dialog("We will get you a " + beverageChoice)

    @intent_file_handler('pasta.intent')
    def handle_pasta(self, message):
         dinnerChoice = "Pasta"
         self.speak_dialog("Thanks Dave, here are your choices. Your breakfast is " + breakfast + " Your lunch choice is " + lunch + " Your dinner is " + dinner)

    @intent_file_handler('PorkChop.intent')
    def handle_PorkChop(self, message):
         dinnerChoice = "Pork Chop"
         self.speak_dialog("Thanks Dave, here are your choices. Your breakfast is " + breakfast + " Your lunch choice is " + lunch + " Your dinner is " + dinner)

    @intent_file_handler('ShepherdsPie.intent')
    def handle_ShepherdsPie(self, message):
         dinnerChoice = "Shepherds Pie"
         self.speak_dialog("Thanks Dave, here are your choices. Your breakfast is " + breakfast + " Your lunch choice is " + lunch + " Your dinner is " + dinner)

    @intent_file_handler('porridge.intent')
    def handle_porridge(self, message):
         breakfastChoice = "Porridge"
         self.speak_dialog('lunch')

    @intent_file_handler('Salad.intent')
    def handle_salad(self, message):
         lunchChoice = "Salad"
         self.speak_dialog('dinner')

    @intent_file_handler('ScrambledEggs.intent')
    def handle_scrambledeggs(self, message):
         lunchChoice = "Scrambled Eggs"
         self.speak_dialog('lunch')

    @intent_file_handler('Soup.intent')
    def handle_soup(self, message):
         lunchChoice = "Soup"
         self.speak_dialog('dinner')

    @intent_file_handler('toast.intent')
    def handle_toast(self, message):
         breakfastChoice = "Toast"
         self.speak_dialog('lunch')


def create_skill():
    return HospitalAssistant()
