from typing import Any

from fastapi import APIRouter

from mtmai.core.logging import get_logger
from mtmai.crud.curd_search import search_list
from mtmai.deps import AsyncSessionDep, CurrentUser
from mtmai.models.search_index import SearchIndexResponse, SearchRequest

router = APIRouter()
logger = get_logger()
sql_schema = """
CREATE TABLE search_index (
    id SERIAL PRIMARY KEY,
    type VARCHAR(50) NOT NULL,  -- 'site', 'thread', 'task' 等
    title TEXT NOT NULL,
    content TEXT,
    url TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    search_vector tsvector
);

CREATE INDEX search_vector_idx ON search_index USING GIN (search_vector);
"""
# 创建一个触发器函数来自动更新 search_vector：
sql_trigger = """
CREATE FUNCTION search_vector_update() RETURNS trigger AS $$
BEGIN
    NEW.search_vector :=
        setweight(to_tsvector('english', COALESCE(NEW.title, '')), 'A') ||
        setweight(to_tsvector('english', COALESCE(NEW.content, '')), 'B');
    RETURN NEW;
END
$$ LANGUAGE plpgsql;

CREATE TRIGGER search_vector_update
BEFORE INSERT OR UPDATE ON search_index
FOR EACH ROW EXECUTE FUNCTION search_vector_update();
"""


@router.post("/", response_model=SearchIndexResponse)
async def search(
    session: AsyncSessionDep, current_user: CurrentUser, req: SearchRequest
) -> Any:
    """
    综合搜索, 支持搜索站点, 文档, 知识库。返回搜索结果的摘要条目。
    前端，通常点击条目后，打开详细操作页
    参考： https://www.w3cschool.cn/article/34124192.html

    TODO: 可以考虑添加高亮显示的功能。
    """
    return await search_list(session, req)
