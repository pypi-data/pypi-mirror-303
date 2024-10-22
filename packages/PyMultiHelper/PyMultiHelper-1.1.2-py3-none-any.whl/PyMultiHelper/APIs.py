from typing import Literal, Optional, Dict, Tuple, Any
import requests

def safeRequest(
        method: Literal["GET", "POST"],
        endpoint: str,
        auth: Optional[Tuple[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        querystring: Optional[Dict[str, str]] = None,
        data: Optional[str] = None,
        json: Optional[Dict[str, Any]] = None,
        timeout: int = 10,
        retries: int = 3,
        allow_redirects: bool = True,
        user_agent: Optional[str] = None,
        responseFormat: Literal["content", "text"] = "text",
) -> str:
    """
    Perform a safe HTTP request (GET or POST) to a specified endpoint.

    This function supports optional headers, query parameters, JSON data,
    and handles retries and timeouts. It also allows customization of the User-Agent header.

    Args:
        method (Literal["GET", "POST"]): The HTTP method to use for the request.
        endpoint (str): The URL to which the request is sent.
        auth (Optional[Tuple[str, str]], optional): Tuple of (username, password) for basic authentication.
        headers (Optional[dict[str, str]], optional): Headers to include in the request.
        querystring (Optional[List[Tuple[str, str]]], optional): List of query parameters.
        data (Optional[str], optional): Data to send in the request body (for POST).
        json (Optional[dict], optional): JSON data to send in the request body (for POST).
        timeout (int, optional): Maximum time to wait for the request to complete (in seconds).
        retries (int, optional): Number of times to retry the request on failure.
        allow_redirects (bool, optional): Whether to allow HTTP redirections.
        user_agent (Optional[str], optional): Custom User-Agent string for the request.
        responseFormat (Literal["content", "text"], optional): Format of the response; "text" for string and "content" for bytes.

    Returns:
        str: The response content in the specified format (text or bytes).

    Raises:
        ValueError: If the method is not "GET" or "POST".
        RuntimeError: If the request fails or if the response status code is not 200.
    """
    if method not in ["GET", "POST"]:
        raise ValueError("You must either choose GET or POST method")

    if user_agent:
        if headers is None:
            headers = {}
        headers['User-Agent'] = user_agent

    for attempt in range(retries):
        try:
            response = requests.request(
                method=method,
                url=endpoint,
                data=data,
                json=json,
                headers=headers,
                params=querystring,
                timeout=timeout,
                allow_redirects=allow_redirects,
                auth=auth
            )

            if response.status_code == 200:
                if responseFormat == "text":
                    return response.text
                elif responseFormat == "content":
                    return response.content
            else:
                raise RuntimeError(f'HTTP error: Code {response.status_code} -> {response.reason}')

        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                continue  # Retry on exception
            raise RuntimeError(f'Requests error: {e}')