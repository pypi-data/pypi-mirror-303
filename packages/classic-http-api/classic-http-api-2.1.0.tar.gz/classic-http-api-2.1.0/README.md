# Classic HTTP Api

Этот пакет содержит вариант HTTP API, совместимый с принципами Ioc и DI.
Является оберткой над фреймворком
[Falcon](https://falcon.readthedocs.io/en/stable/index.html), 
позволяющей описывать входные и выходные параметр входных точек с помощью
[msgspec][https://jcristharif.com/msgspec/index.html], и предстоявлящей 
интеграцию с OpenAPI и Swagger.

Пример:

```python
from falcon import Request, Response
from classic.components import component
from classic.http_api import App, specification
import msgspec


# Описывает параметры запроса для GET /api/some_obj
class SomeObjFilter(msgspec.Struct):
    number: int


# Описывает структуру ответа
class SomeObj(msgspec.Struct):
    some_attr: int


# Описывает структуру запроса для POST /api/some_obj
class CreateSomeObjRequest(msgspec.Struct):
    some_attr: int


@component
class SomeObjResource:

    @specification(query=SomeObjFilter, response=SomeObj)
    def on_get(self, request: Request, response: Response):
        # Представим себе, что объекты берутся из БД
        response.media = [
            SomeObj(number)
            for number in range(
                # Объект запроса содержится в контексте под именем media.
                request.context.media.number,
            )
        ]

    @specification(media=CreateSomeObjRequest, response=SomeObj)
    def on_post(self, request: Request, response: Response):
        # Представим себе, что объект был сохранен в БД;)
        response.media = SomeObj(
            **msgspec.structs.asdict(request.context.media)
        )


# Композит
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    app = App(openapi=True)
    app.add_route('/api/some_obj', SomeObjResource())

    # 
    with make_server('', 8000, app) as httpd:
        httpd.serve_forever()

```
