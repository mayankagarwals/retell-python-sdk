# Call

Types:

```python
from retell_sdk.types import (
    CallCreateResponse,
    CallRetrieveResponse,
    CallListResponse,
    CallRegisterResponse,
)
```

Methods:

- <code title="post /create-phone-call">client.call.<a href="./src/retell_sdk/resources/call.py">create</a>(\*\*<a href="src/retell_sdk/types/call_create_params.py">params</a>) -> <a href="./src/retell_sdk/types/call_create_response.py">CallCreateResponse</a></code>
- <code title="get /get-call/{call_id}">client.call.<a href="./src/retell_sdk/resources/call.py">retrieve</a>(call_id) -> <a href="./src/retell_sdk/types/call_retrieve_response.py">CallRetrieveResponse</a></code>
- <code title="get /list-calls">client.call.<a href="./src/retell_sdk/resources/call.py">list</a>(\*\*<a href="src/retell_sdk/types/call_list_params.py">params</a>) -> <a href="./src/retell_sdk/types/call_list_response.py">CallListResponse</a></code>
- <code title="post /register-call">client.call.<a href="./src/retell_sdk/resources/call.py">register</a>(\*\*<a href="src/retell_sdk/types/call_register_params.py">params</a>) -> <a href="./src/retell_sdk/types/call_register_response.py">CallRegisterResponse</a></code>

# PhoneNumber

Types:

```python
from retell_sdk.types import (
    PhoneNumberCreateResponse,
    PhoneNumberRetrieveResponse,
    PhoneNumberUpdateResponse,
    PhoneNumberListResponse,
)
```

Methods:

- <code title="post /create-phone-number">client.phone_number.<a href="./src/retell_sdk/resources/phone_number.py">create</a>(\*\*<a href="src/retell_sdk/types/phone_number_create_params.py">params</a>) -> <a href="./src/retell_sdk/types/phone_number_create_response.py">PhoneNumberCreateResponse</a></code>
- <code title="get /get-phone-number/{phone_number}">client.phone_number.<a href="./src/retell_sdk/resources/phone_number.py">retrieve</a>(phone_number) -> <a href="./src/retell_sdk/types/phone_number_retrieve_response.py">PhoneNumberRetrieveResponse</a></code>
- <code title="patch /update-phone-number/{phone_number}">client.phone_number.<a href="./src/retell_sdk/resources/phone_number.py">update</a>(phone_number, \*\*<a href="src/retell_sdk/types/phone_number_update_params.py">params</a>) -> <a href="./src/retell_sdk/types/phone_number_update_response.py">PhoneNumberUpdateResponse</a></code>
- <code title="get /list-phone-number">client.phone_number.<a href="./src/retell_sdk/resources/phone_number.py">list</a>() -> <a href="./src/retell_sdk/types/phone_number_list_response.py">PhoneNumberListResponse</a></code>
- <code title="delete /delete-phone-number/{phone_number}">client.phone_number.<a href="./src/retell_sdk/resources/phone_number.py">delete</a>(phone_number) -> None</code>

# Agent

Types:

```python
from retell_sdk.types import (
    AgentCreateResponse,
    AgentRetrieveResponse,
    AgentUpdateResponse,
    AgentListResponse,
)
```

Methods:

- <code title="post /create-agent">client.agent.<a href="./src/retell_sdk/resources/agent.py">create</a>(\*\*<a href="src/retell_sdk/types/agent_create_params.py">params</a>) -> <a href="./src/retell_sdk/types/agent_create_response.py">AgentCreateResponse</a></code>
- <code title="get /get-agent/{agent_id}">client.agent.<a href="./src/retell_sdk/resources/agent.py">retrieve</a>(agent_id) -> <a href="./src/retell_sdk/types/agent_retrieve_response.py">AgentRetrieveResponse</a></code>
- <code title="patch /update-agent/{agent_id}">client.agent.<a href="./src/retell_sdk/resources/agent.py">update</a>(agent_id, \*\*<a href="src/retell_sdk/types/agent_update_params.py">params</a>) -> <a href="./src/retell_sdk/types/agent_update_response.py">AgentUpdateResponse</a></code>
- <code title="get /list-agents">client.agent.<a href="./src/retell_sdk/resources/agent.py">list</a>() -> <a href="./src/retell_sdk/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /delete-agent/{agent_id}">client.agent.<a href="./src/retell_sdk/resources/agent.py">delete</a>(agent_id) -> None</code>

# Llm

Types:

```python
from retell_sdk.types import (
    LlmCreateResponse,
    LlmRetrieveResponse,
    LlmUpdateResponse,
    LlmListResponse,
)
```

Methods:

- <code title="post /create-retell-llm">client.llm.<a href="./src/retell_sdk/resources/llm.py">create</a>(\*\*<a href="src/retell_sdk/types/llm_create_params.py">params</a>) -> <a href="./src/retell_sdk/types/llm_create_response.py">LlmCreateResponse</a></code>
- <code title="get /get-retell-llm/{llm_id}">client.llm.<a href="./src/retell_sdk/resources/llm.py">retrieve</a>(llm_id) -> <a href="./src/retell_sdk/types/llm_retrieve_response.py">LlmRetrieveResponse</a></code>
- <code title="patch /update-retell-llm/{llm_id}">client.llm.<a href="./src/retell_sdk/resources/llm.py">update</a>(llm_id, \*\*<a href="src/retell_sdk/types/llm_update_params.py">params</a>) -> <a href="./src/retell_sdk/types/llm_update_response.py">LlmUpdateResponse</a></code>
- <code title="get /list-retell-llm">client.llm.<a href="./src/retell_sdk/resources/llm.py">list</a>() -> <a href="./src/retell_sdk/types/llm_list_response.py">LlmListResponse</a></code>
- <code title="delete /delete-retell-llm/{llm_id}">client.llm.<a href="./src/retell_sdk/resources/llm.py">delete</a>(llm_id) -> None</code>