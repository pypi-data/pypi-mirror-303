from typing import Literal, Optional, Text

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi import Path as QueryPath
from fastapi import Query, Request
from openai.types.beta.assistant import Assistant
from openai.types.beta.assistant_deleted import AssistantDeleted
from pyassorted.asyncio.executor import run_func

from languru.exceptions import NotFound
from languru.resources.sql.openai.backend import OpenaiBackend
from languru.server.config import ServerBaseSettings
from languru.server.deps.common import app_settings
from languru.server.deps.openai_backend import depends_openai_backend
from languru.types.openai_assistants import (
    AssistantCreateRequest,
    AssistantUpdateRequest,
)
from languru.types.openai_page import OpenaiPage

router = APIRouter()


# https://platform.openai.com/docs/api-reference/assistants/listAssistants
@router.get("/assistants")
async def list_assistants(
    request: Request,
    after: Optional[Text] = Query(
        None,
        description="`after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.",  # noqa: E501
    ),
    before: Optional[Text] = Query(
        None,
        description="`before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.",  # noqa: E501
    ),
    limit: int = Query(
        20,
        ge=1,
        le=100,
        description="A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.",  # noqa: E501
    ),
    order: Optional[Literal["asc", "desc"]] = Query(
        None,
        description="Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.",  # noqa: E501
    ),
    settings: ServerBaseSettings = Depends(app_settings),
    openai_backend: OpenaiBackend = Depends(depends_openai_backend),
) -> OpenaiPage[Assistant]:
    """List all assistants."""

    assistants = await run_func(
        openai_backend.assistants.list,
        after=after,
        before=before,
        limit=limit,
        order=order,
    )
    return OpenaiPage(
        data=assistants,
        object="list",
        first_id=assistants[0].id if assistants else None,
        last_id=assistants[-1].id if assistants else None,
        has_more=len(assistants) >= limit,
    )


# https://platform.openai.com/docs/api-reference/assistants/createAssistant
@router.post("/assistants")
async def create_assistant(
    request: Request,
    assistant_create_request: AssistantCreateRequest = Body(
        ...,
        description="The request to create an assistant.",
        openapi_examples={
            "math_tutor": {
                "summary": "Math Tutor",
                "value": {
                    "model": "gpt-4o-mini",
                    "instructions": "You are a personal math tutor. Respond briefly and concisely to the user's questions.",  # noqa: E501
                    "name": "Math Tutor",
                    "response_format": "none",
                    "temperature": 0.7,
                },
            }
        },
    ),
    settings: ServerBaseSettings = Depends(app_settings),
    openai_backend: OpenaiBackend = Depends(depends_openai_backend),
) -> Assistant:
    """Create an assistant."""

    try:
        assistant = await run_func(
            openai_backend.assistants.create,
            assistant_create_request.to_assistant(),
        )
        return assistant
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# https://platform.openai.com/docs/api-reference/assistants/getAssistant
@router.get("/assistants/{assistant_id}")
async def get_assistant(
    request: Request,
    assistant_id: Text = QueryPath(..., description="The ID of the assistant."),
    settings: ServerBaseSettings = Depends(app_settings),
    openai_backend: OpenaiBackend = Depends(depends_openai_backend),
) -> Assistant:
    """Retrieve an assistant by ID."""

    try:
        assistant = await run_func(openai_backend.assistants.retrieve, assistant_id)
        return assistant
    except NotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# https://platform.openai.com/docs/api-reference/assistants/modifyAssistant
@router.post("/assistants/{assistant_id}")
async def update_assistant(
    request: Request,
    assistant_id: Text = QueryPath(..., description="The ID of the assistant."),
    assistant_update_request: AssistantUpdateRequest = Body(
        ...,
        description="The request to update an assistant.",
    ),
    settings: ServerBaseSettings = Depends(app_settings),
    openai_backend: OpenaiBackend = Depends(depends_openai_backend),
) -> Assistant:
    """Update an assistant by ID."""

    try:
        assistant = await run_func(
            openai_backend.assistants.update,
            assistant_id,
            description=assistant_update_request.description,
            instructions=assistant_update_request.instructions,
            metadata=assistant_update_request.metadata,
            name=assistant_update_request.name,
            response_format=assistant_update_request.response_format,
            temperature=assistant_update_request.temperature,
            tool_resources=assistant_update_request.tool_resources,
            tools=assistant_update_request.tools,
            top_p=assistant_update_request.top_p,
        )
        return assistant
    except NotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# https://platform.openai.com/docs/api-reference/assistants/deleteAssistant
@router.delete("/assistants/{assistant_id}")
async def delete_assistant(
    request: Request,
    assistant_id: Text = QueryPath(..., description="The ID of the assistant."),
    settings: ServerBaseSettings = Depends(app_settings),
    openai_backend: OpenaiBackend = Depends(depends_openai_backend),
) -> AssistantDeleted:
    """Delete an assistant by ID."""

    try:
        assistant_deleted = await run_func(
            openai_backend.assistants.delete, assistant_id
        )
        return assistant_deleted
    except NotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
