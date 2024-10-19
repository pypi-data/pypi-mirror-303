# The MIT License (MIT)
# Copyright © 2024 Corsali, Inc. dba Vana

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.


import base64
import json
import sys
from typing import Optional, List, Any, Dict

import pydantic

import vana


def get_size(obj, seen=None) -> int:
    """
    Recursively finds size of objects.

    This function traverses every item of a given object and sums their sizes to compute the total size.

    Args:
        obj (any type): The object to get the size of.
        seen (set): Set of object ids that have been calculated.

    Returns:
        int: The total size of the object.

    """
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, "__dict__"):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, "__iter__") and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size


def cast_int(raw: str) -> int:
    """
    Converts a string to an integer, if the string is not ``None``.

    This function attempts to convert a string to an integer. If the string is ``None``, it simply returns ``None``.

    Args:
        raw (str): The string to convert.

    Returns:
        int or None: The converted integer, or ``None`` if the input was ``None``.

    """
    return int(raw) if raw is not None else raw  # type: ignore


def cast_float(raw: str) -> float:
    """
    Converts a string to a float, if the string is not ``None``.

    This function attempts to convert a string to a float. If the string is ``None``, it simply returns ``None``.

    Args:
        raw (str): The string to convert.

    Returns:
        float or None: The converted float, or ``None`` if the input was ``None``.

    """
    return float(raw) if raw is not None else raw  # type: ignore


class TerminalInfo(pydantic.BaseModel):
    """
    TerminalInfo encapsulates detailed information about a network message (node) involved in a communication process.

    This class serves as a metadata carrier,
    providing essential details about the state and configuration of a terminal during network interactions. This is a crucial class in the Vana framework.

    The TerminalInfo class contains information such as HTTP status codes and messages, processing times,
    IP addresses, ports, Vana version numbers, and unique identifiers. These details are vital for
    maintaining network reliability, security, and efficient data flow within the Vana network.

    This class includes Pydantic validators and root validators to enforce data integrity and format. It is
    designed to be used natively within Messages, so that you will not need to call this directly, but rather
    is used as a helper class for Messages.

    Args:
        status_code (int): HTTP status code indicating the result of a network request. Essential for identifying the outcome of network interactions.
        status_message (str): Descriptive message associated with the status code, providing additional context about the request's result.
        process_time (float): Time taken by the terminal to process the call, important for performance monitoring and optimization.
        ip (str): IP address of the terminal, crucial for network routing and data transmission.
        port (int): Network port used by the terminal, key for establishing network connections.
        version (int): Vana version running on the terminal, ensuring compatibility between different nodes in the network.
        nonce (int): Unique, monotonically increasing number for each terminal, aiding in identifying and ordering network interactions.
        uuid (str): Unique identifier for the terminal, fundamental for network security and identification.
        hotkey (str): Encoded hotkey string of the terminal wallet, important for transaction and identity verification in the network.
        signature (str): Digital signature verifying the tuple of nonce, node_server_hotkey, node_client_hotkey, and uuid, critical for ensuring data authenticity and security.

    Usage::

        # Creating a TerminalInfo instance
        terminal_info = TerminalInfo(
            status_code=200,
            status_message="Success",
            process_time=0.1,
            ip="198.123.23.1",
            port=9282,
            version=111,
            nonce=111111,
            uuid="5ecbd69c-1cec-11ee-b0dc-e29ce36fec1a",
            hotkey="5EnjDGNqqWnuL2HCAdxeEtN2oqtXZw6BMBe936Kfy2PFz1J1",
            signature="0x0813029319030129u4120u10841824y0182u091u230912u"
        )

        # Accessing TerminalInfo attributes
        ip_address = terminal_info.ip
        processing_duration = terminal_info.process_time

        # TerminalInfo can be used to monitor and verify network interactions, ensuring proper communication and security within the Vana network.

    TerminalInfo plays a pivotal role in providing transparency and control over network operations, making it an indispensable tool for developers and users interacting with the Vana ecosystem.
    """

    class Config:
        validate_assignment = True

    # The HTTP status code from: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    status_code: Optional[int] = pydantic.Field(
        title="status_code",
        description="The HTTP status code from: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status",
        examples=200,
        default=None,
        allow_mutation=True,
    )
    _extract_status_code = pydantic.validator(
        "status_code", pre=True, allow_reuse=True
    )(cast_int)

    # The HTTP status code from: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    status_message: Optional[str] = pydantic.Field(
        title="status_message",
        description="The status_message associated with the status_code",
        examples="Success",
        default=None,
        allow_mutation=True,
    )

    # Process time on this terminal side of call
    process_time: Optional[float] = pydantic.Field(
        title="process_time",
        description="Process time on this terminal side of call",
        examples=0.1,
        default=None,
        allow_mutation=True,
    )
    _extract_process_time = pydantic.validator(
        "process_time", pre=True, allow_reuse=True
    )(cast_float)

    # The terminal ip.
    ip: Optional[str] = pydantic.Field(
        title="ip",
        description="The ip of the NodeServer receiving the request.",
        examples="198.123.23.1",
        default=None,
        allow_mutation=True,
    )

    # The host port of the terminal.
    port: Optional[int] = pydantic.Field(
        title="port",
        description="The port of the terminal.",
        examples="9282",
        default=None,
        allow_mutation=True,
    )
    _extract_port = pydantic.validator("port", pre=True, allow_reuse=True)(cast_int)

    # The opendata version on the terminal as an int.
    version: Optional[int] = pydantic.Field(
        title="version",
        description="The opendata version on the NodeServer as str(int)",
        examples=111,
        default=None,
        allow_mutation=True,
    )
    _extract_version = pydantic.validator("version", pre=True, allow_reuse=True)(
        cast_int
    )

    # A unique monotonically increasing integer nonce associate with the terminal
    nonce: Optional[int] = pydantic.Field(
        title="nonce",
        description="A unique monotonically increasing integer nonce associate with the terminal generated from time.monotonic_ns()",
        examples=111111,
        default=None,
        allow_mutation=True,
    )
    _extract_nonce = pydantic.validator("nonce", pre=True, allow_reuse=True)(cast_int)

    # A unique identifier associated with the terminal, set on the NodeServer side.
    uuid: Optional[str] = pydantic.Field(
        title="uuid",
        description="A unique identifier associated with the terminal",
        examples="5ecbd69c-1cec-11ee-b0dc-e29ce36fec1a",
        default=None,
        allow_mutation=True,
    )

    # The opendata version on the terminal as an int.
    hotkey: Optional[str] = pydantic.Field(
        title="hotkey",
        description="The h160 encoded hotkey string of the terminal wallet.",
        examples="0x0123456789abcdef0123456789abcdef01234567",
        default=None,
        allow_mutation=True,
    )

    # A signature verifying the tuple (node_server_nonce, node_server_hotkey, node_client_hotkey, node_server_uuid)
    signature: Optional[str] = pydantic.Field(
        title="signature",
        description="A signature verifying the tuple (nonce, node_server_hotkey, node_client_hotkey, uuid)",
        examples="0x0813029319030129u4120u10841824y0182u091u230912u",
        default=None,
        allow_mutation=True,
    )


