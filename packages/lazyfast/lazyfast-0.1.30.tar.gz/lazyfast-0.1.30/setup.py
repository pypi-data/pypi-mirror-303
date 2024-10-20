# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lazyfast']

package_data = \
{'': ['*']}

install_requires = \
['asgiref>=3.8.1,<4.0.0',
 'fastapi>=0.115.2,<0.116.0',
 'python-multipart>=0.0.12,<0.0.13']

setup_kwargs = {
    'name': 'lazyfast',
    'version': '0.1.30',
    'description': 'LazyFast = FastAPI + HTMX + Component-based approach + State management',
    'long_description': '<p align="center">\n  <img src="https://raw.githubusercontent.com/nikirg/lazyfast/refs/heads/main/img/logo.png" alt="LazyFast">\n</p>\n<p align="center">\n  <img src="https://raw.githubusercontent.com/nikirg/lazyfast/refs/heads/main/img/title.png" alt="LazyFast">\n</p>\n<p align="center">\n  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/lazyfast">\n  <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/lazyfast">\n  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/lazyfast">\n</p>\n\n**LazyFast** is a lightweight Python library for building modern, component-based web interfaces using FastAPI. It handles server-side logic in Python, with interactive elements like inputs and buttons triggering server-side component reloads for dynamic state updates.\n\n**Ideal for Python developers who:**\n- Have basic HTML and CSS knowledge and want to build web interfaces without learning complex frontend frameworks like React, Angular, or Vue.\n\n**Suitable for projects that:**\n- Have low to medium traffic and can benefit from server-side rendering to offload work from the client\'s machine. *(Note: High traffic may increase server costs due to backend load.)*\n- Require quick prototyping and demos without involving frontend developers. LazyFast offers more flexibility than tools like Streamlit, which can be limiting and produce similar-looking applications.\n\n**Key Features**\n\n1. **Component-Based Server Rendering**\n   - Build interfaces with lazy-loaded components that encapsulate logic, state, and presentation.\n2. **Server-Side Logic**\n   - Manage interactions and state on the server, reducing client-side complexity.\n3. **FastAPI Integration**\n   - Components and pages are FastAPI endpoints, supporting dependency injection and other features.\n4. **Lightweight**\n   - Dependencies: FastAPI for Python and HTMX for JavaScript (included via CDN).\n5. **State Management**\n   - Use a state manager to trigger component reloads for a reactive user experience.\n\n## Installation\n\nTo install LazyFast, use pip:\n\n```bash\npip install lazyfast\n```\nor\n```bash\npoetry add lazyfast\n```\n\n## Quick Start\n\nHere\'s an example application to demonstrate how LazyFast works:\n\n```python\nfrom fastapi import FastAPI, Request\nfrom lazyfast import LazyFastRouter, Component, tags\n\n\n# LazyFastRouter inherits from FastAPI\'s APIRouter\nrouter = LazyFastRouter()\n\n# Define a lazy-loaded HTML component powered by HTMX\n@router.component()\nclass MyComponent(Component):\n    title: str\n\n    async def view(self, request: Request) -> None:\n        tags.h1(self.title, class_="my-class")\n\n        with tags.div(style="border: 1px solid black"):\n            tags.span(request.headers)\n\n# Initialize the page dependencies for component rendering\n# The page endpoint is also a FastAPI endpoint\n@router.page("/{name}")\ndef root(name: str):\n    with tags.div(class_="container mt-6"):\n        MyComponent(title=f"Hello, World from {name}")\n\n# Embed the router in a FastAPI app\napp = FastAPI()\napp.include_router(router)\n```\nIf you use `uvicorn` instead as a server and want to reload on changes, use the following command:\n```bash\nuvicorn app:app --reload --timeout-graceful-shutdown 1\n```\n\n## Documentation\nDocumentation can be found [here](https://github.com/nikirg/lazyfast/blob/main/DOCS.md).\n\n## Examples\nYou can find examples in [examples](https://github.com/nikirg/lazyfast/tree/main/examples).\n\n## License\n\nLazyFast is licensed under the [MIT License](https://github.com/nikirg/lazyfast/blob/main/LICENSE).\n',
    'author': 'Nikita Irgashev',
    'author_email': 'nik.irg@yandex.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nikirg/lazyfast',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
