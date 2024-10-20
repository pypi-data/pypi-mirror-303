from fastapi import APIRouter

from languru.server.api.v1.assistants import router as assistants_router
from languru.server.api.v1.audio import router as audio_router
from languru.server.api.v1.chat import router as chat_router
from languru.server.api.v1.completions import router as completions_router
from languru.server.api.v1.embeddings import router as embeddings_router
from languru.server.api.v1.images import router as images_router
from languru.server.api.v1.model import router as model_router
from languru.server.api.v1.moderations import router as moderations_router
from languru.server.api.v1.threads import router as threads_router

router = APIRouter()


router.include_router(router=model_router, tags=["model"])
router.include_router(router=chat_router, tags=["chat"])
router.include_router(router=completions_router, tags=["completions"])
router.include_router(router=embeddings_router, tags=["embeddings"])
router.include_router(router=moderations_router, tags=["moderations"])
router.include_router(router=audio_router, tags=["audio"])
router.include_router(router=images_router, tags=["images"])
router.include_router(router=assistants_router, tags=["assistants"])
router.include_router(router=threads_router, tags=["threads"])
