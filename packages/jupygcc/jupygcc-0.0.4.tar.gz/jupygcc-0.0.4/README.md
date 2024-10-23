# jupygcc

[![PyPI - Version](https://img.shields.io/pypi/v/jupygcc.svg)](https://pypi.org/project/jupygcc)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/jupygcc.svg)](https://pypi.org/project/jupygcc)

-----

## Installation

```console
pip install jupygcc
```

## Usage

### Configuration

Currently, the kernel can't be configured and will always use:

- `-std=c99 -Wall` for C code
- Wrap the code in a ``main`` function if it doesn't already have one with:

  ```c
  #include <stdbool.h>
  #include <stddef.h>
  #include <stdint.h>
  #include <stdio.h>
  #include <stdlib.h>
  #include <math.h>
  ```

### Cell metadata

Currently, the only cell metadata handled is `stdin` for non-interactive `scanf` and `gets` calls:

```{c}
//| stdin: 10
int n;
printf("How many lines? ");
scanf("%d", &n);
printf("\n%d lines\n");
```

## Development

- Test: `hatch run test`
- Coverage: `htach run coverage`
- 
## License

`jupygcc` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
