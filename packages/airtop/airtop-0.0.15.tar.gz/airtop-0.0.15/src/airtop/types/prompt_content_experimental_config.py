# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class PromptContentExperimentalConfig(UniversalBaseModel):
    include_visual_analysis: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="includeVisualAnalysis")
    ] = pydantic.Field(default=None)
    """
    If set to 'enabled', Airtop AI will also analyze the web page visually when fulfilling the request. Note that this can add to both the execution time and cost of the operation. If the page is too large, the context window can be exceeded and the request will fail. If set to 'auto' or 'disabled', no visual analysis will be conducted. If 'followPaginationLinks' is set to true, visual analysis will be conducted unless 'includeVisualAnalysis' is explicitly set to 'disabled'.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
