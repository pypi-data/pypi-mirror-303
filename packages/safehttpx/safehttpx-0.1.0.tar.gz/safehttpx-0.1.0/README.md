# safehttpx

A small utility Python created to help developers protect their applications from Server Side Request Forgery (SSRF) attacks. It implements an **asynchronous GET method** called `safehttpx.get()`, which is a wrapper around `httpx.AsyncClient.get()` while performing DNS validation on URL using [Google DNS](https://developers.google.com/speed/public-dns). 

It also implements mitigation for [DNS rebinding](https://en.wikipedia.org/wiki/DNS_rebinding) attacks.

## Why?

Server Side Request Forgery (SSRF) attacks can be particularly dangerous as they allow attackers to make arbitrary HTTP requests from your server, potentially accessing sensitive internal services that are normally unreachable from the internet. This could enable attackers to scan internal networks, access metadata services in cloud environments (like "AWS Instance Metadata Service"), or hit internal APIs - all while appearing to come from your trusted server. By validating URLs against public DNS servers and implementing protections against DNS rebinding, `safehttpx` helps prevent attackers from coercing your application into making requests to internal or otherwise restricted network resources.

## Usage

### Installation

```bash
$ pip install safehttpx
```

### Basic Usage

```py
import safehttpx as sh

await sh.get("https://huggingface.co")
>>> <Response [200 OK]>

await sh.get("http://127.0.0.1")
>>> ValueError: Hostname 127.0.0.1 failed validation
```

**Note on Async Usage:**

The example snippets above will work in environments like IPython or Jupyter notebooks where an asyncio event loop is already running. For regular Python scripts, you'll need to explicitly create and run an asyncio event loop. Here's how you can structure your code to use `safehttpx` in a standard Python script:

```python
import asyncio
import safehttpx as sh

async def main():
    response = await sh.get("https://huggingface.co")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
```

### Whitelisted Domains

You may want to whitelist certain domains from being validated. For example, if you are running code on a server that implements DNS splitting, then even public URLs may appear as internal URLs. You can whitelist domains like this:


```py
import safehttpx as sh

PUBLIC_HOSTNAME_WHITELIST = ["hf.co", "huggingface.co"]

await sh.get("https://huggingface.co", domain_whitelist=PUBLIC_HOSTNAME_WHITELIST)
>>> <Response [200 OK]>
```

### Custom Transports (Advanced)

If you know what you are doing, and what to pass in a custom instance of
`httpx.AsyncBaseTransport`, you can use the `_transport` parameter in `sh.get()`. Setting
this to `False` explicitly will use no secure transport (effectively 
making `sh.get` equivalent to `httpx.AsyncClient.get()`).

## More Information

This library was created as a result of Trail of Bits' security audit of Gradio 5 (Hugging Face), and is used in the Gradio library to make secure requests to custom, user-specified URLs. We are releasing this as a standalone library so that other developers can benefit from our learnings.

If you find a security issue in this library, please email the Gradio team at `gradio-team@huggingface.co`. Thanks!
