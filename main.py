import os
from flask import Flask
import sys




try:
    if __name__ == '__main__':
        app.run(debug=os.environ['FLASK_ENV'] == 'development',host='0.0.0.0', port=8080)
    elif __name__ == '__main__':
        app.run(debug=os.environ['FLASK_ENV'] == 'production',host='0.0.0.0', port=80)
except:
    print("setting to FLASK_ENV")