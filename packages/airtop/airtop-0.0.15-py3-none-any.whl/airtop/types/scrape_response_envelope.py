# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from .scrape_response_output import ScrapeResponseOutput
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class ScrapeResponseEnvelope(UniversalBaseModel):
    model_response: typing_extensions.Annotated[ScrapeResponseOutput, FieldMetadata(alias="modelResponse")] = (
        pydantic.Field()
    )
    """
    The response from the Airtop AI model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
