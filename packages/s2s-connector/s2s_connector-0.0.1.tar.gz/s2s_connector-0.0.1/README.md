# s2s-connector

A general-purpose Service-to-Service (S2S) connector for obtaining bearer tokens for authentication in service-to-service communication.

## Installation

Install the package via pip:

```bash
pip install s2s-connector
```

## Usage

```python
import asyncio
from s2s_connector import S2SConnector

async def main():
    connector = S2SConnector(
        auth_url="https://auth.example.com",
        tenant="your_tenant",
        client_id="your_client_id",
        client_secret="your_client_secret"
    )

    token = await connector.get_token()
    print(f"Access Token: {token}")

asyncio.run(main())
```