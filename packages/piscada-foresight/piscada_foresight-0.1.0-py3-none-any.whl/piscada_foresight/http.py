"""Authenticated HTTPXTransport used to connect to Foresight."""

import http.server
import json
import logging
import socket
import socketserver
import webbrowser
from contextlib import closing
from pathlib import Path

import httpx
from authlib.common.security import generate_token
from authlib.integrations.httpx_client import OAuth2Client
from authlib.oauth2.rfc7636 import create_s256_code_challenge
from gql.transport.exceptions import TransportAlreadyConnected
from gql.transport.httpx import HTTPXTransport

SCOPE = "email"
CODE_CHALLENGE_METHOD = "S256"

log = logging.getLogger(__name__)


def _find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(("", 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]


def _get_config(domain: str) -> dict:
    config_response = httpx.get(
        f"https://accounts.{domain}/realms/foresight/.well-known/openid-configuration",
        timeout=10.0,
    )
    if config_response.status_code != httpx.codes.OK:
        raise RuntimeError(
            f"Could not fetch authentication configuration from {domain}."
        )
    return config_response.json()


def _get_state_file(client_id: str) -> Path:
    return Path().home() / Path(f".{client_id}_state")


def _has_state_and_refresh_token(domain: str, client_id: str) -> bool:
    try:
        persisted_state = json.load(_get_state_file(client_id).open())
    except FileNotFoundError:
        return False
    return (
        domain in persisted_state
        and "state" in persisted_state[domain]
        and "refresh_token" in persisted_state[domain]
    )


def _get_state_and_refresh_token(domain: str, client_id: str) -> tuple[str, str]:
    persisted_state = json.load(_get_state_file(client_id).open())
    state = persisted_state[domain]["state"]
    refresh_token = persisted_state[domain]["refresh_token"]
    return (state, refresh_token)


def _save_state_and_refresh_token(
    domain: str, client_id: str, state: str, refresh_token: str
):
    json.dump(
        {domain: {"state": state, "refresh_token": refresh_token}},
        _get_state_file(client_id).open("w"),
    )


def _get_client(domain: str, client_id: str, **kwargs) -> OAuth2Client:
    port = _find_free_port()
    openid_configuration = _get_config(domain)
    if _has_state_and_refresh_token(domain, client_id):
        state, refresh_token = _get_state_and_refresh_token(domain, client_id)
        client = OAuth2Client(
            client_id,
            scope=SCOPE,
            code_challenge_method=CODE_CHALLENGE_METHOD,
            state=state,
            **kwargs,
        )
        token = client.refresh_token(
            openid_configuration["token_endpoint"], refresh_token=refresh_token
        )
        _save_state_and_refresh_token(domain, client_id, state, token["refresh_token"])
        return client
    # We need to fetch a new token from scratch.
    code_verifier = generate_token(48)
    code_challenge = create_s256_code_challenge(code_verifier)

    client = OAuth2Client(
        client_id=client_id,
        redirect_uri=f"http://localhost:{port}/callback",
        code_verifier=code_verifier,
        **kwargs,
    )

    uri, state = client.create_authorization_url(
        openid_configuration["authorization_endpoint"],
        scope=SCOPE,
        code_challenge=code_challenge,
        code_challenge_method="S256",
    )

    class CallbackHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path.startswith("/callback"):
                authorization_response = self.path

                token = client.fetch_token(
                    openid_configuration["token_endpoint"],
                    authorization_response=authorization_response,
                    code_verifier=code_verifier,
                )
                _save_state_and_refresh_token(
                    domain, client_id, state, token["refresh_token"]
                )

                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"Authorization complete. You can close this window.")
            else:
                self.send_error(404)
                raise RuntimeError("Could not retrieve response.")

    with socketserver.TCPServer(("localhost", port), CallbackHandler) as httpd:
        webbrowser.open(uri)
        httpd.handle_request()

    return client


class ForesightHTTPXTransport(HTTPXTransport):

    """Sync HTTPXTransport using OAuth2 authentication with Foresight."""

    def __init__(
        self, domain, client_id="foresight-lib-py", json_serialize=json.dumps, **kwargs
    ):
        """Create a new ForesightHTTPXTransport.

        Parameters
        ----------
        domain :
            Which Foresight domain to authenticate against.
        client_id :
            The client-id to use for authentication.
        json_serialize : optional
            The JSON serialization function to use, by default json.dumps.
        kwargs :
            Additional arguments which will be passed to the underlying OAuth2Client.

        """
        self.domain = domain
        self.client_id = client_id
        super().__init__(f"https://graphql.{domain}/", json_serialize, **kwargs)

    def connect(self):
        """Instantiate a new client.

        Raises
        ------
        TransportAlreadyConnected
            If the client had already been instantiated.

        """
        if self.client:
            raise TransportAlreadyConnected("Transport is already connected")

        log.debug("Connecting transport")

        self.client = _get_client(self.domain, self.client_id, **self.kwargs)
