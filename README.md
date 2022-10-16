The goal of this repository was to prove the following mini thought experiment I randomly had: represent any number as the sum of unique powers of n. I did so by first coding the special case where n = 2 (the binary case). Next, based on this, I generalized it such that any number could be represented as the sum of unique powers of n. 

The code in this repository is split into 2 main files:
* base_2.py
* base_n.py

In base_2.py, I wrote a function to represent any number as the sum of unique powers of two, which is exactly how binary representations work. This was relatively simple to implement but, after doing so, I realized that I too heavily relied on string manipulation after converting the given number to its equivalent binary representation. In order to implement the general case with the base being any positive integer n, I had to turn to another special case that people are more familiar with representing numbers in: base 10.

In general, this was a pretty neat exercise!