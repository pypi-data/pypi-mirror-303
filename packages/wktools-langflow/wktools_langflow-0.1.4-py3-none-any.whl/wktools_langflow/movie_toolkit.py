"""Tool for the Movie API (popular, now playing)."""

from typing import Optional, Type

from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.tools import BaseTool

from wktools_langflow.wrapper.tmdb_wrapper import TMDBWrapper


class MovieQueryInput(BaseModel):
    """Input for the MovieQuery tool."""

    query: str = Field(description="query to look up on movie")
    # region(ISO 3166-1)
    region: str = Field(description="region to look up on movie in ISO 3166-1 format", default="us")


class MovieQueryRun(BaseTool):
    """Tool that search movie, now playing, popular."""

    name: str = "movie"
    description: str = (
        "A wrapper for movie. "
        "Useful for when you need to answer questions about current movies. "
        "Now playing, popular, or search by movie name. "
    )
    api_wrapper: TMDBWrapper

    args_schema: Type[BaseModel] = MovieQueryInput

    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the Wikipedia tool."""
        input_data = self.args_schema(query=query)  # Create an instance of MovieQueryInput
        return self.api_wrapper.get_movie_popular(region=input_data.region)


