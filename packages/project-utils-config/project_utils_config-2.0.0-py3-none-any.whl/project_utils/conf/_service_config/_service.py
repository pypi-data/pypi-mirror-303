from ._base import BaseServiceConfig


class ServiceConfig(BaseServiceConfig):
    @classmethod
    def __new__(cls, *args, **kwargs):
        return cls.create_instance()


if __name__ == '__main__':
    print(ServiceConfig("0.0.0.0", "8080"))
    print(ServiceConfig("0.0.0.0", "8081"))
    print(ServiceConfig("0.0.0.0", "8082"))
