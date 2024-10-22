# NetBG Package

NetBG is a Python package designed for various data processing and analysis tasks, providing a suite of methods for handling different algorithms and techniques in network analysis, data mining, and more.

## Installation

To install the NetBG package, you can use pip:

```bash
pip install netbg
```

## Usage

To use the NetBG package, you can import it as follows:

```python
import netbg as ng
```

## Available Methods

The following methods are available in the NetBG package:

1. **crud()** - Perform Create, Read, Update, and Delete operations.
2. **logistic()** - Implement logistic regression for classification tasks.
3. **pipeline()** - Create a processing pipeline for data transformations.
4. **shingles_word()** or **shingles_char()** - Generate word or character shingles from text.
5. **minhash()** - Perform MinHash for estimating the similarity between datasets.
6. **minhashpro()** - Apply MinHash for k-shingles.
7. **martin()** - Implement the Martin algorithm for network analysis.
8. **bloom()** - Use Bloom filters for probabilistic data structures.
9. **ams()** - Apply Alon-Matias-Szegedy algorithm for frequency estimation.
10. **bipartite()** - Analyze bipartite graphs.
11. **social()** - Implement social network analysis methods.
12. **pcy()** - Use the PCY algorithm for frequent itemset mining.

## Example

Here's an example of how to use the `social` method:

```python
import netbg as ng

# Call the social method
ng.social()
```

## Documentation

For more detailed information on each method, please refer to the official documentation or the source code within the package.

## License

This package is licensed under the MIT License. See the LICENSE file for more information.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.
