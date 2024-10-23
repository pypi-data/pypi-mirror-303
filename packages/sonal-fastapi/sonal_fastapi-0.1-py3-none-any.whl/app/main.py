
from fastapi import FastAPI, HTTPException
from app.utils.payload_schema import InputPayload
from app.utils.validator import ValidationHandler
from app.transformer import LogicProcessor
from app.utils.db_client import dbClient
from fastapi.exceptions import RequestValidationError
import logging

Fastapp = FastAPI()
# Custom exception handler
Fastapp.add_exception_handler(RequestValidationError, ValidationHandler.validation_exception_handler)

class uppercase:
    # API endpoint to handle POST requests
    @Fastapp.post("/upper_input_payload")
    async def uppercase_data(payload: InputPayload):
        logging.debug("BEGIN:upper_input_payload")
        try:
            # Process the request data using logic from logic.py
            upper_input = LogicProcessor.process_uppercase_data(payload)
            logging.debug("END:upper_input_payload")
            return upper_input
        except Exception as e:
            # Catch all other exceptions
            logging.error(f"error retrieving secret: {e}")
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

    #Endpoint to handle get requests
    @Fastapp.get("/retrive_secrets/")
    async def retrive_secret(name:str):
        logging.debug("BEGIN:retrive_secret")
        try:
            #Process the request data
            dbClient.get_secret()
            logging.debug("END:retrive_secret")
            return {
                "name":name,
                "message": "Secret retrived successfully"
            }
        except Exception as e:
            #Catch all other exceptions
            logging.error(f"error retrieving secret: {e}")
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
