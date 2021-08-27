from flask import redirect, url_for

from schlepwise_api.api import register_api
from schlepwise_api.factory import create_app

app = create_app()
register_api(app)

@app.route('/')
@app.route('/api/')
def root():
    """
    Render the OpenAPI spec
    """
    return redirect(url_for('api.doc'))
