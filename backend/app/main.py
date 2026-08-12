from collections.abc import AsyncIterator
from typing import Any

from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import SessionLocal

app = FastAPI(title="Scattershot Application Tracker")

async def get_session() -> AsyncIterator[AsyncSession]:
    async with SessionLocal() as session:
        yield session

@app.get("/api/health")
async def health(session: AsyncSession = Depends(get_session)) -> dict[str, Any]:
    result = await session.execute(text("select 1"))
    return {"status" : "ok", "db" : result.scalar_one()}