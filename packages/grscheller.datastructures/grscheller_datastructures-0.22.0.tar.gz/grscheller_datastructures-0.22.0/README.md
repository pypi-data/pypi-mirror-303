# Python Datastructures Useful for Algorithms

Python package of data structures which support the use and
implementation of algorithms.

* **Repositories**
  * [grscheller.datastructures][1] project on *PyPI*
  * [Source code][2] on *GitHub*
* **Detailed documentation**
  * [Detailed API documentation][3] on *GH-Pages*


### Overview

Data structures allowing developers to focus on the algorithms they are
using instead of all the "bit fiddling" required to implement behaviors,
perform memory management, and handle coding edge cases. These data
structures allow iterators to leisurely iterate over inaccessible copies
of internal state while the data structures themselves are free to
safely mutate. They are designed to be reasonably "atomic" without
introducing inordinate complexity. Some of these data structures allow
data to be safely shared between multiple data structure instances by
making shared data immutable and inaccessible to client code.

* functional & imperative programming styles supported
  * functional programming encouraged
  * project endeavors to remain Pythonic
    * methods which mutate objects don't return anything
      * like Python lists
    * in caparisons identity is considered before equality
      * like Python builtins

Sometimes the real power of a data structure comes not from what it
empowers you to do, but from what it prevents you from doing to
yourself.

---

[1]: https://pypi.org/project/grscheller.datastructures/
[2]: https://github.com/grscheller/datastructures/
[3]: https://grscheller.github.io/datastructures/
