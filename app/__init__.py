from flask import Flask

app = Flask(__name__)
from app import views


#if __name__ == "__main__":  # pragma: no cover
#    #logging.basicConfig(level=logging.NOTSET)
#    app.run( debug=True)

    #app.run(host=app.config['HOST'], port=get_port(),
    #                    debug=app.config.get('DEBUG', True))

