from app import app

import os

if __name__ == '__main__':
	app.run(threaded=True, debug=True, port=8080)