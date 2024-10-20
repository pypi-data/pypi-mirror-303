from fastapi import APIRouter
from sqlmodel import Field, SQLModel, select

from mtmai.deps import SessionDep
from mtmai.mtlibs import mtutils

router = APIRouter()


class Workspace(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    title: str = Field(index=True)


@router.post("")
def create_workspace(ws: Workspace, db: SessionDep):
    ws.id = mtutils.gen_orm_id_key()
    if not hasattr(ws, "title"):
        ws.title = "example title"

    db.add(ws)
    db.commit()
    db.refresh(ws)
    return ws


@router.get("/workspace", response_model=list[Workspace])
def items(db: SessionDep):
    return db.exec(select(Workspace)).all()


@router.get("/workspace/{id}", response_model=Workspace)
def get_one(id: str, db: SessionDep):
    statement = select(Workspace).where(Workspace.id == id)
    results = db.exec(statement)
    item = results.one_or_none()
    print("item:", item)
    return item
