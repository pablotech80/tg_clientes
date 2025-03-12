from tg import AppConfig

def make_app(global_conf, **app_conf):
    app_config = AppConfig(minimal=True, root_controller=None)
    return app_config.make_wsgi_app()
