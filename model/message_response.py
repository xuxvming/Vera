class MessageResponse:
    def __init__(self,fullfillment_text,socketId,submitted_message,timestamp):
        self.fullfillment_text = fullfillment_text
        self.socketId = socketId
        self.submitted_message = submitted_message
        self.timestamp = timestamp

    def serialize(self):

        return {
            "response message": self.fullfillment_text,
            "socketID": self.socketId,
            "submitted message": self.submitted_message,
            "time": str(self.timestamp)
        }