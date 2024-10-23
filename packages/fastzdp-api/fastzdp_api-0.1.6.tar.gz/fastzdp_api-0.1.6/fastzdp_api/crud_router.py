from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy import Engine
from sqlmodel import SQLModel
import fastzdp_sqlmodel as fasm


def get_crud_router(
        engine: Engine,
        modelSchema: BaseModel,
        model: SQLModel,
):
    """或者增删改查的路由对象"""
    if model is None:
        return

    name = model.__name__
    path = name.lower()

    router = APIRouter(tags=[f"{name} 管理"])

    @router.post(f"/{path}", summary=f"新增 {name}")
    async def add_model_router(req_data: modelSchema):
        fasm.add(engine, model(**req_data.model_dump()))
        return None

    @router.put(f"/{path}" + "/{id}", summary=f"更新 {name}")
    async def update_model_router(id: int, req_data: modelSchema):
        model_router = fasm.get(engine, model, id)
        if not model_router:
            return JSONResponse(status_code=404, content={"error": "数据不存在"})

        fasm.update(engine, model_router, req_data.model_dump())
        return None

    @router.delete(f"/{path}" + "/{id}", summary=f"删除 {name}")
    async def delete_model_router(id: int):
        fasm.delete_id(engine, model, id)
        return None

    def _get_query_dict(key1, value1, key2, value2, key3, value3):
        """获取等值查询参数"""
        query_dict = {}
        if key1 and value1:
            query_dict[key1] = value1
        if key2 and value2:
            query_dict[key2] = value2
        if key3 and value3:
            query_dict[key3] = value3
        return query_dict

    def _get_in_dict(in_key, in_value):
        """获取in查询参数"""
        in_dict = None
        if in_key and in_value:
            in_dict = {in_key: in_value.split(",")}
        return in_dict

    @router.get(f"/{path}", summary=f"查询 {name}")
    async def get_model_router(
            page: int = 1,
            size: int = 8,
            key1: str = None,
            value1: str = None,
            key2: str = None,
            value2: str = None,
            key3: str = None,
            value3: str = None,
            in_key: str = None,
            in_value: str = None,
    ):
        """
        查询数据
        - page: 第几页
        - size: 每页数量
        - key1: 等值查询key1
        - value1: 等值查询key1对应的value
        - key2: 等值查询key2
        - value2: 等值查询key2对应的value
        - key3: 等值查询key3
        - value3: 等值查询key3对应的value
        - in_key: in查询的key
        - in_value: in查询的value
        """
        # 等值查询参数
        query_dict = _get_query_dict(key1, value1, key2, value2, key3, value3)

        # in 查询
        in_dict = _get_in_dict(in_key, in_value)

        # 执行查询
        return fasm.get_page(
            engine, model, page, size,
            query_dict=query_dict,
            in_dict=in_dict,
        )

    @router.get(f"/{path}/sum", summary=f"{name} 统计求和")
    async def get_model_sum_router(
            column: str,
            key1: str = None,
            value1: str = None,
            key2: str = None,
            value2: str = None,
            key3: str = None,
            value3: str = None,
            in_key: str = None,
            in_value: str = None,
    ):
        """
        统计某张表中某一列的总和
        - column: 列名
        - key1: 等值查询key1
        - value1: 等值查询key1对应的value
        - key2: 等值查询key2
        - value2: 等值查询key2对应的value
        - key3: 等值查询key3
        - value3: 等值查询key3对应的value
        - in_key: in查询的key
        - in_value: in查询的value
        """
        # 等值查询参数
        query_dict = _get_query_dict(key1, value1, key2, value2, key3, value3)

        # in 查询
        in_dict = _get_in_dict(in_key, in_value)

        total = fasm.get_sum(
            engine, model,
            column,
            query_dict=query_dict,
            in_dict=in_dict,
        )
        return {"value": total}

    return router