class Message(pydantic.BaseModel):
    """
    Represents a Message in the Vana network, serving as a communication schema between neurons (nodes).

    Messages ensure the format and correctness of transmission tensors according to the Vana protocol.
    Each Message type is tailored for a specific machine learning (ML) task, following unique compression and
    communication processes. This helps maintain sanitized, correct, and useful information flow across the network.

    The Message class encompasses essential network properties such as HTTP route names, timeouts, request sizes, and
    terminal information. It also includes methods for serialization, deserialization, attribute setting, and hash
    computation, ensuring secure and efficient data exchange in the network.

    The class includes Pydantic validators and root validators to enforce data integrity and format. Additionally,
    properties like ``is_success``, ``is_failure``, ``is_timeout``, etc., provide convenient status checks based on
    NodeClient responses.

    Think of Vana Messages as glorified pydantic wrappers that have been designed to be used in a distributed
    network. They provide a standardized way to communicate between neurons, and are the primary mechanism for
    communication between neurons in Vana.

    Key Features:

    1. HTTP Route Name (``name`` attribute):
        Enables the identification and proper routing of requests within the network. Essential for users
        defining custom routes for specific machine learning tasks.

    2. Query Timeout (``timeout`` attribute):
        Determines the maximum duration allowed for a query, ensuring timely responses and network
        efficiency. Crucial for users to manage network latency and response times, particularly in
        time-sensitive applications.

    3. Request Sizes (``total_size``, ``header_size`` attributes):
        Keeps track of the size of request bodies and headers, ensuring efficient data transmission without
        overloading the network. Important for users to monitor and optimize the data payload, especially
        in bandwidth-constrained environments.

    4. Terminal Information (``NodeClient``, ``NodeServer`` attributes):
        Stores information about the NodeClient (receiving end) and NodeServer (sending end), facilitating communication
        between nodes. Users can access detailed information about the communication endpoints, aiding in
        debugging and network analysis.

    5. Body Hash Computation (``computed_body_hash``, ``required_hash_fields``):
        Ensures data integrity and security by computing hashes of transmitted data. Provides users with a
        mechanism to verify data integrity and detect any tampering during transmission.

    6. Serialization and Deserialization Methods:
        Facilitates the conversion of Message objects to and from a format suitable for network transmission.
        Essential for users who need to customize data formats for specific machine learning models or tasks.

    7. Status Check Properties (``is_success``, ``is_failure``, ``is_timeout``, etc.):
        Provides quick and easy methods to check the status of a request, improving error handling and
        response management. Users can efficiently handle different outcomes of network requests, enhancing
        the robustness of their applications.

    Example usage::

        # Creating a Message instance with default values
        message = Message()

        # Setting properties and input
        message.timeout = 15.0
        message.name = "MyMessage"
        # Not setting fields that are not defined in your message class will result in an error, e.g.:
        message.dummy_input = 1 # This will raise an error because dummy_input is not defined in the Message class

        # Get a dictionary of headers and body from the message instance
        message_dict = message.json()

        # Get a dictionary of headers from the message instance
        headers = message.to_headers()

        # Reconstruct the message from headers using the classmethod 'from_headers'
        message = Message.from_headers(headers)

        # Deserialize message after receiving it over the network, controlled by `deserialize` method
        deserialized_message = message.deserialize()

        # Checking the status of the request
        if message.is_success:
            print("Request succeeded")

        # Checking and setting the status of the request
        print(message.node_server.status_code)
        message.node_server.status_code = 408 # Timeout

    Args:
        name (str): HTTP route name, set on :func:`NodeServer.attach`.
        timeout (float): Total query length, set by the NodeClient terminal.
        total_size (int): Total size of request body in bytes.
        header_size (int): Size of request header in bytes.
        node_client (TerminalInfo): Information about the NodeClient terminal.
        node_server (TerminalInfo): Information about the NodeServer terminal.
        computed_body_hash (str): Computed hash of the request body.
        required_hash_fields (List[str]): Fields required to compute the body hash.

    Methods:
        deserialize: Custom deserialization logic for subclasses.
        __setattr__: Override method to make ``required_hash_fields`` read-only.
        get_total_size: Calculates and returns the total size of the object.
        to_headers: Constructs a dictionary of headers from instance properties.
        body_hash: Computes a SHA3-256 hash of the serialized body.
        parse_headers_to_inputs: Parses headers to construct an inputs dictionary.
        from_headers: Creates an instance from a headers dictionary.

    This class is a cornerstone in the Vana framework, providing the necessary tools for secure, efficient, and
    standardized communication in a decentralized environment.
    """

    class Config:
        validate_assignment = True

    def deserialize(self) -> "Message":
        """
        Deserializes the Message object.

        This method is intended to be overridden by subclasses for custom deserialization logic.
        In the context of the Message superclass, this method simply returns the instance itself.
        When inheriting from this class, subclasses should provide their own implementation for
        deserialization if specific deserialization behavior is desired.

        By default, if a subclass does not provide its own implementation of this method, the
        Message's deserialize method will be used, returning the object instance as-is.

        In its default form, this method simply returns the instance of the Message itself without any modifications. Subclasses of Message can override this method to add specific deserialization behaviors, such as converting serialized data back into complex object types or performing additional data integrity checks.

        Example::

            class CustomMessage(Message):
                additional_data: str

                def deserialize(self) -> "CustomMessage":
                    # Custom deserialization logic
                    # For example, decoding a base64 encoded string in 'additional_data'
                    if self.additional_data:
                        self.additional_data = base64.b64decode(self.additional_data).decode('utf-8')
                    return self

            serialized_data = '{"additional_data": "SGVsbG8gV29ybGQ="}'  # Base64 for 'Hello World'
            custom_message = CustomMessage.parse_raw(serialized_data)
            deserialized_message = custom_message.deserialize()

            # deserialized_message.additional_data would now be 'Hello World'

        Returns:
            Message: The deserialized Message object. In this default implementation, it returns the object itself.
        """
        return self

    @pydantic.root_validator(pre=True)
    def set_name_type(cls, values) -> dict:
        values["name"] = cls.__name__  # type: ignore
        return values

    # Defines the http route name which is set on NodeServer.attach( callable( request: RequestName ))
    name: Optional[str] = pydantic.Field(
        title="name",
        description="Defines the http route name which is set on NodeServer.attach( callable( request: RequestName ))",
        examples="Forward",
        allow_mutation=True,
        default=None,
        repr=False,
    )

    # The call timeout, set by the NodeClient terminal.
    timeout: Optional[float] = pydantic.Field(
        title="timeout",
        description="Defines the total query length.",
        examples=12.0,
        default=12.0,
        allow_mutation=True,
        repr=False,
    )
    _extract_timeout = pydantic.validator("timeout", pre=True, allow_reuse=True)(
        cast_float
    )

    # The call timeout, set by the NodeClient terminal.
    total_size: Optional[int] = pydantic.Field(
        title="total_size",
        description="Total size of request body in bytes.",
        examples=1000,
        default=0,
        allow_mutation=True,
        repr=False,
    )
    _extract_total_size = pydantic.validator("total_size", pre=True, allow_reuse=True)(
        cast_int
    )

    # The call timeout, set by the NodeClient terminal.
    header_size: Optional[int] = pydantic.Field(
        title="header_size",
        description="Size of request header in bytes.",
        examples=1000,
        default=0,
        allow_mutation=True,
        repr=False,
    )
    _extract_header_size = pydantic.validator(
        "header_size", pre=True, allow_reuse=True
    )(cast_int)

    # The NodeClient Terminal Information.
    node_client: Optional[TerminalInfo] = pydantic.Field(
        title="NodeClient",
        description="NodeClient Terminal Information",
        examples="vana.TerminalInfo",
        default=TerminalInfo(),
        allow_mutation=True,
        repr=False,
    )

    # A NodeServer terminal information
    node_server: Optional[TerminalInfo] = pydantic.Field(
        title="NodeServer",
        description="NodeServer Terminal Information",
        examples="vana.TerminalInfo",
        default=TerminalInfo(),
        allow_mutation=True,
        repr=False,
    )

    computed_body_hash: Optional[str] = pydantic.Field(
        title="computed_body_hash",
        description="The computed body hash of the request.",
        examples="0x0813029319030129u4120u10841824y0182u091u230912u",
        default="",
        allow_mutation=False,
        repr=False,
    )

    required_hash_fields: Optional[List[str]] = pydantic.Field(
        title="required_hash_fields",
        description="The list of required fields to compute the body hash.",
        examples=["roles", "messages"],
        default=[],
        allow_mutation=False,
        repr=False,
    )

    def __setattr__(self, name: str, value: Any):
        """
        Override the :func:`__setattr__` method to make the ``required_hash_fields`` property read-only.

        This is a security mechanism such that the ``required_hash_fields`` property cannot be
        overridden by the user or malicious code.
        """
        if name == "body_hash":
            raise AttributeError(
                "body_hash property is read-only and cannot be overridden."
            )
        super().__setattr__(name, value)

    def get_total_size(self) -> int:
        """
        Get the total size of the current object.

        This method first calculates the size of the current object, then assigns it
        to the instance variable :func:`self.total_size` and finally returns this value.

        Returns:
            int: The total size of the current object.
        """
        self.total_size = get_size(self)
        return self.total_size

    @property
    def is_success(self) -> bool:
        """
        Checks if the NodeClient's status code indicates success.

        This method returns ``True`` if the status code of the NodeClient is ``200``,
        which typically represents a successful HTTP request.

        Returns:
            bool: ``True`` if NodeClient's status code is ``200``, ``False`` otherwise.
        """
        return self.node_client is not None and self.node_client.status_code == 200

    @property
    def is_failure(self) -> bool:
        """
        Checks if the NodeClient's status code indicates failure.

        This method returns ``True`` if the status code of the NodeClient is not ``200``,
        which would mean the HTTP request was not successful.

        Returns:
            bool: ``True`` if NodeClient's status code is not ``200``, ``False`` otherwise.
        """
        return self.node_client is not None and self.node_client.status_code != 200

    @property
    def is_timeout(self) -> bool:
        """
        Checks if the NodeClient's status code indicates a timeout.

        This method returns ``True`` if the status code of the NodeClient is ``408``,
        which is the HTTP status code for a request timeout.

        Returns:
            bool: ``True`` if NodeClient's status code is ``408``, ``False`` otherwise.
        """
        return self.node_client is not None and self.node_client.status_code == 408

    @property
    def is_blacklist(self) -> bool:
        """
        Checks if the NodeClient's status code indicates a blacklisted request.

        This method returns ``True`` if the status code of the NodeClient is ``403``,
        which is the HTTP status code for a forbidden request.

        Returns:
            bool: ``True`` if NodeClient's status code is ``403``, ``False`` otherwise.
        """
        return self.node_client is not None and self.node_client.status_code == 403

    @property
    def failed_verification(self) -> bool:
        """
        Checks if the NodeClient's status code indicates failed verification.

        This method returns ``True`` if the status code of the NodeClient is ``401``,
        which is the HTTP status code for unauthorized access.

        Returns:
            bool: ``True`` if NodeClient's status code is ``401``, ``False`` otherwise.
        """
        return self.node_client is not None and self.node_client.status_code == 401

    def to_headers(self) -> dict:
        """
        Converts the state of a Message instance into a dictionary of HTTP headers.

        This method is essential for
        packaging Message data for network transmission in the Vana framework, ensuring that each key aspect of
        the Message is represented in a format suitable for HTTP communication.

        Process:

        1. Basic Information: It starts by including the ``name`` and ``timeout`` of the Message, which are fundamental for identifying the query and managing its lifespan on the network.
        2. Complex Objects: The method serializes the ``NodeServer`` and ``NodeClient`` objects, if present, into strings. This serialization is crucial for preserving the state and structure of these objects over the network.
        3. Encoding: Non-optional complex objects are serialized and encoded in base64, making them safe for HTTP transport.
        4. Size Metrics: The method calculates and adds the size of headers and the total object size, providing valuable information for network bandwidth management.

        Example Usage::

            message = Message(name="ExampleMessage", timeout=30)
            headers = message.to_headers()
            # headers now contains a dictionary representing the Message instance

        Returns:
            dict: A dictionary containing key-value pairs representing the Message's properties, suitable for HTTP communication.
        """
        # Initializing headers with 'name' and 'timeout'
        headers = {"name": self.name, "timeout": str(self.timeout)}

        # Adding headers for 'NodeServer' and 'NodeClient' if they are not None
        if self.node_server:
            headers.update(
                {
                    f"header_node_server_{k}": str(v)
                    for k, v in self.node_server.dict().items()
                    if v is not None
                }
            )
        if self.node_client:
            headers.update(
                {
                    f"header_node_client_{k}": str(v)
                    for k, v in self.node_client.dict().items()
                    if v is not None
                }
            )

        # Getting the fields of the instance
        instance_fields = self.dict()

        # Iterating over the fields of the instance
        for field, value in instance_fields.items():
            required = [name for name, field in self.__fields__.items() if field.is_required()]

            # Skipping the field if it's already in the headers or its value is None
            if field in headers or value is None:
                continue

            elif required and field in required:
                try:
                    # create an empty (dummy) instance of type(value) to pass pydantic validation on the NodeServer side
                    serialized_value = json.dumps(value.__class__.__call__())
                    encoded_value = base64.b64encode(serialized_value.encode()).decode(
                        "utf-8"
                    )
                    headers[f"header_input_obj_{field}"] = encoded_value
                except TypeError as e:
                    raise ValueError(
                        f"Error serializing {field} with value {value}. Objects must be json serializable."
                    ) from e

        # Adding the size of the headers and the total size to the headers
        headers["header_size"] = str(sys.getsizeof(headers))
        headers["total_size"] = str(self.get_total_size())
        headers["computed_body_hash"] = self.body_hash

        return headers

    @property
    def body_hash(self) -> str:
        """
        Computes a SHA3-256 hash of the serialized body of the Message instance.

        This hash is used to
        ensure the data integrity and security of the Message instance when it's transmitted across the
        network. It is a crucial feature for verifying that the data received is the same as the data sent.

        Process:

        1. Iterates over each required field as specified in ``required_fields_hash``.
        2. Concatenates the string representation of these fields.
        3. Applies SHA3-256 hashing to the concatenated string to produce a unique fingerprint of the data.

        Example::

            message = Message(name="ExampleRoute", timeout=10)
            hash_value = message.body_hash
            # hash_value is the SHA3-256 hash of the serialized body of the Message instance

        Returns:
            str: The SHA3-256 hash as a hexadecimal string, providing a fingerprint of the Message instance's data for integrity checks.
        """
        # Hash the body for verification
        hashes = []

        # Getting the fields of the instance
        instance_fields = self.dict()

        for field, value in instance_fields.items():
            # If the field is required in the subclass schema, hash and add it.
            if (
                    self.required_hash_fields is not None
                    and field in self.required_hash_fields
            ):
                hashes.append(vana.utils.hash(str(value)))

        # Hash and return the hashes that have been concatenated
        return vana.utils.hash("".join(hashes))

    @classmethod
    def parse_headers_to_inputs(cls, headers: dict) -> dict:
        """
        Interprets and transforms a given dictionary of headers into a structured dictionary, facilitating the reconstruction of Message objects.

        This method is essential for parsing network-transmitted
        data back into a Message instance, ensuring data consistency and integrity.

        Process:

        1. Separates headers into categories based on prefixes (``node_server``, ``node_client``, etc.).
        2. Decodes and deserializes ``input_obj`` headers into their original objects.
        3. Assigns simple fields directly from the headers to the input dictionary.

        Example::

            received_headers = {
                'header_node_server_address': '127.0.0.1',
                'header_node_client_port': '8080',
                # Other headers...
            }
            inputs = Message.parse_headers_to_inputs(received_headers)
            # inputs now contains a structured representation of Message properties based on the headers

        Note:
            This is handled automatically when calling :func:`Message.from_headers(headers)` and does not need to be called directly.

        Args:
            headers (dict): The headers dictionary to parse.

        Returns:
            dict: A structured dictionary representing the inputs for constructing a Message instance.
        """

        # Initialize the input dictionary with empty sub-dictionaries for 'NodeServer' and 'NodeClient'
        inputs_dict: Dict[str, Dict[str, str]] = {"node_server": {}, "node_client": {}}

        # Iterate over each item in the headers
        for key, value in headers.items():
            # Handle 'NodeServer' headers
            if "header_node_server_" in key:
                try:
                    new_key = key.split("header_node_server_")[1]
                    inputs_dict["node_server"][new_key] = value
                except Exception as e:
                    vana.logging.error(
                        f"Error while parsing 'node_server' header {key}: {e}"
                    )
                    continue
            # Handle 'NodeClient' headers
            elif "header_node_client_" in key:
                try:
                    new_key = key.split("header_node_client_")[1]
                    inputs_dict["node_client"][new_key] = value
                except Exception as e:
                    vana.logging.error(
                        f"Error while parsing 'node_client' header {key}: {e}"
                    )
                    continue
            # Handle 'input_obj' headers
            elif "header_input_obj" in key:
                try:
                    new_key = key.split("header_input_obj_")[1]
                    # Skip if the key already exists in the dictionary
                    if new_key in inputs_dict:
                        continue
                    # Decode and load the serialized object
                    inputs_dict[new_key] = json.loads(
                        base64.b64decode(value.encode()).decode("utf-8")
                    )
                except json.JSONDecodeError as e:
                    vana.logging.error(
                        f"Error while json decoding 'input_obj' header {key}: {e}"
                    )
                    continue
                except Exception as e:
                    vana.logging.error(
                        f"Error while parsing 'input_obj' header {key}: {e}"
                    )
                    continue
            else:
                pass  # TODO: log unexpected keys

        # Assign the remaining known headers directly
        inputs_dict["timeout"] = headers.get("timeout", None)
        inputs_dict["name"] = headers.get("name", None)
        inputs_dict["header_size"] = headers.get("header_size", None)
        inputs_dict["total_size"] = headers.get("total_size", None)
        inputs_dict["computed_body_hash"] = headers.get("computed_body_hash", None)

        return inputs_dict

    @classmethod
    def from_headers(cls, headers: dict) -> "Message":
        """
        Constructs a new Message instance from a given headers dictionary, enabling the re-creation of the Message's state as it was prior to network transmission.

        This method is a key part of the
        deserialization process in the Vana network, allowing nodes to accurately reconstruct Message
        objects from received data.

        Example::

            received_headers = {
                'header_node_server_address': '127.0.0.1',
                'header_node_client_port': '8080',
                # Other headers...
            }
            message = Message.from_headers(received_headers)
            # message is a new Message instance reconstructed from the received headers

        Args:
            headers (dict): The dictionary of headers containing serialized Message information.

        Returns:
            Message: A new instance of Message, reconstructed from the parsed header information, replicating the original instance's state.
        """

        # Get the inputs dictionary from the headers
        input_dict = cls.parse_headers_to_inputs(headers)

        # Use the dictionary unpacking operator to pass the inputs to the class constructor
        message = cls(**input_dict)

        return message
