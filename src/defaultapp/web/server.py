from defaultapp.web.app import create_app


def run_uwsgi(env: str):
    pass


def run_flask(env: str):
    app = create_app(env)
    app.run(debug=True)


if __name__ == '__main__':
    run_flask('test')
