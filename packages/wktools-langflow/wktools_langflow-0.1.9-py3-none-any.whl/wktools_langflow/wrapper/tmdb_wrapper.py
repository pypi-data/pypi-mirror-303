from typing import Dict

from langchain_core.utils import get_from_dict_or_env
from pydantic.v1 import root_validator, BaseModel
from tmdbv3api import TMDb, Movie
import requests


class TMDBWrapper(BaseModel):
    openai_api_key: str
    tmdb_api_key: str

    class Config:
        extra = "forbid"

    # noinspection PyMethodParameters
    @root_validator(pre=True)
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that api key and endpoint exists in environment."""
        tmdb_api_key = get_from_dict_or_env(
            values, "tmdb_api_key", "TMDB_API_KEY"
        )
        values["tmdb_api_key"] = tmdb_api_key

        openai_api_key = get_from_dict_or_env(
            values, "openai_api_key", "OPENAI_API_KEY"
        )
        values["openai_api_key"] = openai_api_key

        return values

    # region(ISO 3166-1)
    def get_movie_now_playing(self, max_results: int = 5, max_snippet_length: int = 100, region=None):
        tmdb = TMDb()
        tmdb.api_key = self.tmdb_api_key
        tmdb.language = 'en'

        movie = Movie()
        new_movies = movie.now_playing(region)
        limited_results = []
        for result in new_movies:
            limited_result = {
                "snippet": result,
            }
            limited_results.append(limited_result)
        return limited_results

    # region(ISO 3166-1)
    def get_movie_popular(self, region=None):
        tmdb = TMDb()
        tmdb.api_key = self.tmdb_api_key
        tmdb.language = 'en'

        movie = Movie()
        new_movies = movie.popular(region)
        return new_movies



wrapper = TMDBWrapper(tmdb_api_key='86c9f91ac5004fa70f21db5a34b50de5', openai_api_key='empty')
now_playing = wrapper.get_movie_now_playing()
print(now_playing)
