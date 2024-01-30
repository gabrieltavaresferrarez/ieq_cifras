from ieq_cifras import create_app
from config import settings

app = create_app(settings)

app.run(port=settings['FLASK_RUN_PORT'], debug=True)