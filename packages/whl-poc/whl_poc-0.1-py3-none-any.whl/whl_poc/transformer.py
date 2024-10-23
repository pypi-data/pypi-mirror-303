from pydantic import BaseModel, Field
import logging
from fastapi.exceptions import HTTPException


class RequestPayload(BaseModel):
    """
    Request payload details.
    """
    # name: str
    # input: str
    name: str = Field(
        default=None,
        min_length=1,
        max_length=30,
        title="Name of the requester.",
        description="Provide valid string for 'name'."
    )
    input: str = Field(
        default=None,
        min_length=1,
        max_length=30,
        title="Input value to be converted to UPPER case.",
        description="Provide valid string for 'input'."
    )


class PayloadValidator:
    """Payoad validator class."""
    def __init__(self, request_payload: RequestPayload) -> None:
        """Constructor."""
        logging.debug("BEGIN: RequestPayloadTransformer - Constructor")
        self.request_payload = request_payload
        print(request_payload.name)
        print(request_payload.input)
        self.empty_data(request_payload.name, "name")
        self.empty_data(request_payload.input, "input")
        self.invalid_data(request_payload.name, "name")
        self.invalid_data(request_payload.input, "input")
        logging.debug("END: RequestPayloadTransformer - Constructor")

    def empty_data(self, value: str, key: str):
        """checks if given value is null"""
        logging.debug("BEGIN: empty_data")
        if not value:
            logging.debug(f"value: {value}")
            raise HTTPException(status_code=400, detail=f"{key} can not be empty")
        logging.debug("END: empty_data")

    def invalid_data(self, value: str, key: str):
        """checks if given value is non string"""
        logging.debug("BEGIN: invalid_data")
        if not isinstance(value, str):
            logging.debug(f"value: {value}")
            raise HTTPException(status_code=400, detail=f"{key} should be string")
        logging.debug("END: invalid_data")


class RequestTransformer:
    """
    Performs operations related to Request payload.
    """
    def __init__(self, request_payload: RequestPayload) -> None:
        """Constructor."""
        logging.debug("BEGIN: RequestPayloadTransformer - Constructor")
        self.request_payload = request_payload
        PayloadValidator(self.request_payload)
        logging.debug("END: RequestPayloadTransformer - Constructor")

    def to_upper_case(self) -> RequestPayload:
        """
        Changes the given value's case to upper case.
        """
        logging.debug(f"to_upper_case: {self.request_payload}")
        self.request_payload.input = self.request_payload.input.upper()
        return self.request_payload


request_payload = RequestPayload(name="Wheel POC", input="Creation of wheel")
obj = RequestTransformer(request_payload=request_payload)
res = obj.to_upper_case()
print(f"res: {res}")
