from gunicorn import FrameworkApp

def create_app():
    app = FrameworkApp()
    # data = b"Hello, World!\n"
    # start_response("200 OK", [
    #     ("Content-Type", "text/plain"),
    #     ("Content-Length", str(len(data)))
    # ])
    # return iter([data, b"whatup"])
    return app


# def app(environ, start_response):
#     data = b"Hello, World!\n"
#     start_response("200 OK", [
#         ("Content-Type", "text/plain"),
#         ("Content-Length", str(len(data)))
#     ])
#     return iter([data, b"whatup"])
