# Streamed YAML

> Parse streamed (incomplete) single-level YAML

```bash
pip install streamed-yaml
```

## Partial Parsing

Parse a partial, single-level YAML document. Returns `values, done`, where `done[key]` indicated whether `values[key]` is fully parsed.

```python
from streamed_yaml import parse

parse('key: value') # { 'key': 'value }, { 'key': False }` (values, done)

parse('''
  key: value
  key2
''') # { 'key': 'value }, { 'key': True }

parse('''
  key: value
  key2:
''') # { 'key': 'value', 'key2': '' }, { 'key': True, 'key2': False }

parse('''
  key: value
  key2: "Val...
''') # { 'key': 'value', 'key2': 'Val...' }, { 'key': True, 'key2': False }
```

## Streaming Updates

Parse an arbitrarily chunked stream of single-level YAML. Yields updates at the end of each chunk, s.t. concatenating them yields the full document.

```python
from streamed_yaml import chunked_parse

async def stream():
  yield 'key'      # no update
  yield ': value'  # -> Update(key='key', value='value', done=False)
  yield '\nke'     # -> Update(key='key', value='', done=True)
  yield 'y2: '     # -> Update(key='key2', value='', done=False)
  yield 'value2\n' # -> Update(key='key2', value='value2', done=True)

async for update in chunked_parse(stream()):
  print(update)
```