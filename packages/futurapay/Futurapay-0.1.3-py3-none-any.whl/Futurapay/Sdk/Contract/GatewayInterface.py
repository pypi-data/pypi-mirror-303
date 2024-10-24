class GatewayInterface:
    def initialize(self, payment_payload: dict):
        raise NotImplementedError

    def get_payment(self, hashtoken: str):
        raise NotImplementedError

    def get_status(self, hashtoken: str):
        raise NotImplementedError
