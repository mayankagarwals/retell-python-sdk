# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell_sdk import RetellSdk, AsyncRetellSdk
from tests.utils import assert_matches_type
from retell_sdk.types import (
    LlmListResponse,
    LlmCreateResponse,
    LlmUpdateResponse,
    LlmRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLlm:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RetellSdk) -> None:
        llm = client.llm.create()
        assert_matches_type(LlmCreateResponse, llm, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: RetellSdk) -> None:
        llm = client.llm.create(
            begin_message="string",
            general_prompt="string",
            general_tools=[
                {
                    "type": "end_call",
                    "name": "string",
                    "description": "string",
                },
                {
                    "type": "end_call",
                    "name": "string",
                    "description": "string",
                },
                {
                    "type": "end_call",
                    "name": "string",
                    "description": "string",
                },
            ],
            starting_state="string",
            states=[
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                    ],
                },
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                    ],
                },
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                    ],
                },
            ],
        )
        assert_matches_type(LlmCreateResponse, llm, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RetellSdk) -> None:
        response = client.llm.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = response.parse()
        assert_matches_type(LlmCreateResponse, llm, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RetellSdk) -> None:
        with client.llm.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = response.parse()
            assert_matches_type(LlmCreateResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: RetellSdk) -> None:
        llm = client.llm.retrieve(
            "16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(LlmRetrieveResponse, llm, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: RetellSdk) -> None:
        response = client.llm.with_raw_response.retrieve(
            "16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = response.parse()
        assert_matches_type(LlmRetrieveResponse, llm, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: RetellSdk) -> None:
        with client.llm.with_streaming_response.retrieve(
            "16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = response.parse()
            assert_matches_type(LlmRetrieveResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: RetellSdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_id` but received ''"):
            client.llm.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: RetellSdk) -> None:
        llm = client.llm.update(
            "16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(LlmUpdateResponse, llm, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: RetellSdk) -> None:
        llm = client.llm.update(
            "16b980523634a6dc504898cda492e939",
            begin_message="string",
            general_prompt="string",
            general_tools=[
                {
                    "type": "end_call",
                    "name": "string",
                    "description": "string",
                },
                {
                    "type": "end_call",
                    "name": "string",
                    "description": "string",
                },
                {
                    "type": "end_call",
                    "name": "string",
                    "description": "string",
                },
            ],
            starting_state="string",
            states=[
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                    ],
                },
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                    ],
                },
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                    ],
                },
            ],
        )
        assert_matches_type(LlmUpdateResponse, llm, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: RetellSdk) -> None:
        response = client.llm.with_raw_response.update(
            "16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = response.parse()
        assert_matches_type(LlmUpdateResponse, llm, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: RetellSdk) -> None:
        with client.llm.with_streaming_response.update(
            "16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = response.parse()
            assert_matches_type(LlmUpdateResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: RetellSdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_id` but received ''"):
            client.llm.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: RetellSdk) -> None:
        llm = client.llm.list()
        assert_matches_type(LlmListResponse, llm, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: RetellSdk) -> None:
        response = client.llm.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = response.parse()
        assert_matches_type(LlmListResponse, llm, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: RetellSdk) -> None:
        with client.llm.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = response.parse()
            assert_matches_type(LlmListResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: RetellSdk) -> None:
        llm = client.llm.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert llm is None

    @parametrize
    def test_raw_response_delete(self, client: RetellSdk) -> None:
        response = client.llm.with_raw_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = response.parse()
        assert llm is None

    @parametrize
    def test_streaming_response_delete(self, client: RetellSdk) -> None:
        with client.llm.with_streaming_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = response.parse()
            assert llm is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: RetellSdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_id` but received ''"):
            client.llm.with_raw_response.delete(
                "",
            )


class TestAsyncLlm:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncRetellSdk) -> None:
        llm = await async_client.llm.create()
        assert_matches_type(LlmCreateResponse, llm, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRetellSdk) -> None:
        llm = await async_client.llm.create(
            begin_message="string",
            general_prompt="string",
            general_tools=[
                {
                    "type": "end_call",
                    "name": "string",
                    "description": "string",
                },
                {
                    "type": "end_call",
                    "name": "string",
                    "description": "string",
                },
                {
                    "type": "end_call",
                    "name": "string",
                    "description": "string",
                },
            ],
            starting_state="string",
            states=[
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                    ],
                },
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                    ],
                },
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                    ],
                },
            ],
        )
        assert_matches_type(LlmCreateResponse, llm, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRetellSdk) -> None:
        response = await async_client.llm.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = await response.parse()
        assert_matches_type(LlmCreateResponse, llm, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRetellSdk) -> None:
        async with async_client.llm.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = await response.parse()
            assert_matches_type(LlmCreateResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRetellSdk) -> None:
        llm = await async_client.llm.retrieve(
            "16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(LlmRetrieveResponse, llm, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRetellSdk) -> None:
        response = await async_client.llm.with_raw_response.retrieve(
            "16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = await response.parse()
        assert_matches_type(LlmRetrieveResponse, llm, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRetellSdk) -> None:
        async with async_client.llm.with_streaming_response.retrieve(
            "16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = await response.parse()
            assert_matches_type(LlmRetrieveResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRetellSdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_id` but received ''"):
            await async_client.llm.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncRetellSdk) -> None:
        llm = await async_client.llm.update(
            "16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(LlmUpdateResponse, llm, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRetellSdk) -> None:
        llm = await async_client.llm.update(
            "16b980523634a6dc504898cda492e939",
            begin_message="string",
            general_prompt="string",
            general_tools=[
                {
                    "type": "end_call",
                    "name": "string",
                    "description": "string",
                },
                {
                    "type": "end_call",
                    "name": "string",
                    "description": "string",
                },
                {
                    "type": "end_call",
                    "name": "string",
                    "description": "string",
                },
            ],
            starting_state="string",
            states=[
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                    ],
                },
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                    ],
                },
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": {}},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                        {
                            "type": "end_call",
                            "name": "string",
                            "description": "string",
                        },
                    ],
                },
            ],
        )
        assert_matches_type(LlmUpdateResponse, llm, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRetellSdk) -> None:
        response = await async_client.llm.with_raw_response.update(
            "16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = await response.parse()
        assert_matches_type(LlmUpdateResponse, llm, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRetellSdk) -> None:
        async with async_client.llm.with_streaming_response.update(
            "16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = await response.parse()
            assert_matches_type(LlmUpdateResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRetellSdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_id` but received ''"):
            await async_client.llm.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRetellSdk) -> None:
        llm = await async_client.llm.list()
        assert_matches_type(LlmListResponse, llm, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRetellSdk) -> None:
        response = await async_client.llm.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = await response.parse()
        assert_matches_type(LlmListResponse, llm, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRetellSdk) -> None:
        async with async_client.llm.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = await response.parse()
            assert_matches_type(LlmListResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRetellSdk) -> None:
        llm = await async_client.llm.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert llm is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRetellSdk) -> None:
        response = await async_client.llm.with_raw_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = await response.parse()
        assert llm is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRetellSdk) -> None:
        async with async_client.llm.with_streaming_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = await response.parse()
            assert llm is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRetellSdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_id` but received ''"):
            await async_client.llm.with_raw_response.delete(
                "",
            )