# -*- coding: utf8 -*-
from app.core import create_app

if __name__ == "__main__":
    app = create_app()

    app.run(host=app.config['HOST'], port=app.config['PORT'],
        debug=app.config.get('DEBUG', True))

    app.logger.debug('llamado directamente a run')
else:
    app = create_app()

    app.logger.debug('llamado por referencia')
