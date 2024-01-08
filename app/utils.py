from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)




# function to generate unique room id
import random
from string import ascii_uppercase
rooms = [] # rooms = {} # {room_id : [messages]} # for storing the message for a given room id

def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)
        
        if code not in rooms:
            break
    
    return code




"""
Websocket example
import asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')

@sio.event
async def my_message(data):
    print('message received with ', data)
    await sio.emit('my response', {'response': 'my response'})

@sio.event
async def disconnect():
    print('disconnected from server')

async def main():
    await sio.connect('http://localhost:5000')
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())
Client Features
Can connect to other Socket.IO servers that are compatible with the JavaScript Socket.IO 1.x and 2.x releases. Work to support release 3.x is in progress.

Compatible with Python 3.6+.

Two versions of the client, one for standard Python and another for asyncio.

Uses an event-based architecture implemented with decorators that hides the details of the protocol.

Implements HTTP long-polling and WebSocket transports.

Automatically reconnects to the server if the connection is dropped.

Server Examples
The following application is a basic server example that uses the Eventlet asynchronous server:

import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
Below is a similar application, coded for asyncio (Python 3.5+ only) and the Uvicorn web server:

from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
async def chat_message(sid, data):
    print("message ", data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_static('/static', 'static')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)
Server Features
Can connect to servers running other Socket.IO clients that are compatible with the JavaScript client versions 1.x and 2.x. Work to support the 3.x release is in progress.

Compatible with Python 3.6+.

Two versions of the server, one for standard Python and another for asyncio.

Supports large number of clients even on modest hardware due to being asynchronous.

Can be hosted on any WSGI or ASGI web server including Gunicorn, Uvicorn, eventlet and gevent.

Can be integrated with WSGI applications written in frameworks such as Flask, Django, etc.

Can be integrated with aiohttp, sanic and tornado asyncio applications.

Broadcasting of messages to all connected clients, or to subsets of them assigned to “rooms”.

Optional support for multiple servers, connected through a messaging queue such as Redis or RabbitMQ.

Send messages to clients from external processes, such as Celery workers or auxiliary scripts.

Event-based architecture implemented with decorators that hides the details of the protocol.

Support for HTTP long-polling and WebSocket transports.

Support for XHR2 and XHR browsers.

Support for text and binary messages.

Support for gzip and deflate HTTP compression.

Configurable CORS responses, to avoid cross-origin problems with browsers.

©2018, Miguel Grinberg. | Powered by Sphinx 7.2.6 & Alabaster 0.7.13 | Page sourceimport asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')

@sio.event
async def my_message(data):
    print('message received with ', data)
    await sio.emit('my response', {'response': 'my response'})

@sio.event
async def disconnect():
    print('disconnected from server')

async def main():
    await sio.connect('http://localhost:5000')
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())
Client Features
Can connect to other Socket.IO servers that are compatible with the JavaScript Socket.IO 1.x and 2.x releases. Work to support release 3.x is in progress.

Compatible with Python 3.6+.

Two versions of the client, one for standard Python and another for asyncio.

Uses an event-based architecture implemented with decorators that hides the details of the protocol.

Implements HTTP long-polling and WebSocket transports.

Automatically reconnects to the server if the connection is dropped.

Server Examples
The following application is a basic server example that uses the Eventlet asynchronous server:

import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
Below is a similar application, coded for asyncio (Python 3.5+ only) and the Uvicorn web server:

from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
async def chat_message(sid, data):
    print("message ", data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_static('/static', 'static')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)
Server Features
Can connect to servers running other Socket.IO clients that are compatible with the JavaScript client versions 1.x and 2.x. Work to support the 3.x release is in progress.

Compatible with Python 3.6+.

Two versions of the server, one for standard Python and another for asyncio.

Supports large number of clients even on modest hardware due to being asynchronous.

Can be hosted on any WSGI or ASGI web server including Gunicorn, Uvicorn, eventlet and gevent.

Can be integrated with WSGI applications written in frameworks such as Flask, Django, etc.

Can be integrated with aiohttp, sanic and tornado asyncio applications.

Broadcasting of messages to all connected clients, or to subsets of them assigned to “rooms”.

Optional support for multiple servers, connected through a messaging queue such as Redis or RabbitMQ.

Send messages to clients from external processes, such as Celery workers or auxiliary scripts.

Event-based architecture implemented with decorators that hides the details of the protocol.

Support for HTTP long-polling and WebSocket transports.

Support for XHR2 and XHR browsers.

Support for text and binary messages.

Support for gzip and deflate HTTP compression.

Configurable CORS responses, to avoid cross-origin problems with browsers.

©2018, Miguel Grinberg. | Powered by Sphinx 7.2.6 & Alabaster 0.7.13 | Page sourceimport asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')

@sio.event
async def my_message(data):
    print('message received with ', data)
    await sio.emit('my response', {'response': 'my response'})

@sio.event
async def disconnect():
    print('disconnected from server')

async def main():
    await sio.connect('http://localhost:5000')
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())
Client Features
Can connect to other Socket.IO servers that are compatible with the JavaScript Socket.IO 1.x and 2.x releases. Work to support release 3.x is in progress.

Compatible with Python 3.6+.

Two versions of the client, one for standard Python and another for asyncio.

Uses an event-based architecture implemented with decorators that hides the details of the protocol.

Implements HTTP long-polling and WebSocket transports.

Automatically reconnects to the server if the connection is dropped.

Server Examples
The following application is a basic server example that uses the Eventlet asynchronous server:

import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
Below is a similar application, coded for asyncio (Python 3.5+ only) and the Uvicorn web server:

from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
async def chat_message(sid, data):
    print("message ", data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_static('/static', 'static')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)
Server Features
Can connect to servers running other Socket.IO clients that are compatible with the JavaScript client versions 1.x and 2.x. Work to support the 3.x release is in progress.

Compatible with Python 3.6+.

Two versions of the server, one for standard Python and another for asyncio.

Supports large number of clients even on modest hardware due to being asynchronous.

Can be hosted on any WSGI or ASGI web server including Gunicorn, Uvicorn, eventlet and gevent.

Can be integrated with WSGI applications written in frameworks such as Flask, Django, etc.

Can be integrated with aiohttp, sanic and tornado asyncio applications.

Broadcasting of messages to all connected clients, or to subsets of them assigned to “rooms”.

Optional support for multiple servers, connected through a messaging queue such as Redis or RabbitMQ.

Send messages to clients from external processes, such as Celery workers or auxiliary scripts.

Event-based architecture implemented with decorators that hides the details of the protocol.

Support for HTTP long-polling and WebSocket transports.

Support for XHR2 and XHR browsers.

Support for text and binary messages.

Support for gzip and deflate HTTP compression.

Configurable CORS responses, to avoid cross-origin problems with browsers.

©2018, Miguel Grinberg. | Powered by Sphinx 7.2.6 & Alabaster 0.7.13 | Page sourceimport asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')

@sio.event
async def my_message(data):
    print('message received with ', data)
    await sio.emit('my response', {'response': 'my response'})

@sio.event
async def disconnect():
    print('disconnected from server')

async def main():
    await sio.connect('http://localhost:5000')
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())
Client Features
Can connect to other Socket.IO servers that are compatible with the JavaScript Socket.IO 1.x and 2.x releases. Work to support release 3.x is in progress.

Compatible with Python 3.6+.

Two versions of the client, one for standard Python and another for asyncio.

Uses an event-based architecture implemented with decorators that hides the details of the protocol.

Implements HTTP long-polling and WebSocket transports.

Automatically reconnects to the server if the connection is dropped.

Server Examples
The following application is a basic server example that uses the Eventlet asynchronous server:

import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
Below is a similar application, coded for asyncio (Python 3.5+ only) and the Uvicorn web server:

from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
async def chat_message(sid, data):
    print("message ", data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_static('/static', 'static')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)
Server Features
Can connect to servers running other Socket.IO clients that are compatible with the JavaScript client versions 1.x and 2.x. Work to support the 3.x release is in progress.

Compatible with Python 3.6+.

Two versions of the server, one for standard Python and another for asyncio.

Supports large number of clients even on modest hardware due to being asynchronous.

Can be hosted on any WSGI or ASGI web server including Gunicorn, Uvicorn, eventlet and gevent.

Can be integrated with WSGI applications written in frameworks such as Flask, Django, etc.

Can be integrated with aiohttp, sanic and tornado asyncio applications.

Broadcasting of messages to all connected clients, or to subsets of them assigned to “rooms”.

Optional support for multiple servers, connected through a messaging queue such as Redis or RabbitMQ.

Send messages to clients from external processes, such as Celery workers or auxiliary scripts.

Event-based architecture implemented with decorators that hides the details of the protocol.

Support for HTTP long-polling and WebSocket transports.

Support for XHR2 and XHR browsers.

Support for text and binary messages.

Support for gzip and deflate HTTP compression.

Configurable CORS responses, to avoid cross-origin problems with browsers.

©2018, Miguel Grinberg. | Powered by Sphinx 7.2.6 & Alabaster 0.7.13 | Page sourceimport asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')

@sio.event
async def my_message(data):
    print('message received with ', data)
    await sio.emit('my response', {'response': 'my response'})

@sio.event
async def disconnect():
    print('disconnected from server')

async def main():
    await sio.connect('http://localhost:5000')
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())
Client Features
Can connect to other Socket.IO servers that are compatible with the JavaScript Socket.IO 1.x and 2.x releases. Work to support release 3.x is in progress.

Compatible with Python 3.6+.

Two versions of the client, one for standard Python and another for asyncio.

Uses an event-based architecture implemented with decorators that hides the details of the protocol.

Implements HTTP long-polling and WebSocket transports.

Automatically reconnects to the server if the connection is dropped.

Server Examples
The following application is a basic server example that uses the Eventlet asynchronous server:

import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
Below is a similar application, coded for asyncio (Python 3.5+ only) and the Uvicorn web server:

from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
async def chat_message(sid, data):
    print("message ", data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_static('/static', 'static')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)
Server Features
Can connect to servers running other Socket.IO clients that are compatible with the JavaScript client versions 1.x and 2.x. Work to support the 3.x release is in progress.

Compatible with Python 3.6+.

Two versions of the server, one for standard Python and another for asyncio.

Supports large number of clients even on modest hardware due to being asynchronous.

Can be hosted on any WSGI or ASGI web server including Gunicorn, Uvicorn, eventlet and gevent.

Can be integrated with WSGI applications written in frameworks such as Flask, Django, etc.

Can be integrated with aiohttp, sanic and tornado asyncio applications.

Broadcasting of messages to all connected clients, or to subsets of them assigned to “rooms”.

Optional support for multiple servers, connected through a messaging queue such as Redis or RabbitMQ.

Send messages to clients from external processes, such as Celery workers or auxiliary scripts.

Event-based architecture implemented with decorators that hides the details of the protocol.

Support for HTTP long-polling and WebSocket transports.

Support for XHR2 and XHR browsers.

Support for text and binary messages.

Support for gzip and deflate HTTP compression.

Configurable CORS responses, to avoid cross-origin problems with browsers.

©2018, Miguel Grinberg. | Powered by Sphinx 7.2.6 & Alabaster 0.7.13 | Page sourceimport asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')

@sio.event
async def my_message(data):
    print('message received with ', data)
    await sio.emit('my response', {'response': 'my response'})

@sio.event
async def disconnect():
    print('disconnected from server')

async def main():
    await sio.connect('http://localhost:5000')
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())
Client Features
Can connect to other Socket.IO servers that are compatible with the JavaScript Socket.IO 1.x and 2.x releases. Work to support release 3.x is in progress.

Compatible with Python 3.6+.

Two versions of the client, one for standard Python and another for asyncio.

Uses an event-based architecture implemented with decorators that hides the details of the protocol.

Implements HTTP long-polling and WebSocket transports.

Automatically reconnects to the server if the connection is dropped.

Server Examples
The following application is a basic server example that uses the Eventlet asynchronous server:

import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
Below is a similar application, coded for asyncio (Python 3.5+ only) and the Uvicorn web server:

from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
async def chat_message(sid, data):
    print("message ", data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_static('/static', 'static')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)
Server Features
Can connect to servers running other Socket.IO clients that are compatible with the JavaScript client versions 1.x and 2.x. Work to support the 3.x release is in progress.

Compatible with Python 3.6+.

Two versions of the server, one for standard Python and another for asyncio.

Supports large number of clients even on modest hardware due to being asynchronous.

Can be hosted on any WSGI or ASGI web server including Gunicorn, Uvicorn, eventlet and gevent.

Can be integrated with WSGI applications written in frameworks such as Flask, Django, etc.

Can be integrated with aiohttp, sanic and tornado asyncio applications.

Broadcasting of messages to all connected clients, or to subsets of them assigned to “rooms”.

Optional support for multiple servers, connected through a messaging queue such as Redis or RabbitMQ.

Send messages to clients from external processes, such as Celery workers or auxiliary scripts.

Event-based architecture implemented with decorators that hides the details of the protocol.

Support for HTTP long-polling and WebSocket transports.

Support for XHR2 and XHR browsers.

Support for text and binary messages.

Support for gzip and deflate HTTP compression.

Configurable CORS responses, to avoid cross-origin problems with browsers.

©2018, Miguel Grinberg. | Powered by Sphinx 7.2.6 & Alabaster 0.7.13 | Page sourceimport asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')

@sio.event
async def my_message(data):
    print('message received with ', data)
    await sio.emit('my response', {'response': 'my response'})

@sio.event
async def disconnect():
    print('disconnected from server')

async def main():
    await sio.connect('http://localhost:5000')
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())
Client Features
Can connect to other Socket.IO servers that are compatible with the JavaScript Socket.IO 1.x and 2.x releases. Work to support release 3.x is in progress.

Compatible with Python 3.6+.

Two versions of the client, one for standard Python and another for asyncio.

Uses an event-based architecture implemented with decorators that hides the details of the protocol.

Implements HTTP long-polling and WebSocket transports.

Automatically reconnects to the server if the connection is dropped.

Server Examples
The following application is a basic server example that uses the Eventlet asynchronous server:

import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
Below is a similar application, coded for asyncio (Python 3.5+ only) and the Uvicorn web server:

from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
async def chat_message(sid, data):
    print("message ", data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_static('/static', 'static')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)
Server Features
Can connect to servers running other Socket.IO clients that are compatible with the JavaScript client versions 1.x and 2.x. Work to support the 3.x release is in progress.

Compatible with Python 3.6+.

Two versions of the server, one for standard Python and another for asyncio.

Supports large number of clients even on modest hardware due to being asynchronous.

Can be hosted on any WSGI or ASGI web server including Gunicorn, Uvicorn, eventlet and gevent.

Can be integrated with WSGI applications written in frameworks such as Flask, Django, etc.

Can be integrated with aiohttp, sanic and tornado asyncio applications.

Broadcasting of messages to all connected clients, or to subsets of them assigned to “rooms”.

Optional support for multiple servers, connected through a messaging queue such as Redis or RabbitMQ.

Send messages to clients from external processes, such as Celery workers or auxiliary scripts.

Event-based architecture implemented with decorators that hides the details of the protocol.

Support for HTTP long-polling and WebSocket transports.

Support for XHR2 and XHR browsers.

Support for text and binary messages.

Support for gzip and deflate HTTP compression.

Configurable CORS responses, to avoid cross-origin problems with browsers.

©2018, Miguel Grinberg. | Powered by Sphinx 7.2.6 & Alabaster 0.7.13 | Page sourceimport asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')

@sio.event
async def my_message(data):
    print('message received with ', data)
    await sio.emit('my response', {'response': 'my response'})

@sio.event
async def disconnect():
    print('disconnected from server')

async def main():
    await sio.connect('http://localhost:5000')
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())
Client Features
Can connect to other Socket.IO servers that are compatible with the JavaScript Socket.IO 1.x and 2.x releases. Work to support release 3.x is in progress.

Compatible with Python 3.6+.

Two versions of the client, one for standard Python and another for asyncio.

Uses an event-based architecture implemented with decorators that hides the details of the protocol.

Implements HTTP long-polling and WebSocket transports.

Automatically reconnects to the server if the connection is dropped.

Server Examples
The following application is a basic server example that uses the Eventlet asynchronous server:

import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
Below is a similar application, coded for asyncio (Python 3.5+ only) and the Uvicorn web server:

from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
async def chat_message(sid, data):
    print("message ", data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_static('/static', 'static')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)
Server Features
Can connect to servers running other Socket.IO clients that are compatible with the JavaScript client versions 1.x and 2.x. Work to support the 3.x release is in progress.

Compatible with Python 3.6+.

Two versions of the server, one for standard Python and another for asyncio.

Supports large number of clients even on modest hardware due to being asynchronous.

Can be hosted on any WSGI or ASGI web server including Gunicorn, Uvicorn, eventlet and gevent.

Can be integrated with WSGI applications written in frameworks such as Flask, Django, etc.

Can be integrated with aiohttp, sanic and tornado asyncio applications.

Broadcasting of messages to all connected clients, or to subsets of them assigned to “rooms”.

Optional support for multiple servers, connected through a messaging queue such as Redis or RabbitMQ.

Send messages to clients from external processes, such as Celery workers or auxiliary scripts.

Event-based architecture implemented with decorators that hides the details of the protocol.

Support for HTTP long-polling and WebSocket transports.

Support for XHR2 and XHR browsers.

Support for text and binary messages.

Support for gzip and deflate HTTP compression.

Configurable CORS responses, to avoid cross-origin problems with browsers.

©2018, Miguel Grinberg. | Powered by Sphinx 7.2.6 & Alabaster 0.7.13 | Page sourceimport asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')

@sio.event
async def my_message(data):
    print('message received with ', data)
    await sio.emit('my response', {'response': 'my response'})

@sio.event
async def disconnect():
    print('disconnected from server')

async def main():
    await sio.connect('http://localhost:5000')
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())
Client Features
Can connect to other Socket.IO servers that are compatible with the JavaScript Socket.IO 1.x and 2.x releases. Work to support release 3.x is in progress.

Compatible with Python 3.6+.

Two versions of the client, one for standard Python and another for asyncio.

Uses an event-based architecture implemented with decorators that hides the details of the protocol.

Implements HTTP long-polling and WebSocket transports.

Automatically reconnects to the server if the connection is dropped.

Server Examples
The following application is a basic server example that uses the Eventlet asynchronous server:

import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
Below is a similar application, coded for asyncio (Python 3.5+ only) and the Uvicorn web server:

from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
async def chat_message(sid, data):
    print("message ", data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_static('/static', 'static')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)
Server Features
Can connect to servers running other Socket.IO clients that are compatible with the JavaScript client versions 1.x and 2.x. Work to support the 3.x release is in progress.

Compatible with Python 3.6+.

Two versions of the server, one for standard Python and another for asyncio.

Supports large number of clients even on modest hardware due to being asynchronous.

Can be hosted on any WSGI or ASGI web server including Gunicorn, Uvicorn, eventlet and gevent.

Can be integrated with WSGI applications written in frameworks such as Flask, Django, etc.

Can be integrated with aiohttp, sanic and tornado asyncio applications.

Broadcasting of messages to all connected clients, or to subsets of them assigned to “rooms”.

Optional support for multiple servers, connected through a messaging queue such as Redis or RabbitMQ.

Send messages to clients from external processes, such as Celery workers or auxiliary scripts.

Event-based architecture implemented with decorators that hides the details of the protocol.

Support for HTTP long-polling and WebSocket transports.

Support for XHR2 and XHR browsers.

Support for text and binary messages.

Support for gzip and deflate HTTP compression.

Configurable CORS responses, to avoid cross-origin problems with browsers.

©2018, Miguel Grinberg. | Powered by Sphinx 7.2.6 & Alabaster 0.7.13 | Page source
"""
