from webplane import WebApp


class MyApp:

    def index(self):
        return "Hello world"


application = WebApp(MyApp).run()
