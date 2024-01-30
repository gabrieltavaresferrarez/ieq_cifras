

def init_app(app, settings):
    for config in settings.get_config():
        app.config[config] = settings[config]