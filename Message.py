class Message:
    def __init__(self, data):
        self.message = data['message']['text']
        self.chat_id = data['message']['chat']['id']
        if self.message == '/popular':
            self.action = '/popular'
            self.value = 0
        elif self.message.count(' ') > 0:
            self.action = self.message.split(' ')[0]
            self.value = self.message.split(' ')[1]
        else:
            self.action = None
            self.value = None