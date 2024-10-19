# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

# cSpell:ignore ests
import pytest
import os
from devtools_testutils import (
    test_proxy,
    add_header_regex_sanitizer,
    set_default_session_settings,
    add_body_key_sanitizer,
    add_oauth_response_sanitizer,
    add_general_string_sanitizer,
    add_general_regex_sanitizer,
)
from azure.communication.messages._shared.utils import parse_connection_str


# autouse=True will trigger this fixture on each pytest run, even if it's not explicitly used by a test method
@pytest.fixture(scope="session", autouse=True)
def start_proxy(test_proxy):
    set_default_session_settings()
    add_oauth_response_sanitizer()

    FAKE_CONNECTION_STRING = "endpoint=https://sanitized.unitedstates.communication.azure.com/;accesskey=fake==="
    FAKE_ENDPOINT = "sanitized.unitedstates.communication.azure.com"
    connection_str = os.environ.get("COMMUNICATION_LIVETEST_DYNAMIC_CONNECTION_STRING", FAKE_CONNECTION_STRING)
    if connection_str is not None:
        endpoint, _ = parse_connection_str(connection_str)
        resource_name = endpoint.split(".")[0]
        add_general_string_sanitizer(target=resource_name, value="sanitized")
        add_general_regex_sanitizer(regex=connection_str, value=FAKE_CONNECTION_STRING)
        add_general_regex_sanitizer(regex=endpoint, value=FAKE_ENDPOINT)

    add_general_string_sanitizer(target="8f8c29b2-c2e4-4340-bb28-3009c8a57283", value="sanitized")
    add_body_key_sanitizer(json_path="channel_registration_id", value="sanitized")
    add_body_key_sanitizer(json_path="*.channel_registration_id", value="sanitized")
    add_body_key_sanitizer(json_path="*..channel_registration_id", value="sanitized")
    add_body_key_sanitizer(json_path="to", value="sanitized")
    add_body_key_sanitizer(json_path="*.to", value="sanitized")
    add_body_key_sanitizer(json_path="*..to", value="sanitized")
    add_body_key_sanitizer(json_path="content", value="sanitized")
    add_body_key_sanitizer(json_path="*.content", value="sanitized")
    add_body_key_sanitizer(json_path="*..content", value="sanitized")
    add_body_key_sanitizer(json_path="media_uri", value="sanitized")
    add_body_key_sanitizer(json_path="*.media_uri", value="sanitized")
    add_body_key_sanitizer(json_path="*..media_uri", value="sanitized")
    add_body_key_sanitizer(json_path="id", value="sanitized")
    add_body_key_sanitizer(json_path="*.id", value="sanitized")
    add_body_key_sanitizer(json_path="*..id", value="sanitized")
    add_body_key_sanitizer(json_path="repeatability-request-id", value="sanitized")
    add_body_key_sanitizer(json_path="*.repeatability-request-id", value="sanitized")
    add_body_key_sanitizer(json_path="*..repeatability-request-id", value="sanitized")
    add_body_key_sanitizer(json_path="repeatability-first-sent", value="sanitized")
    add_body_key_sanitizer(json_path="*.repeatability-first-sent", value="sanitized")
    add_body_key_sanitizer(json_path="*..repeatability-first-sent", value="sanitized")

    add_header_regex_sanitizer(key="P3P", value="sanitized")
    add_header_regex_sanitizer(key="Set-Cookie", value="sanitized")
    add_header_regex_sanitizer(key="Date", value="sanitized")
    add_header_regex_sanitizer(key="Cookie", value="sanitized")
    add_header_regex_sanitizer(key="client-request-id", value="sanitized")
    add_header_regex_sanitizer(key="MS-CV", value="sanitized")
    add_header_regex_sanitizer(key="X-Azure-Ref", value="sanitized")
    add_header_regex_sanitizer(key="x-ms-content-sha256", value="sanitized")
    add_header_regex_sanitizer(key="x-ms-client-request-id", value="sanitized")
    add_header_regex_sanitizer(key="x-ms-date", value="sanitized")
    add_header_regex_sanitizer(key="x-ms-ests-server", value="sanitized")
    add_header_regex_sanitizer(key="x-ms-request-id", value="sanitized")
    add_header_regex_sanitizer(key="Content-Security-Policy-Report-Only", value="sanitized")
    add_header_regex_sanitizer(key="repeatability-first-sent", value="sanitized")
    add_header_regex_sanitizer(key="repeatability-request-id", value="sanitized")
    return
