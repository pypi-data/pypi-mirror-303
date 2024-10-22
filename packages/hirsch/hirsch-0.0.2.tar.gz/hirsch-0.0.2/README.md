# Hirsch 🦌
Abstracted, continuous, and normalised of version of the Hirsch index (h-index) from academic writing for use as a statistical measure of even distribution

## Installation

```
pip install hirsch
```

## Usage

Get the h-index of some discrete data, e.g. the number of citations an author has received on their papers:

```
from hirsch import hirsch
citations = [0, 1, 1, 2, 1, 6, 5, 13, 14, 10, 59, 145, 68]
h = hirsch(citations)

```

Calculate a continuous h-index for some normalised and binned data, e.g. fractional populations:

```
from hirsch import hirsch
fractions = [0.1,0.5,0.6,0.3,0.2,0.5,0.4]
h = hirsch(fractions, x_max=1, precision=0.01)
```
