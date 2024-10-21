## v0.6.0 (2024-10-20)

### Feat

- **flight**: added properties
- **AirTransportAdapter**: added trips

### Fix

- **TripMixin**: added missing properties

### Refactor

- **all**: moved environment variable configuration out of client

## v0.5.0 (2024-10-12)

### Feat

- **flight**: added flight number and class, terminal information, and city name
- **flight**: added support for jsonpatch in notes

### Fix

- **client**: progress bar to stderr

## v0.4.2 (2024-10-10)

### Refactor

- **diffsync**: moved models to diffsyncmodels

## v0.4.1 (2024-10-07)

### Fix

- **diffsync**: updated datetime fields from str to datetime and added timezone

## v0.4.0 (2024-10-07)

### Feat

- **tripitadapter**: added adapter and status model
- **tools**: added progress bar to api calls

## v0.3.0 (2024-10-05)

### Feat

- **client**: made returned json consistent and promoted first class citizen fields

### Refactor

- **client.py**: split into several mixins

## v0.2.0 (2024-10-05)

### Feat

- **all**: added flights support

## v0.1.2 (2024-10-05)

### Fix

- **__version__.py**: removed local part from version, added automatic stripping of local path when calculating tuple

## v0.1.1 (2024-10-05)

### Fix

- **docker**: removed VERSION build arg
- **__version__.py**: created and removed from .gitignore

## v0.1.0 (2024-10-05)

### Feat

- **all**: initial release
