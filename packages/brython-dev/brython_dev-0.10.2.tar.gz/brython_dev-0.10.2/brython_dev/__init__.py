import sysconfig
from copy import deepcopy
from pathlib import Path

import pkg_resources
import yaml
from flask import (
    Flask,
    abort,
    jsonify,
    render_template_string,
    request,
    send_from_directory,
)

try:
    __version__ = pkg_resources.get_distribution("brython-dev").version
except pkg_resources.DistributionNotFound:  # pragma: no cover
    __version__ = "unknown"


INDEX_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>{{ config["NAME"] }}</title>
    <meta charset="utf-8">
    {% for stylesheet in config["STYLESHEETS"] %}
    <link rel="stylesheet" href="{{ stylesheet }}">{% endfor %}
</head>
<body onload="brython({{ config["BRYTHON_OPTIONS"]|pretty_dict }})">
    {{ load_template()|safe }}
    {% if config["CONSOLE"] and config["EXTENSIONS"]["brython_stdlib"] %}
    <script id="console" type="text/python3">
    from interpreter import Interpreter
    import sys
    sys.stdout = sys.stderr = Interpreter()
    print("\\n")
    </script>
    {% endif %}{% for script in config["SCRIPTS"] %}
    <script type="text/javascript" src="{{ script }}"></script>{% endfor %}{% for pyscript in config["PYSCRIPTS"] %}
    <script id="{{ pyscript.split("//", 1)[-1].rsplit(".", 1)[0].replace(":", "_").replace("/", "_").replace(".", "_") }}" type="text/python3" src="{{ pyscript }}"></script>{% endfor %}
</body>
</html>
"""


def read_config_file(config_file):
    if config_file.is_file():  # pragma: no cover
        return {
            k.upper(): v for k, v in yaml.safe_load(config_file.read_text()).items()
        }
    return {}


def create_app(__config__: dict = {}) -> Flask:
    config_file = Path(__config__.pop("CONFIG_FILE", "brython.yml")).resolve()

    config = read_config_file(config_file)
    config.update(__config__)

    config.setdefault("NAME", "Unnamed")
    config.setdefault(
        "PROYECT",
        (
            config["NAME"].lower().replace("-", "_")
            if Path(config["NAME"].lower().replace("-", "_")).is_dir()
            else "."
        ),
    )
    config.setdefault("APP", "app.py")
    config.setdefault("TEMPLATE", "app.html")
    config.setdefault("PROYECT_TESTS", "tests")
    config.setdefault("APP_TESTS", "tests.py")
    config.setdefault("TEMPLATE_TESTS", "tests.html")
    config.setdefault("CONSOLE", False)
    config.setdefault("STYLESHEETS", [])
    config.setdefault("EXTENSIONS", {})
    config["EXTENSIONS"].setdefault("brython", True)
    config["EXTENSIONS"].setdefault("brython_stdlib", False)
    config.setdefault("SCRIPTS", [])
    config.setdefault("PYSCRIPTS", [])
    config.setdefault("BRYTHON_OPTIONS", {})
    config["BRYTHON_OPTIONS"].setdefault("debug", 1)
    config.setdefault("STATIC_URL", "/")

    if config["EXTENSIONS"]["brython"]:
        config["SCRIPTS"].append("/brython.js")
    if config["EXTENSIONS"]["brython_stdlib"]:
        config["SCRIPTS"].append("/brython_stdlib.js")
    if config["APP"]:
        config["PYSCRIPTS"].append(config["APP"])

    app = Flask(
        __name__,
        static_folder=Path(config["PROYECT"]).resolve(),
        static_url_path=config["STATIC_URL"],
    )

    app.config.from_mapping(config)

    @app.template_filter()
    def pretty_dict(_dict):
        return f"{{{', '.join(f'{k}: {v}' for k, v in _dict.items())}}}"

    @app.template_global()
    def load_template():
        if request.path.startswith("/tests") and app.config["TEMPLATE_TESTS"]:
            filename = Path(app.config["PROYECT_TESTS"]) / app.config["TEMPLATE_TESTS"]
        elif not request.path.startswith("/tests") and app.config["TEMPLATE"]:
            filename = Path(app.config["PROYECT"]) / app.config["APP"]
        else:
            return ""

        if not filename.exists():
            abort(404, f"{str(filename)} not exist")
        return filename.read_text()

    @app.route("/")
    def index():
        return render_template_string(INDEX_TEMPLATE)

    @app.route(f"/{app.config['NAME'].lower().replace('-', '_')}/<path:filename>")
    def proyect(filename: str):
        return send_from_directory(
            Path(app.config["NAME"].lower().replace("-", "_")).resolve(), filename
        )

    @app.route("/brython.js")
    def brythonjs():
        return send_from_directory(
            sysconfig.get_path("purelib"), "brython/data/brython.js"
        )

    @app.route("/brython_stdlib.js")
    def brythonstdlibjs():
        return send_from_directory(
            sysconfig.get_path("purelib"), "brython/data/brython_stdlib.js"
        )

    @app.route("/Lib/site-packages/<path:filename>")
    def site_packages(filename: str):
        return send_from_directory(sysconfig.get_path("purelib"), filename)

    @app.route("/tests")
    def tests():
        if "files" in request.args:
            return jsonify(
                [str(path).replace("\\", "/") for path in Path("tests").iterdir()]
            )

        old_config = deepcopy(app.config)

        if "/brython_stdlib.js" not in app.config["SCRIPTS"]:
            app.config["SCRIPTS"].append("/brython_stdlib.js")

        if app.config["APP"] and app.config["APP_TESTS"]:
            app.config["PYSCRIPTS"][
                -1
            ] = f"{app.config['PROYECT_TESTS']}/{app.config['APP_TESTS']}"
        elif app.config["APP_TESTS"]:
            app.config["PYSCRIPTS"].append(
                f"{app.config['PROYECT_TESTS']}/{app.config['APP_TESTS']}"
            )

        template = render_template_string(INDEX_TEMPLATE)
        app.config.update(old_config)
        return template

    @app.route("/tests/<path:filename>")
    def tests_lib(filename: str):
        return send_from_directory(Path("tests").resolve(), filename)

    return app
