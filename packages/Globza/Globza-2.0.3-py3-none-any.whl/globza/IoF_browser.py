# IoF_browser.py (for Internet of Functions)
# Version 2.0.3
# author: © Sergei Sychev, 2024 , see also free of charge LICENSE.txt

"""
This module provides the IoF class to interact with the Internet of functions (IoF).
The class dynamically handles function calls to remote services by generating methods on-the-fly,
converting argument types as needed, and handling HTTP requests and responses. It also allows
for registering new functions with the IoF.

Classes:
    IoF: A class to handle function registration and invocation for the IoF.
"""

import requests
import uuid


class IoF:
    """
    A class to interact with the IoF for function registration and invocation.

    This class handles dynamic creation of methods corresponding to registered functions
    and manages HTTP requests to invoke these functions. It also handles converting the types
    of function arguments and results using specified metadata.

    Attributes:
        base_url (str): The base URL of the cloud service.
    """

    def __init__(self, base_url='https://apiwwf-production.up.railway.app/'):
        """
        Initializes the IoF class with a base URL for the cloud service.

        Parameters:
            base_url (str): The base URL of the cloud service. Defaults to a specific production URL.
        """
        self.base_url = base_url

    def __getattr__(self, function_name):
        """
        Dynamically creates a method corresponding to the called function name.

        This method allows the IoF class to handle arbitrary function calls by generating
        a callable method that sends a request to the corresponding endpoint on the cloud service.

        Parameters:
            function_name (str): The name of the function being called.

        Returns:
            method (function): A method that, when called, sends a request to the cloud service.
        """

        def method(*args, **kwargs):
            """
            Sends a request to invoke a remote function with the provided arguments.

            This method constructs a request with the function's arguments, sends it to the cloud service,
            handles the response, and performs type conversion if necessary.

            Parameters:
                *args: Positional arguments for the function call.
                **kwargs: Keyword arguments for the function call, including a 'types' argument to specify type conversion.

            Returns:
                dict: The response data from the function call, possibly after type conversion.
            """
            # Generate a unique request ID
            request_id = uuid.uuid4().hex
            # Construct the URL for the function
            url = f"{self.base_url}/{function_name}"

            # Extract 'types' for type conversion
            types = kwargs.pop('types', {})
            types_str = {key: value.__name__ for key, value in types.items()}

            # Convert non-serializable keyword arguments to strings
            for key, value in kwargs.items():
                if not isinstance(value, (str, int, float, bool, type(None))):
                    kwargs[key] = str(value)

            # Prepare the payload for the request
            payload = {'request_id': request_id, 'args': args, 'kwargs': kwargs, 'types': types_str}

            try:
                # Send a POST request to the IoF
                response = requests.post(url, json=payload)
                response.raise_for_status()  # Raise an error for bad responses
                result = response.json()
                data = result.get('data', None)

                # Convert the response data using specified types
                if data and isinstance(data, dict):  # Check if data is a dictionary
                    for key, type_func in types.items():
                        if key in data:
                            data[key] = type_func(data[key])

                return data

            except requests.exceptions.HTTPError as e:
                return {'error': 'HTTP error', 'message': str(e)}
            except requests.exceptions.RequestException as e:
                return {'error': 'Request error', 'message': str(e)}
            except ValueError as e:
                return {'error': 'Decode error', 'message': str(e)}
            except Exception as e:
                return {'error': 'Unexpected error', 'message': str(e)}

        return method

    def to_register_function(self, id, function=None, metadata=None):
        """
        Registers a function using IoF.

        Parameters:
            id (str): Unique identifier for the function.
            metadata (dict): Metadata for registering a function, including:
                - 'location' (URL): Required function URL.
                - 'http_method' (str, optional): Request method, default is 'POST'.
                - 'description' (str, optional): Description of the function.

        Returns:
            dict: Response from the server with the result of registration or update.
        """
        # Check that 'location' is specified in the metadata
        if 'location' not in metadata:
            raise ValueError("The 'location' (URL) must be specified in the metadata.")

        # Assign a default value to 'http_method' if not specified
        if 'http_method' not in metadata:
            metadata['http_method'] = 'POST'

        url = f"{self.base_url}/register_function"
        payload = {'id': id, 'metadata': metadata}

        # Send a POST request to register a function
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Check

        return response.json()

    def to_call_function(self, id, *args, **kwargs):
        """
        Calls a registered function by its identifier with provided arguments.

        This method allows for direct invocation of a registered function using its ID,
        passing any required positional and keyword arguments.

        Parameters:
            id (str): The unique identifier of the function to be called.
            *args: Positional arguments to pass to the function.
            **kwargs: Keyword arguments to pass to the function.

        Returns:
            dict: The response data from the function call.
        """
        return self.__getattr__(id)(*args, **kwargs)


iof = IoF()
