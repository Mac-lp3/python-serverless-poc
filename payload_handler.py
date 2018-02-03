from domain.abstract_payload_processor import AbstractPayloadProcessor

class PayloadHandler(AbstractPayloadProcessor):
    def processPayload(self, crud_op, json_payload):
        print('omg in my processor impl.')
