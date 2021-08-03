# Evil Sums

Generation of sets of numbers where all constituents are recoverable from a partial sum.

## Example

```python
>>> import evil_sums
>>> options = list(evil_sums.generate_options(5))
>>> options
[6, 9, 11, 12, 13]
>>> evil_sums.get_constituents(options, 17)
(6, 11)
>>> # 6 + 11 is the only way to get 17 from the given options
```
