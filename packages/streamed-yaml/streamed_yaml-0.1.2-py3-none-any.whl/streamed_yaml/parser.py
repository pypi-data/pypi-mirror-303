from typing_extensions import Literal, Iterable
from dataclasses import dataclass
from collections import defaultdict

def strip(text: str) -> str:
  return text.strip().strip('"').strip("'")

def lstrip(text: str) -> str:
  return text.lstrip().lstrip('"').lstrip("'")

@dataclass
class KeyState:
  buffer: str = ''
  stage: Literal['key'] = 'key'

  def step(self, chunk: str) -> tuple['State', str]:
    if ':' in chunk:
      pre, post = chunk.split(':', 1)
      return ValueState(key=strip(self.buffer+pre)), post
    else:
      return KeyState(buffer=self.buffer+chunk), ''

@dataclass
class ValueState:
  key: str
  value_chunk: str = ''
  stage: Literal['value'] = 'value'

  def step(self, chunk: str) -> tuple['State', str]:
    if '\n' in chunk:
      pre, post = chunk.split('\n', 1)
      return PostValueState(key=self.key, value_chunk=pre), post
    else:
      return ValueState(key=self.key, value_chunk=chunk), ''

@dataclass
class PostValueState:
  key: str
  value_chunk: str
  stage: Literal['post'] = 'post'

  def step(self, chunk: str) -> tuple['State', str]:
    return KeyState(), chunk

State = KeyState | ValueState | PostValueState

def strip_lines(text: str) -> str:
  return '\n'.join(l for line in text.splitlines() if (l := line.strip()))

def preprocess(chunk: str) -> str:
  return strip_lines(chunk) + '\n'

def unroll(chunk: str, state: State = KeyState()) -> Iterable[State]:
  yield state
  while chunk:
    state, chunk = state.step(chunk)
    yield state

def aggregate(states: Iterable[State]) -> tuple[dict[str, str], dict[str, bool]]:
  values = defaultdict(lambda: '')
  done = defaultdict(lambda: False)
  for state in states:
    if state.stage == 'value':
      if state.key in values:
        values[state.key] += state.value_chunk
      else:
        values[state.key] = lstrip(state.value_chunk)
        
    elif state.stage == 'post':
      values[state.key] += state.value_chunk
      values[state.key] = strip(values[state.key])
      done[state.key] = True

  return values, done  

def parse(chunk: str) -> tuple[dict[str, str], dict[str, bool]]:
  """Parse a partial single-level YAML document
  
  - Returns `(values, done)`, where `done[key]` indicates whether `values[key]` is complete.
  
  >>> parse('key: value') # `{ 'key': 'value }, { 'key': False }`
  >>> parse('key: value\\nkey2') # `{ 'key': 'value }, { 'key': True }`
  >>> parse('key: value\\nkey2:') # `{ 'key': 'value', 'key2': '' }, ...`
  >>> parse('key: value\\nkey2: "Val...') # `{ 'key': 'value', 'key2': 'Val...' }, ...`
  """
  return aggregate(unroll(chunk))