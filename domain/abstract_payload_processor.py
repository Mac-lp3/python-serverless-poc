from abc import ABC, abstractmethod

class AbstractPayloadProcessor(ABC):
    def __init__(self, config):
        self.__config = config

    @abstractmethod
    def processPayload(self, crud_op, json_payload):
        pass

    def __preHandle(self, payload):
        print('reached prehandle')

    def __postHandle(self, payload):
        print('reached posthandle')

    def beginProcessing(self, payload):
        self.__preHandle(payload)
        try:
            self.processPayload(
                payload['operation'],
                payload['body']
            )
        except Exception as e:
            self.handleError(e)
        self.__postHandle(payload)

    def handleError(self, error):
        print('caught this', error)
