class Question(object):
    def __init__(self, rollNumber, name, *args, **kwargs):
        self.rollNumber = rollNumber
        self.name = name

class Owner(object):
    def __init__(self, reputation, used_id,
                 user_type, profile_image,
                 display_name, link):
        self.reputation = reputation
        self.user_id = user_id
        self.user_type = user_type
        self.profile_image = profile_image
        self.display_name = display_name
        self.link = link

class QuestionEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__