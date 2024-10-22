from multiprocessing.managers import DictProxy
from sanic import Sanic, Request


class CacheManage:
    app: Sanic = None

    @staticmethod
    def getApp():
        app = Sanic.get_app()
        return app

    @staticmethod
    def session(request: Request):
        return request.ctx.session

    def __init__(self, app: Sanic) -> None:
        self.app = app
        pass

    @property
    def cache(self) -> DictProxy:
        """
        缓存
        """
        return self.app.shared_ctx.cache

    @property
    def dbservice(self):
        return self.app.ctx.service

    def setCache(self, key: str, value: any):
        """
        设置数据缓存
        """
        self.cache[key] = value

    def getCache(self, key: str):
        """
        获取数据缓存
        """
        if key in self.cache:
            return self.cache[key]
        return None

    def exist(self, key: str):
        """
        是否存在
        """
        return key in self.cache

    def remove(self, key: str):
        """
        移除缓存 key
        return key对应的值,没有返回空 
        """
        # del my_dict['b']  key 可以必须存在， KeyError 异常
        return self.cache.pop(key, None)
