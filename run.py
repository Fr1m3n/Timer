from app import app
from app import config as cfg
import sys

app.run(debug = True, port = sys.argv[1])