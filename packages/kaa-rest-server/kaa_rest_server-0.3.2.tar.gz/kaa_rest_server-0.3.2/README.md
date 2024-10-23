# Kaa REST Server

A very simple python server framework for REST applications.

## Install

```bash
pip install kaa-rest-server
```

## Configuration

**kaa.json**: Specifies server handling.

```json
{
  "name": "My Server",
  "version": "1.0.0",
  "server": "server.MyServer",
  "basePath": ".",
  "debug": false,
  "enableCors": false
}
```

**basePath**: In dev mode. It is the path the system will look at to reload the server.

### Definitions (deprecated)

See [Legacy Documentation](docs/legacy.md)

## Main classes

### server.py

Initializes Kaa for each http request:

```python
from kaa import KaaServer


class MyServer(KaaServer):

    def register_resources(self):
        self.kaa.register_resources("resources", "AppResources")
```

### resources.py

This class define your resources (or routes):

```python
from kaa import GET, PATH, Resources, Response, Status


class AppResources(Resources):

    @GET
    @PATH("/")
    def basic_resource(self, **params):
        return Response(Status.OK).json({
            "message": "your response"
        })
```

## Starting server

**Static mode** (serve): Starts Kaa server in static mode. Every code change needs restart server manually.

```bash
kaa serve
```

**Development mode** (dev): Start server that auto restarts on every code change.

```bash
kaa dev
```

## Custom host and port

By default host is localhost and port is 5321.

You can change them adding host and port on kaa.json file:

```jsonc
{
  // ...
  "host": "localhost",
  "port": 5111,
  // ...
}
```

Or in command line:

```bash
kaa serve host:port
```

## More

For more information, [view Documentation](docs/README.md).
