from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.database import get_async_session
from src.auth.manager import get_user_manager
from src.auth.auth import auth_backend
from src.auth.models import User
from src.notes.models import Record, Tag, TagsRecord

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend]
)
current_user = fastapi_users.current_user()

router = APIRouter(
    prefix="/notes",
    tags=["notes"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_records(current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    query_records = select(Record).where(Record.auther == current_user.id)
    result = await session.execute(query_records)
    records =  result.scalars().all()
    record_id_list = [rec.id for rec in records]
    query_tags = (select(Tag.tag_name, TagsRecord.record_id)
                  .join(TagsRecord, TagsRecord.tag_id == Tag.id)
                  .where(TagsRecord.record_id.in_(record_id_list)))
    result = await session.execute(query_tags)
    tags =  result.all()  
    tags_by_record = {}
    for tag in tags:
        if tag[1] not in tags_by_record:
            tags_by_record[tag[1]] = []
        tags_by_record[tag[1]].append(tag[0])
    return [{
        "id": rec.id,
        "auther": rec.auther,
        "title": rec.title,
        "content": rec.content,
        "tags": tags_by_record[rec.id],
        "created_at": rec.created_at
    } for rec in records]

@router.post("/")
async def create_record(data:dict, current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    new_record = Record(
        auther = current_user.id,
        title = data["title"],
        content = data["content"]
    )
    session.add(new_record)
    session.flush()
    tags_query = select(Tag)
    all_tags = (await session.execute(tags_query)).scalars().all()
    tags = {tag.tag_name : tag.id  for tag in all_tags}
    for tag in data["tags"]:
        if tag not in tags:
            new_tag = Tag(tag_name=tag)
            session.add(new_tag)
    tags_id_query = select(Tag.id).where(Tag.tag_name.in_(data["tags"]))
    tags_id = (await session.execute(tags_id_query)).scalars().all()
    for tag_id in tags_id:
        session.add(TagsRecord(tag_id=tag_id, record_id=new_record.id))
    await session.commit()

@router.delete("/{record_id}")
async def delete_record(record_id: int, current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    query = select(Record).where(Record.id == record_id, Record.auther == current_user.id)
    result = await session.execute(query)
    record = result.scalar_one_or_none()
    if not record:
        return {"message": "Not found"}
    await session.delete(record)
    await session.commit()
    return {"message": "OK"}

@router.patch("/{record_id}")
async def update_record(record_id: int, data:dict, current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    query = select(Record).where(Record.id == record_id, Record.auther == current_user.id)
    result = await session.execute(query)
    record = result.scalar_one_or_none()
    if not record:
        return {"message": "Not found"}
    record.title = data["title"]
    record.content = data["content"]
    await session.commit()
    return {"message": "OK"}

@router.get("/tags")
async def search_tags(tags:str, session: AsyncSession = Depends(get_async_session)):
    query = select(TagsRecord.record_id).join(Tag, Tag.id == TagsRecord.tag_id).where(Tag.tag_name.in_(tags.strip().lstrip("#").split("#")))
    result = await session.execute(query)
    record_ids = result.scalars().all()
    query = select(Record).where(Record.id.in_(record_ids))
    result = await session.execute(query)
    records = result.scalars().all()
    record_id_list = [rec.id for rec in records]
    query_tags = (select(Tag.tag_name, TagsRecord.record_id)
                  .join(TagsRecord, TagsRecord.tag_id == Tag.id)
                  .where(TagsRecord.record_id.in_(record_id_list)))
    result = await session.execute(query_tags)
    tags =  result.all()  
    tags_by_record = {}
    for tag in tags:
        if tag[1] not in tags_by_record:
            tags_by_record[tag[1]] = []
        tags_by_record[tag[1]].append(tag[0])
    return [{
        "id": rec.id,
        "auther": rec.auther,
        "title": rec.title,
        "content": rec.content,
        "tags": tags_by_record[rec.id],
        "created_at": rec.created_at
    } for rec in records]
