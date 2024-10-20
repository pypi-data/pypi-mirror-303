from typing import Tuple

from fastapi import APIRouter, Depends, Request
from fastapi.responses import StreamingResponse
from openai import OpenAI
from openai.types.chat import ChatCompletion
from pyassorted.asyncio.executor import run_func, run_generator

from languru.server.config import ServerBaseSettings
from languru.server.deps.common import app_settings
from languru.server.deps.openai_chat import (
    depends_openai_client_chat_completion_request,
)
from languru.types.chat.completions import ChatCompletionRequest
from languru.utils.http import simple_sse_encode

router = APIRouter()


class ChatCompletionHandler:

    async def handle_request(
        self,
        request: "Request",
        *args,
        chat_completion_request: "ChatCompletionRequest",
        settings: "ServerBaseSettings",
        openai_client: "OpenAI",
        **kwargs,
    ) -> ChatCompletion | StreamingResponse:
        if chat_completion_request.stream is True:
            return await self.handle_stream(
                request=request,
                chat_completion_request=chat_completion_request,
                settings=settings,
                openai_client=openai_client,
                **kwargs,
            )
        else:
            return await self.handle_normal(
                request=request,
                chat_completion_request=chat_completion_request,
                settings=settings,
                openai_client=openai_client,
                **kwargs,
            )

    async def handle_normal(
        self,
        request: "Request",
        *args,
        chat_completion_request: "ChatCompletionRequest",
        settings: "ServerBaseSettings",
        openai_client: "OpenAI",
        **kwargs,
    ) -> ChatCompletion:
        params = chat_completion_request.model_dump(exclude_none=True)
        params["stream"] = False
        chat_completion = await run_func(
            openai_client.chat.completions.create, **params
        )
        return chat_completion

    async def handle_stream(
        self,
        request: "Request",
        *args,
        chat_completion_request: "ChatCompletionRequest",
        settings: "ServerBaseSettings",
        openai_client: "OpenAI",
        **kwargs,
    ) -> StreamingResponse:
        params = chat_completion_request.model_dump(exclude_none=True)
        params["stream"] = True
        return StreamingResponse(
            run_generator(
                simple_sse_encode,
                await run_func(openai_client.chat.completions.create, **params),
            ),
            media_type="application/stream+json",
        )


@router.post("/chat/completions")
async def chat_completions(
    request: Request,
    openai_client_chat_completion_request: Tuple[
        OpenAI, ChatCompletionRequest
    ] = Depends(depends_openai_client_chat_completion_request),
    settings: ServerBaseSettings = Depends(app_settings),
):  # -> openai.types.chat.ChatCompletion | openai.types.chat.ChatCompletionChunk
    return await ChatCompletionHandler().handle_request(
        request=request,
        chat_completion_request=openai_client_chat_completion_request[1],
        settings=settings,
        openai_client=openai_client_chat_completion_request[0],
    )
