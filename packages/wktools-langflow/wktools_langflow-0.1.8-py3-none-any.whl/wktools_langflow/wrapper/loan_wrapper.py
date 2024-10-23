from typing import Dict

from langchain_core.utils import get_from_dict_or_env
from pydantic.v1 import root_validator, BaseModel
from tmdbv3api import TMDb, Movie
import requests


class LoanWrapper(BaseModel):
    openai_api_key: str
    user_id: str

    class Config:
        extra = "forbid"

    def get_user_loan_profiles(self):
        url = f"http://localhost:8000/api/loans/user/{self.user_id}"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            print(response.json())
            return response
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
