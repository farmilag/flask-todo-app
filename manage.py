from flask.cli import FlaskGroup
from flask_migrate import Migrate
from werkzeug.serving import run_simple

from application import create_app
from application.extensions import db

app = create_app()
Migrate(app, db)
cli = FlaskGroup(create_app=lambda: app)


@cli.command()
def runserver():
    """Start the development server on port 7345."""
    run_simple("127.0.0.1", 7345, app)


if __name__ == "__main__":
    cli()
