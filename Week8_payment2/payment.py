class PaymentGateway:
    def charge (self, amonut):
        raise NotImplementedError("Real gateway not available in tests")

    class OrderProcessor:
        def __init__(self, gateway):
            self.payment_gateway = gateway

        def process(self, amount):
            if amount <= 0:
                raise ValueError("Amount must be positive")
            result = self.gateway.charge(amount)
            return f"Order processed: {result}"