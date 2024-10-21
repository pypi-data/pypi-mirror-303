# Conva AI Python Library

This library enables interaction with Conva AI Co-pilots.

## Installation
```
pip install conva-ai
```

## Usage

### Initializing the Client

To use the Conva AI library, you first need to initialize the `AsyncConvaAI` client with your credentials:

```
from conva_ai import AsyncConvaAI

client = AsyncConvaAI(
    assistant_id="<YOUR_ASSISTANT_ID>",
    assistant_version="<YOUR_ASSISTANT_VERSION>",
    api_key="<YOUR_API_KEY>"
)
```

Replace the placeholders with your actual assistant ID, version, and API key provided by Conva AI.

### Basic Response Generation

To generate a response from the AI, use the `invoke_capability` method:

```
import asyncio

query = "What's the weather like today?"
response = asyncio.run(client.invoke_capability(query, stream=False))
print(response.message)
```

This will send your query to the AI and return a response. The `stream=False` parameter indicates that you want to receive the full response at once.


### Invoking Specific Capabilities

If you want to use a particular capability of the AI, you can specify it using the `invoke_capability_name` method:

```
query = "Take me to the home page"
response = asyncio.run(client.invoke_capability_name(query, stream=False, capability_name="navigation"))
print(response.message)
```

In this example, we're specifically invoking the "navigation" capability of the AI.

### Streaming Responses

For longer responses or real-time interactions, you can use streaming mode:

```
query = "Give me a detailed explanation of quantum computing"
response = asyncio.run(client.invoke_capability(query, stream=True))
async for res in response:
    print(res)
```

This will print parts of the response as they are generated, allowing for more interactive experiences.

### Maintaining Conversation History

To have a continuous conversation with Conva AI, you can keep track of the conversation history:

```
history = "{}"
while True:
    query = input("Enter your query: ")
    response = asyncio.run(client.invoke_capability(query, stream=False, history=history))
    history = response.conversation_history
    print(response.message)
```

This loop allows you to have an ongoing conversation with the Conva AI, with each response considering the context of previous interactions.

### Debugging Responses

To understand the Conva AI's reasoning behind a response, you can access additional information:

```
final_response_dict = response.model_dump()
print(final_response_dict["reason"])
```

This will print out the AI's reasoning process, which can be helpful for debugging or understanding complex responses.

### Try It Out
You can experiment with the Conva AI Co-pilot in a Google Colab notebook. This is a great way to get familiar with the library's capabilities without setting up a local environment.
[Try Conva AI on Google Colab](https://colab.research.google.com/drive/1WtbARTRQ9wCvztrAQuEhQUvwImhtPZXd#scrollTo=ZSVBQsOelgfv)

### Additional Information

Make sure to handle API keys securely and never expose them in your code repositories.
The library uses asynchronous programming with asyncio for efficient handling of I/O operations.