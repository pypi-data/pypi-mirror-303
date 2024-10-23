from typing import List
from fastapi.middleware.cors import CORSMiddleware

def add_cors_middleware(
        app,
        allow_origins: List[str] = None,
        allow_methods: List[str] = None,
        allow_headers: List[str] = None,
):
    """添加跨域中间件"""
    # 运行之前, 添加跨域中间件
    if allow_origins is None:
        allow_origins = ["*"]
    if allow_methods is None:
        allow_methods = ["*"]
    if allow_headers is None:
        allow_headers = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=True,
        allow_methods=allow_methods,
        allow_headers=allow_headers,
    )
