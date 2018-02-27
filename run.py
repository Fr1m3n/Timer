from app import app
from app import config as cfg

app.run(debug = True, port = cfg.PORT)