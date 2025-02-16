from defaultapp.web.app import create_app


def run_uwsgi(env: str):
    pass


def run_flask(env: str):
    app = create_app(env)
    app.run(debug=True)
