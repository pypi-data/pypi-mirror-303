"""Smoke-test to ensure the API runs and returns a valid response."""

import json
import subprocess
from http import client
from subprocess import SubprocessError, TimeoutExpired
from urllib import request

import pytest

endpoint = "spec"
host = "127.0.0.1"
pipe = subprocess.PIPE
port = 5000
timeout = 10


@pytest.fixture
def payload():
    """Return the payload to use for the API test."""
    return {
        "timeout": timeout,
        "url": f"http://{host}:{port}/{endpoint}",
    }


@pytest.fixture
def server():
    """Return a server subprocess."""
    cmd = [
        "openfisca",
        "serve",
        "--country-package",
        "openfisca_country_template",
        "--extensions",
        "openfisca_extension_template",
        "--port",
        str(port),
    ]

    with subprocess.Popen(cmd, stdout=pipe, stderr=pipe) as proc:
        for _ in range(timeout * 100 + 1):
            try:
                _, out = proc.communicate(timeout=timeout / 100)

            except TimeoutExpired as error:
                out = error.stderr

            if out is not None:
                break

        if f"Listening at: http://{host}:{port} ({proc.pid})" in str(out):
            yield
            proc.terminate()

        elif out is not None:
            proc.terminate()
            msg = f"Failed to start!\n{out.decode('utf-8')}"
            raise SubprocessError(msg)

        else:
            proc.terminate()
            msg = "Failed to start!"
            raise SubprocessError(msg)


@pytest.mark.usefixtures("server")
def test_openfisca_server(payload):
    """Test the OpenFisca API serves the /spec endpoint."""
    with request.urlopen(**payload) as response:
        data = json.loads(response.read().decode("utf-8"))
        assert response.status == client.OK
        assert data["info"]["title"] == "Openfisca-Country_Template Web API"
