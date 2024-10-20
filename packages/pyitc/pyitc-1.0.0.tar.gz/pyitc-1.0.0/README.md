# pyitc

<img src="https://img.shields.io/github/actions/workflow/status/astro-stan/pyitc/.github%2Fworkflows%2Fbuild-and-run-tests.yml?branch=main&logo=github" alt="Build Status"> <a href="https://codecov.io/gh/astro-stan/pyitc" ><img src="https://codecov.io/gh/astro-stan/pyitc/graph/badge.svg"/></a> <a href="https://github.com/astro-stan/pyitc/releases/latest"><img src="https://img.shields.io/github/v/release/astro-stan/pyitc" alt="Latest GitHub Release"></a> <a href="./LICENSE"><img src="https://img.shields.io/github/license/astro-stan/pyitc" alt="License AGPL-3.0"></a>

Python bindings for the [libitc library](https://github.com/astro-stan/libitc).

## Table Of Contents

* [What Are Interval Tree Clocks?](#what-are-interval-tree-clocks)
* [Features](#features)
* [Getting Started](#getting-started)
    + [Prerequisites](#prerequisites)
    + [Usage Examples](#usage-examples)
* [Contributing](#contributing)
* [Reporting Vulnerabilities](#reporting-vulnerabilities)


## What Are Interval Tree Clocks?

Interval Tree Clocks (ITC) are a generalisation of the [Vector Clock](https://en.wikipedia.org/wiki/Vector_clock) and [Version Vector](https://en.wikipedia.org/wiki/Version_vector) mechanisms, allowing for scalable and efficient management of a
highly dynamic number of replicas/processes in a distributed system.

See the [ITC research paper](http://hydra.azilian.net/Papers/Interval%20Tree%20Clocks.pdf) from Paulo Sérgio Almeida, Carlos Baquero and Victor Fonte for more information.

## Features

* Provides easy-to-use, Pythonesque bindings for the underlying C library
* Provides `__str__` methods for easy visualisation of the ITC trees
* Provides bindings for the C lib's ["extended API"](https://github.com/astro-stan/libitc?tab=readme-ov-file#features:~:text=%22extended%22%20API%20interface)
* Uses 64-bit event counters

## Getting Started

### Prerequisites

Download and install the wheels/sdist from [PyPI](https://pypi.org/project/pyitc/) or [GitHub](https://github.com/astro-stan/pyitc/releases).

### Usage Examples

Here are some usage examples:

```py
from pyitc import Stamp, StampComparisonResult
from pyitc.extended_api import Id, Event

stamp = Stamp()
stamp.event()

stamp2 = stamp.fork()

print(stamp) # {(0, 1); 1}
print(stamp.peek()) # {0, 1}
print(stamp2) # {(1, 0); 1}

if stamp == stamp2: # all comparision operators are supported
    print("yay!")
else:
    print("nay")

if stamp.compare_to(stamp2) == StampComparisonResult.EQUAL: # equivalent to stamp == stamp2
    print("yay again!")

stamp2.event() # Make stamp2 concurrent with stamp

if stamp.compare_to(stamp2) == StampComparisonResult.CONCURRENT:
    print("Oh no! What should we do now?")

stamp3 = stamp2.fork()

stamp2.join(stamp3)

if not stamp3.is_valid():
    print("stamp3 was joined with stamp2 and is no longer valid!")

print(stamp.id_component) # (0, 1)
print(stamp.event_component) # 1

stamp.event_component = Event()
stamp.id_component = Id(seed=True)

print(stamp.serialise()) # b'\x01\t\x01\x02\x01\x00'
print(stamp.id_component.serialise()) # b'\x01\x02'
print(stamp.event_component.serialise()) # b'\x01\x00'

remote_stamp = Stamp.deserialise(b'...')
remote_event = Event.deserialise(b'...')
remote_id = Id.deserialise(b'...')
```

## Contributing

See [CONTRIBUTING.md](https://github.com/astro-stan/pyitc/blob/main/CONTRIBUTING.md).

## Reporting Vulnerabilities

> :warning: **NEVER** open public issues or pull requests to report or fix security vulnerabilities.

See the [Security Policy](https://github.com/astro-stan/pyitc/blob/main/SECURITY.md).
