import json
import os
import uuid
from html.parser import HTMLParser
from al360_tai_core_flask import FlaskHelper
from al360_taiutils.data_processing import serialize_json_safe
from al360_taiwidgets.interfaces import WidgetRequestResponseConstants
from flask import Flask
from flask_cors import CORS

invalid_feature_flights_error = (
    "feature_flights should be of type string. Separate multiple flights using ampersand (&)."
)


class InLineScript(HTMLParser):
    def __init__(self, load_widget_file):
        super().__init__()
        self.content = ""
        self.load_widget_file = load_widget_file

    def handle_starttag(self, tag, attrs):
        if tag == "script":
            src = None
            scriptTag = "<script"
            for att in attrs:
                if att[0] == "src":
                    src = att[1]
                    continue
                # Skip module type to avoid height rendering issues
                if att[0] == "type":
                    continue
                scriptTag += f' {att[0]}="{att[1]}"'
            scriptTag += '>'
            if src is not None:
                content = self.load_widget_file(src)
                self.content += f'{scriptTag}\r\n{content}\r\n</script>\r\n'
                return
        self.content += self.get_starttag_text()

    def handle_endtag(self, tag):
        self.content += f'</{tag}>'

    def handle_data(self, data):
        self.content += data


class Dashboard:
    """The dashboard class, wraps the dashboard component."""

    def __init__(self, *,
                 dashboard_type,
                 model_data,
                 public_ip,
                 port,
                 locale,
                 no_inline_dashboard=False,
                 is_private_link=False,
                 **kwargs):
        """Initialize the dashboard."""
        if model_data is None or dashboard_type is None:
            raise ValueError("Required parameters not provided")

        try:
            self._service = FlaskHelper(ip=public_ip,
                                        port=port,
                                        is_private_link=is_private_link)

            # Enable CORS for the dashboard app
            CORS(self._service.app, resources={r"/*": {"origins": ["http://localhost:3000"]}}, supports_credentials=True)

            # Add headers to allow embedding in iframe
            @self._service.app.after_request
            def add_header(response):
                response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
                response.headers['Access-Control-Allow-Credentials'] = 'true'
                response.headers['Content-Security-Policy'] = "frame-ancestors 'self' http://localhost:3000"
                return response

        except Exception as e:
            self._service = None
            raise e

        self.id = uuid.uuid4().hex
        self.feature_flights = kwargs.get('feature_flights')
        
        if self.feature_flights and not isinstance(self.feature_flights, str):
            raise ValueError(invalid_feature_flights_error)

        self.config = {
            'dashboardType': dashboard_type,
            'id': self.id,
            'baseUrl': self._service.env.base_url,
            'withCredentials': self._service.with_credentials,
            'locale': locale,
            'featureFlights': self.feature_flights
        }

        self.model_data = model_data
        self.add_route()

        # Load and display the dashboard HTML
        html = self.load_index()
        print(f'{dashboard_type} started at {self._service.env.base_url}')
        
        if not no_inline_dashboard:
            self._service.env.display(html)

    def add_route(self):
        """Add routes to serve dashboard resources."""
        def index():
            print("Serving dashboard index page")
            return self.load_index()

        self.add_url_rule(index, '/', methods=["GET"])

        def get_config():
            return json.dumps({WidgetRequestResponseConstants.data: self.config})
        
        self.add_url_rule(get_config, '/config', methods=["POST"])

        def get_model_data():
            return json.dumps({
                WidgetRequestResponseConstants.data: self.model_data},
                default=serialize_json_safe)
        
        self.add_url_rule(get_model_data, '/model_data', methods=["POST"])

    @staticmethod
    def get_widget_path(path):
        """Return the path to a widget resource."""
        script_path = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(script_path, "widget", path)

    def load_index(self):
        """Load the main HTML for the dashboard."""
        index = self.load_widget_file("index.html")
        parser = InLineScript(self.load_widget_file)
        parser.feed(index)
        return parser.content

    def load_widget_file(self, path):
        try:
            js_path = Dashboard.get_widget_path(path)
            with open(js_path, "r", encoding="utf-8") as f:
                content = f.read()
                content = content.replace("__al360_tai_app_id__", f'al360_tai_widget_{self.id}')
                content = content.replace('"__al360_tai_config__"', f'`{json.dumps(self.config)}`')
                model_data = json.dumps(self.model_data, default=serialize_json_safe)
                content = content.replace('"__al360_tai_model_data__"', f'`{model_data}`')
                return content
        except FileNotFoundError:
            raise FileNotFoundError(f"Widget file {path} not found in the 'widget' directory.")

    def add_url_rule(self, func, route, methods):
        func.__name__ = func.__name__ + str(id(self))
        self._service.app.add_url_rule(
            route,
            endpoint=func.__name__,
            view_func=func,
            methods=methods
        )
