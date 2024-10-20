# SporoSDK

SporoSDK is a Python SDK for interacting with the Sporo API to generate summaries from transcripts.

## Installation

You can install SporOSDK via pip:

```bash
pip install sporosdk
```
## Usage
```bash
from sporosdk import SporoClient

# Initialize the client with your API key
client = SporoClient(api_key='YOUR_API_KEY')

# Generate summary
transcript = "Your transcript text here."
summary = client.generate_summary(transcript)

print(summary)
```
## Configuration
Alternatively, you can set the SPORO_API_KEY environment variable:
```bash
export SPORO_API_KEY='YOUR_API_KEY'
```
And initialize the client without passing the API key:
```bash
from sporosdk import SporoClient

client = SporoClient()
summary = client.generate_summary("Your transcript text here.")
```







