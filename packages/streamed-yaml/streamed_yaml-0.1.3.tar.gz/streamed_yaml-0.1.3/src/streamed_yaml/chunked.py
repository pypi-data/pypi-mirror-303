from typing_extensions import AsyncIterable
from dataclasses import dataclass
from .parser import KeyState, unroll, aggregate

@dataclass
class Update:
  key: str
  value: str
  done: bool | None = None

async def chunked_parse(stream: AsyncIterable[str]) -> AsyncIterable[Update]:
  """Parse a stream of partial single-level YAML documents. Outputs updates as they come in:
  - Yields with `not chunk.done` when the key is complete but the value is not.
  - Concatenating all `chunk.value`s for a given `chunk.key` will yield the complete value.
  """

  state = KeyState()

  async for chunk in stream:
    states = list(unroll(chunk, state))[1:]
    values, done = aggregate(states)
    for k, v in values.items():
      yield Update(key=k, value=v, done=done[k])

    if states:
      state = states[-1]