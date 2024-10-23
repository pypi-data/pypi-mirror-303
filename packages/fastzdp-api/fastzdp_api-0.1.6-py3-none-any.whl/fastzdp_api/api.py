from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List


class Api(FastAPI):
    """API接口核心类"""

    def run(
            self,
            host: str = "0.0.0.0",
            port: int = 8888,
            allow_origins: List[str] = None,
            allow_methods: List[str] = None,
            allow_headers: List[str] = None,
    ):
        """运行程序"""
        # 运行之前, 添加跨域中间件
        if allow_origins is None:
            allow_origins = ["*"]
        if allow_methods is None:
            allow_methods = ["*"]
        if allow_headers is None:
            allow_headers = ["*"]
        self.add_middleware(
            CORSMiddleware,
            allow_origins=allow_origins,
            allow_credentials=True,
            allow_methods=allow_methods,
            allow_headers=allow_headers,
        )

        # 运行
        import uvicorn
        uvicorn.run(self, host=host, port=port)
