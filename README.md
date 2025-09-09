Problem Understanding
Design and implement a Weather Data Storage System that organizes temperature data indexed by
(year, city).
Requirements:
1) WeatherRecord ADT with (date, city, temperature).
2) 2D array-based storage: rows=years, cols=cities.
3) Row-major and column-major access methods and comparison.
4) Sparse-data handling (sentinel or sparse matrix).
5) Time/space complexity analysis for insert, delete, retrieve.

1) Weather Record ADT Design
Attributes:
- Date: (day, month, year) integers.
- City: string.
- Temperature: float (Celsius).
Methods/Responsibilities:
- insert(data): executed by storage; record supplies data.
- delete(criteria): by storage using (city, year).
- retrieve(city, year): by storage for a given (city, year).

2) Data Storage Class
Dense 2D array (list of lists): table[row][col] holds temperature; sentinel float('nan') marksmissing entries.
Optional sparse representation: dictionary-of-keys (year, city) -> temperature.
Core methods: populate_array, row_major_access, column_major_access, to_sparse (conversion),
size_metrics

3) Row-major vs Column-major Access
Dense layout is row-major (list-of-lists). Row-major traversal has better locality; columnmajor is typically strided.
In sparse (dict) layout, both traversals perform similarly; locality matters less.


4) Sparse Data Handling
A) Dense + sentinel NaN: simple O(Y*C) space; constant-time access; wastes memory when sparse.B) Dictionary-of-Keys: O(N) space for N present entries; memory-efficient when sparse; slight
overhead per acces

5) Time and Space Complexity
Let Y=|years|, C=|cities|, N=non-missing entries.
Dense: insert/delete/retrieve O(1); full traversal O(Y*C); space O(Y*C).
Sparse: insert/delete/retrieve O(1) avg; iterate present O(N); space O(N).
