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

    # noinspection PyMethodParameters
    @root_validator(pre=True)
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that api key and endpoint exists in environment."""
        user_id = get_from_dict_or_env(
            values, "user_id", "USER_ID"
        )
        values["user_id"] = user_id

        openai_api_key = get_from_dict_or_env(
            values, "openai_api_key", "OPENAI_API_KEY"
        )
        values["openai_api_key"] = openai_api_key

        return values


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
