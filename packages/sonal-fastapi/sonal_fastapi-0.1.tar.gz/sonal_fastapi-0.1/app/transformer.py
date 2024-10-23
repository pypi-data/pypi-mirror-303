from app.utils.payload_schema import InputPayload

class LogicProcessor:
    @staticmethod
    def process_uppercase_data(InputPayload):
        upper_input = InputPayload.input.upper()
        response = {
            "requestor_name": InputPayload.name,
            "upper_input": upper_input
        }
        return response