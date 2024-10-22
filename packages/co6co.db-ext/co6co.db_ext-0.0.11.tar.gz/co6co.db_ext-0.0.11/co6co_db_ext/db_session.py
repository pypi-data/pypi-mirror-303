from sqlalchemy.ext.asyncio import create_async_engine

from contextvars import ContextVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import scoped_session, sessionmaker

# from model.pos.DbModelPo import User, Process

from sqlalchemy import select, create_engine
from sqlalchemy.orm import selectinload

import asyncio
import time
import typing
from typing import TypeVar
from co6co.utils import log
from co6co_db_ext.po import BasePO
from sqlalchemy.pool import NullPool


class db_service:
    default_settings: dict = {
        'DB_HOST': 'localhost',
        'DB_NAME': '',
        'DB_USER': 'root',
        'DB_PASSWORD': '',
        'echo': True,
        'pool_size': 20,
        'max_overflow': 10,
        'pool_pre_ping': True,  # 执行sql语句前悲观地检查db是否可用
        # 'pool_recycle':1800 #超时时间 单位s

    }
    settings = {}
    session: scoped_session  # 同步连接
    async_session_factory: sessionmaker  # 异步连接
    useAsync: bool
    poolSize: int = None
    poolSize: int = None

    def _createEngine(self, url: str):
        self.useAsync = True
        # 字符串 除了 bool(''/""/()/[]/{}/None )== False
        echo = self.settings.get("echo")
        ping = self.settings.get("pool_pre_ping")
        if type(echo) != bool:
            echo = True

        pool_size = self.settings.get("pool_size")
        max_overflow = self.settings.get("max_overflow")
        if "sqlite" in url:
            self.useAsync = False
            self.engine = create_engine(
                url, echo=echo, poolclass=NullPool, pool_pre_ping=ping)
            self.session = scoped_session(sessionmaker(
                autoflush=False, autocommit=False, bind=self.engine))
            BasePO.query = self.session.query_property()
        else:  # AsyncSession
            self.engine = create_async_engine(
                url, echo=echo, pool_size=pool_size, max_overflow=max_overflow, pool_pre_ping=ping)
            self.async_session_factory = sessionmaker(
                self.engine, expire_on_commit=False, class_=AsyncSession)  # AsyncSession,

        self.base_model_session_ctx = ContextVar("session")
        pass

    def __init__(self, config: dict, engineUrl: str = None) -> None:
        self.settings = self.default_settings.copy()
        if engineUrl == None:
            self.settings .update(config)
            engineUrl = "mysql+aiomysql://{}:{}@{}/{}".format(self.settings['DB_USER'],self.settings['DB_PASSWORD'],self.settings['DB_HOST'],self.settings['DB_NAME'])
            
        self._createEngine(engineUrl)
        pass

    async def init_tables(self):
        if self.useAsync:
            async with self.engine.begin() as conn:
                # await conn.run_sync(BasePO.metadata.drop_a顶顶顶顶ll)
                await conn.run_sync(BasePO.metadata.create_all)
                await conn.commit()
            await self.engine.dispose()
        else:
            BasePO.metadata.create_all(bind=self.engine)

    def sync_init_tables(self):
        retryTime = 0
        while (True):
            try:
                if retryTime < 8:
                    retryTime += 1
                asyncio.run(self.init_tables())
                break
            except Exception as e:
                log.warn(f"同步数据表失败{e}!")
                log.info(f"{retryTime*5}s后重试...")
                time.sleep(retryTime*5)
