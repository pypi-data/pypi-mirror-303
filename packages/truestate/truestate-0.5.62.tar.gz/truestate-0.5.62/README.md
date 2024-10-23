# TrueState Python SDK

The TrueState Python SDK is a Python library that allows you to interact with the TrueState API. The SDK provides a convenient way to access the TrueState API from your Python application.

For documentation on the TrueState API, visit the [API documentation](https://docs.truestate.io).

## Installation

You can install the TrueState Python SDK using pip:

```bash
pip install truestate
```

Once installed, you must configure the following environment variables:

```bash
export TRUESTATE_API_KEY="your-api-key"
export TRUESTATE_ORGANISATION_ID="your-organisation-id"
```

### Inference

The TrueState Python SDK provides a simple way to build and deploy robust natural language AI systems. The inference SDK provides a high-level API for making predictions on your models.

#### Univesal Classification

Universal classification is an advanced type of NLP classification that can be used to classify any type of text data. The TrueState Python SDK provides a high-level API for making predictions on your universal classification models.

```python
from truestate.inference import classify

sample_text = "You should invest all of your money on the stock market!"

result = classify(sample_text, choices=["the text contains financial advice"])

print(result)
#{'the text contains financial advice': 0.9951813}
```

#### Semantic Routing

Semantic routing is a powerful feature that allows you to route incoming messages to the appropriate department or team based on the content of the message. The TrueState Python SDK provides a high-level API for making predictions on your semantic routing models.

```python
from truestate.inference import route

sample_text = "I have a question about my order."


def send_to_order_agent(text: str):
    return f"Sending message to order agent: '{text}'"

def send_to_support_agent(text: str):
    return f"Sending message to support agent: '{text}'"

def send_to_general_agent(text: str):
    return f"Would send message to general agent: '{text}'"

routing_strategies = {
    "the user message is about an order": send_to_order_agent,
    "the user message is about a problem with a product / service": send_to_support_agent,
    "__default__": send_to_general_agent
}

response = route(sample_text, routing_strategies, threshold=0.5)

print(response)
# Sending message to order agent: I have a question about my order....
```

#### Natural Language Search

Natural language search allows you to search for information using natural language queries, offering considerable performance gains above traditional search algorithms. The TrueState Python SDK provides a high-level API for making predictions on your searchable datasets. 

To create a searchable dataset, visit the Workflows documentation. 

```python
from truestate.inference import search

query = "lightweight camping gear for backpacking"

dataset_id = "1783d3ff-178e-485d-a43b-23759cc6bdf3"

results = search("Com", dataset_id)

print(results)
# [
#     {
#         "id": "UL001",
#         "name": "Featherlight Pro X2 Tent",
#         "description": "Ultra-lightweight 2-person tent weighing 1.75 lbs (794g). Made with Dyneema Composite Fabric for ultimate strength-to-weight ratio. Ideal for thru-hikers on long-distance trails."
#     },
#     {
#         "id": "UL002",
#         "name": "AeroDown Ultralight 5°F Sleeping Bag",
#         "description": "Premium 5°F (-15°C) rated sleeping bag weighing only 1.2 lbs (544g). Features 950+ fill power down with water-repellent treatment. Perfect for long-distance backpacking in varied conditions."
#     },
#     {
#         "id": "UL003",
#         "name": "TitaniumFlame Micro Stove System",
#         "description": "Integrated stove system weighing 5.6 oz (159g) including pot. Boils water in 100 seconds and nests with a fuel canister. Engineered for ultralight long-distance hikers."
#     }
# ]
```

#### Hierarchy Classification

In some instances it's necessary to classify text data into a hierarchy of categories. The TrueState Python SDK provides a high-level API for making predictions on your hierarchy classification models.

```python
from truestate.inference import hierarchy_classificaiton

sample_text = "Amazon is a multinational technology company that focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence. The primary business of Amazon.com is the sale of consumer goods and subscriptions."

hierarchy = ClassHierarchy(
    name="company-categorisation",
    choices=[
        Category(
            label="Software company",
            criteria="this text contains a description of a software company",
            subcategories=[
                Category(
                    label="Ecommerce",
                    criteria="this text contains a description of an ecommerce company",
                ),
                Category(
                    label="Blockchain",
                    criteria="this text contains a description of an web3.0 / blockchain company",
                ),
            ],
        ),
    ],
)

result = hierarchy_classificaiton(sample_text, hierarchy)
print(result)
# {
#     "text": "Amazon is a multinational technology company that focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence. The primary business of Amazon.com is the sale of consumer goods and subscriptions.",
#    "categories": {
#       "category_1": "Software company",
#       "category_2": "Ecommerce"
# }
```