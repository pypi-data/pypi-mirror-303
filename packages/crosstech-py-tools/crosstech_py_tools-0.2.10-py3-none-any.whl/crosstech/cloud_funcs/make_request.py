from flask import Flask
from typing import Callable, Any
from werkzeug.test import EnvironBuilder


def make_request(*, func: Callable, **kwargs) -> Any:
    """
    Wrapper for sending a request to a Flask app. Useful for testing.
    
    Parameters:
    -----------
        func: Callable 
            The function to test.
        kwargs: 
            Keyword arguments to pass to EnvironBuilder.
    
            method: str 
                The HTTP method to use. GET / POST / PUT / DELETE etc. Default is "GET".
            path: str
                The path to request. Default is "/".
            query_string: str
                The query string to use. Default is None.
            headers: dict
                The headers to use. Default is None.
            data: str
                The request body. Make sure to use `json.dumps` to turn into string. Default is None. 
                ```python
                data = json.dumps({"key": "value"})
                ```
            content_type: str
                The content type to use. Default is None.
    """
    app = Flask(__name__)
    
    builder = EnvironBuilder(**kwargs)
    
    with app.app_context():
        return func(builder.get_request())
