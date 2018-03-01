from app import app
from app import config as cfg
import sys

app.run(debug = True, port = int(sys.argv[1]))
