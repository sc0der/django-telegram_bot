class Middleware(object):
    def __init__(self, message):
        self.message = message

    def is_bot(self):
        if self.message.from_user.is_bot:
            return True
        return False
    
