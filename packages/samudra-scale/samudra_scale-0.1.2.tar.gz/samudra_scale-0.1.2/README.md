# Samudra Scale

This Library helps you extract weight from byte data encoded in a specific way, by mapping byte sequences to numeric digits

## Example usage:

```python
from samudra_scale import decode_bytes

data = b'S\xd4\xacGS\xac+\xa000\xb8950\xeb\xe7\x8d\n'
weight = decode_bytes(data)
print(weight) # 8950
```
