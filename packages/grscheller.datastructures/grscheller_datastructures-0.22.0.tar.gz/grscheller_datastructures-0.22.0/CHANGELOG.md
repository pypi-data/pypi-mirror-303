# CHANGELOG

PyPI grscheller.datastructures project.

#### Semantic versioning

* first digit
  * major event, epoch, or paradigm shift
* second digit
  * breaking API changes
  * major changes
* third digit
  * API additions
  * bug fixes
  * minor changes
  * significant documentation updates
* forth digit (development environment only)
  * commit count of "non-trivial" changes/regressions

## Releases and other important milestones

### Version 0.22.0 - PyPI release date 2024-10-18

* Major refactoring of SplitEnd class
  * splitends is now a subpackage containing the se module
  * removed supporting classes
  * can now be empty
* grscheller.datastructures no longer uses nada as a sentinel value
  * replaced with grscheller.fp.nothingness.noValue
* made classes in nodes module less passive with better encapsulation
* compatible with:
  * grscheller.fp >= 1.0.0 < 1.01
  * grscheller.circular-array >= 3.6.1 < 3.7

### Version 0.21.1.1 - BROKEN as of 2024-10-03

* Does not work with either
  * grscheller.fp 0.3.3 (version working for 0.21.0 release)
  * grscheller.fp 0.4.0 (latest version of fp)
* Needs an upgrade
  * TODO: replace Nada with MB as was done for grscheller.fp.iterables

### Version 0.21.1.0 - mostly docstring updates 2024-09-17

* renamed module `split_ends` -> `stacks`

### Version 0.21.0 - PyPI release date 2024-08-20

* got back to a state maintainer is happy with
  * many dependencies needed updating first

### Version 0.20.5.1 - datastructures coming back together 2024-08-19

* works with all the current versions of fp and circular-array
* preparing for PyPI 0.21.0 release

### Version 0.20.5.0 - datastructures coming back together 2024-08-17

* updated to use grscheller.fp.nada instead of grscheller.untyped.nothing
  * made debugging tons easier
* updated to use all latest PyPI versions of dependencies
* three failed tests involving class SplitEnd
* putting off PyPI v1.0.0 release indefinitely
  * all dependencies need to be at v1.0+
  * need to work out SplitEnd bugs
  * still need to finalize design (need to use it!)
  * need to find good SplitEnd use case
  * other Stack variants like SplintEnd??? (shared data/node variants?)

### Version 0.20.2.0 - Going down a typing rabbit hole 2024-08-03

* updated to use grscheller.circular-array version 3.3.0 (3.2.3.0)
* updated to use grscheller.fp version 0.3.0 (0.2.3.0)
* removed grscheller.circular-array dependency from datastructures.SplitEnd 
* still preparing for the 1.0.0 datastructures release
  * as I tighten up typing, I find I must do so for dependencies too
  * using `# type: ignore` is a band-aid, use `@overload` and `cast` instead
  * using `@overload` to "untype" optional parameters is the way to go
  * use `cast` only when you have knowledge beyond what the typechecker can know

### Version 0.19.0 - PyPI release date 2024-07-15

* continuing to prepare for PyPI release 1.0.0
* cleaned up docstrings for a 1.0.0 release
* changed accumulate1 to accumulate for FTuple
* considering requiring grscheller.fp as a dependency

### Version 0.18.0.0 - Beginning to prepare for PyPI release 1.0.0

* first devel version requiring circular-array 3.1.0
* still some design work to be done
* gave Class SplitEnd fold and fold1 methods
* TODO: Verify flatMap family yields results in "natural" order

### Version 0.17.0.4 - Start of effort to relax None restrictions

* have begun relaxing the requirement of not storing None as a value
  * completed for queues.py
* requires grscheller.circular-array >= 3.0.3.0
* perhaps next PyPI release will be v1.0.0 ???

### Version 0.16.0.0 - Preparing to support PEP 695 generics

* Requires Python >= 3.12
* preparing to support PEP 695 generics
  * will require Python 3.12
  * will not have to import typing for Python 3.12 and beyond
  * BUT... mypy does not support PEP 695 generics yet (Pyright does)
* bumped minimum Python version to >= 3.12 in pyproject.toml
* map methods mutating objects don't play nice with typing
  * map methods now return copies
  * THEREFORE: tests need to be completely overhauled

### Version 0.14.1.1 - Preparing to add TypeVars

* tests working with grscheller.circular-array >= 3.0.0, <3.2
  * lots of mypy complaints
  * first version using TypeVars will be 0.15.0.0

### Version 0.14.0 - PyPI release date 2024-03-09

* updated dependency on CircularArray class
  * dependencies = ["grscheller.circular-array >= 0.2.0, < 2.1"]
* minor README.md woodsmithing
* keeping project an Alpha release for now

### Version 0.13.3.1 - Preparing for another PyPI release soon

* overhauled docstrings with Markdown markup
* updated pyproject.py to drop project back to an Alpha release
  * allows more renaming flexibility
  * intending to develop more graph based data structures
* renamed class core.nodes.Tree_Node to core.node.BT_Node
  * BT for Binary Tree (data in each node of tree)
* created class core.nodes.LT_Node
  * LT for Leaf Tree (data are the leaves of the tree)
* removed deprecated reduce method from various classes
  * use foldL instead

### Version 0.13.2 - PyPI release date 2024-02-20

* Forgot to update pyproject.toml dependencies
  * dependencies = ["grscheller.circular-array >= 0.1.1, < 1.1"]

### Version 0.13.1 - PyPI Release date 2024-01-31

* FTuple now supports both slicing and indexing
* more tests for FTuple
  * slicing and indexing
  * map, foldL, accumulate methods
  * flatMap, mergeMap, exhaustMap methods
* forgot to update CHANGELOG for v0.13.0 release

### Version 0.13.0 - PyPI Release date 2024-01-30

* BREAKING API CHANGE - CircularArray class removed
* CircularArray moved to its own PyPI & GitHub repos
  * https://pypi.org/project/grscheller.circular-array/
  * https://github.com/grscheller/circular-array
* Fix various out-of-date docstrings

### Version 0.12.3 - PyPI Release date 2024-01-20

* cutting next PyPI release from development (main)
  * if experiment works, will drop release branch
  * will not include `docs/`
  * will not include `.gitignore` and `.github/`
  * will include `tests/`
  * made pytest >= 7.4 an optional test dependency

### Version 0.12.2 - PyPI Release date 2024-01-17

* designing sensible reduce & accumulate overrides for Maybe & Either
  * default implementations were not that useful
  * taking their behavior as bugs and not API changes
  * more tests for accumulate & reduce
* fixed Stack reverse() method
  * should have caught this when I fixed FStack on last PyPI release
  * more Stack tests
* many more FP tests

### Version 0.12.1 - PyPI Release date 2024-01-15

* BUG FIX: FStack reverse() method
* added more tests

### Version 0.12.0 - PyPI Release date 2024-01-14

* Considerable future-proofing for first real Beta release

### Version 0.11.3.4 - Finally decided to make next PyPI release Beta

* Package structure mature and not subject to change beyond additions
* Will endeavor to keep top level & core module names the same
* API changes will be deprecated before removed

### Version 0.11.0 - PyPI Release date 2023-12-20

* A lot of work done on class CLArray
  * probably will change its name before the next PyPI Release
    * perhaps to "ProcessArray" or "PArray"
* Keeping this release an Alpha version
  * mostly for the freedom to rename and restructure the package

### Version 0.10.17.0+ (0.11.0-RC2) - 2023-12-17

* Second release candidate - probably will become next PyPI release
  * main now development branch, release will be release branch
  * decided to drop it back to Alpha
    * making datastructures a Beta release was premature
    * classifier "Development Status :: 3 - Alpha"
  * will cut next PyPI release with Flit from release branch
  * will need to regenerate docs on release & move to main
  * things to add in main before next release
    * will not make Maybe Nothing a singleton
    * last touched CLArray refactor
    * improve CLArray test coverage
  * Things for future PYPI releases
    * inherit FTuple from Tuple (use __new__) for performance boost
    * hold off using __slots__ until I understand them better

### Version 0.10.14.2 (0.11.0-RC1) - 2023-12-11

* First release candidate - unlikely this will be the next PyPI release
  * will cut next PyPI release with Flit from main branch
  * removed docs directory before merge (docs/ will be main only)
  * things to add in main before next release
    * make Maybe Nothing a singleton (use __new__)
    * derive FTuple from Tuple (use __new__) for performance boost
    * simplify CLArray to use a Queue instead of CircularArray & iterator
    * start using __slots__ for performance boost to data structures
      * efficiency trumps extensibility
      * prevents client code adding arbitrary attributes & methods
      * smaller size & quicker method/attribute lookups
      * big difference when dealing with huge number of data structures

### Version 0.10.14.0 - commit date 2023-12-09

* Finished massive renaming & repackaging effort
  * to help with future growth in future
  * name choices more self-documenting
  * top level modules
    * array
      * CLArray
    * queue
      * FIFOQueue (formerly SQueue)
      * LIFOQueue (LIFO version of above)
      * DoubleQueue (formerly DQueue)
    * stack
      * Stack (formerly PStack)
      * FStack
    * tuple-like
      * FTuple

### Version 0.10.11.0 - commit date 2023-11-27

* Created new datastructures class CLArray
  * more imperative version of FCLArray
    * has an iterator to swap None values instead of a default value
      * when iterator is exhausted, will swap in () for None
    * no flatMap type methods
    * map method mutates self
    * can be resized
    * returns false when CLArray contains no non-() elements
  * TODO: does not yet handle StopIteration events properly
* made package more overall "atomic"

### Version 0.10.10.0 - commit date 2023-11-26

* More or less finalized FCLArray API
  * finished overriding default flatMap, mergeMap & exhaustMap from FP
  * need mergeMap & exhaustMap versions of unit tests
  * found this data structure very interesting
    * hopefully find a use for it
  * considering a simpler CLArray version

### Version 0.10.9 - PyPI release date 2023-11-21

### Version 0.10.8.0 - commit date 2023-11-18

* Bumping requires-python = ">=3.11" in pyproject.toml
  * Currently developing & testing on Python 3.11.5
  * 0.10.7.X will be used on the GitHub pypy3 branch
    * Pypy3 (7.3.13) using Python (3.10.13)
    * tests pass but are 4X slower
    * LSP almost useless due to more primitive typing module

### Version 0.10.7.0 - commit date 2023-11-18

* Overhauled __repr__ & __str__ methods for all classes
  * tests that ds == eval(repr(ds)) for all data structures ds in package
* CLArray API is in a state of flux
  * no longer stores None as a value
  * __add__ concatenates, no longer component adds
  * maybe allow zero length CLArrays?
    * would make it a monoid and not just a semigroup
    * make an immutable version too?
* Updated markdown overview documentation

### Version 0.10.1.0 - commit date 2023-11-11

* Removed flatMap methods from stateful objects
  * FLArray, DQueue, SQueue, PStack
  * kept the map method for each
* some restructuring so package will scale better in the future

### Version 0.9.1 - PyPI release date: 2023-11-09

* First Beta release of grscheller.datastructures on PyPI
* Infrastructure stable
* Existing datastructures only should need API additions
* Type annotations working extremely well
* Using Pdoc3 to generate documentation on GitHub
  * see https://grscheller.github.io/datastructures/
* All iterators conform to Python language "iterator protocol"
* Improved docstrings
* Future directions:
  * Develop some "typed" containers
  * Add sequence & transverse methods to functional subpackage classes
  * Monad transformers???
  * Need to use this package in other projects to gain insight

### Version 0.8.6.0 - PyPI release date: 2023-11-05

* Finally got queue.py & stack.py inheritance sorted out
* LSP with Pyright working quite well
* Goals for next PyPI release:
  * combine methods
    * tail and tailOr
    * cons and consOr
    * head and headOr

### Version 0.8.4.0 - commit date 2023-11-03

* new data structure FTuple added
  * wrapped tuple with a FP interface
  * initial minimal viable product

### Version 0.8.3.0 - commit date 2023-11-02

* major API breaking change
  * now two versions of Stack class
    * PStack (stateful) with push, pop, peak methods
    * FStack (immutable) with cons, tail, head methods
  * Dqueue renamed DQueue
  * FLarray renamed FLArray
* tests now work

### Version 0.8.0.0 - commit date 2023-10-28

* API breaking changes
  * did not find everything returning self upon mutation
* Efforts for future directions
  * decided to use pdoc3 over sphinx to generate API documentation
  * need to resolve tension of package being Pythonic and Functional

### Version 0.7.5.0 - commit date 2023-10-26

* moved pytest test suite to root of the repo
  * src/grscheller/datastructures/tests -> tests/
  * seems to be the canonical location of a test suite
* instructions to run test suite in tests/__init__.py

### Version 0.7.4.0 - PyPI release date: 2023-10-25

* More mature
* More Pythonic
* Major API changes
* Still tagging it an Alpha release

### Version 0.7.2.0 - commit date 2023-10-18

* Queue & Dqueue no longer return Maybe objects
  * Neither store None as a value
  * Now safe to return None for non-existent values
    * like popping or peaking from an empty queue or dqueue

### Version 0.7.0.0 - commit date 2023-10-16

* added Queue data structure representing a FIFO queue
* renamed two Dqueue methods
  * headR -> peakLastIn
  * headL -> peakNextOut
* went ahead and removed Stack head method
  * fair since I still labeling releases as alpha releases
  * the API is still a work in progress
* updated README.md
  * foreshadowing making a distinction between
    * objects "sharing" their data -> FP methods return copies
    * objects "contain" their data -> FP methods mutate object
  * added info on class Queue

### Version 0.6.9.0 - PyPI release date: 2023-10-09

* deprecated Stack head() method
  * replaced with peak() method
* renamed core module to iterlib module
  * library just contained functions for manipulating iterators
  * TODO: use mergeIters as a guide for an iterator "zip" function
* class Stack better in alignment with:
  * Python lists
    * more natural for Stack to iterate backwards starting from head
    * removed Stack's __getitem__ method
    * both pop and push/append from end
  * Dqueue which wraps a Circle instance
    * also Dqueue does not have a __getitem__ method
  * Circle which implements a circular array with a Python List
  * Stack now implements map, flatMap, mergeMap methods
    * each returns a new Stack instance, with new nodes

### Version 0.6.8.6 - commit date: 2023-10-08

* 3 new methods for class Circle and Dqueue
  * mapSelf, flatMapSelf, mergeMapSelf
    * these correspond to map, flatMap, mergeMap
    * except they act on the class objects themselves, not new instances
* these new methods will NOT be added to the Stack class
  * they would destroy node sharing
  * did add a map method which returns a new instance (with new nodes)
  * TODO: add flatMap and mergeMap methods
* probably will add them to the Dqueue class too
  * not worth the maintenance effort maintaining two version of Dqueue
    * one returning new instances
    * the other modifying the object in place

### Version 0.6.8.3 - commit date: 2023-10-06

* Stack now works with Python Reversed builtin function
  * using a __reversed__ method which is O(n)
  * never figured out why reversed() failed with __getitems__ & __len__
    * this would have been O(n^2) anyway
* Stack no longer implements the __getitems__ method
* class Carray renamed to Circle
  * implements a circular array based on a Python List
  * resizes itself as needed
  * will handle None values being pushed and popped from it
  * implemented in the grscheller.datastructures.circle module
    * in the src/grscheller/datastructures/circle.py file
  * O(1) pushing/popping to/from either end
  * O(1) length determination
  * O(1) indexing for setting and getting values.
* Dqueue implemented with Circle class instead of List class directly
* Ensured that None is never pushed to Stack & Dqueue objects


### Version 0.6.4.1 - commit date: 2023-10-01

* Initial prototypes for map and flatMap for Dqueue class
* Started grscheller.datastructures.core module
  * used for grscheller.datastructures implementation
  * no particular need to indicate them to be _private
  * exports the following functions so far
    * concatIters - sequentially concatenate multiple iterators
    * mergeIters - merge multiple iterators until one is exhausted
    * mapIter - lazily map a function over an iterator stream
* Decided to keep Alpha for next PyPI release

### Version 0.6.3.2 - commit date: 2023-09-30

* Made functional module into a sub package of datastructures
* Improved comments and type annotations
* Removed isEmpty method from Dqueue class
* Both Dqueue & Stack objects evaluate true when non-empty
* Beginning preparations for the next PyPI release
  * Want to make next PyPI release a Beta release
  * Need to improve test suite first

### Version 0.6.2.0 - commit date: 2023-09-25

* Started work on a Left biased Either Monad
* removed isEmpty method from Stack class

### Version 0.6.1.0 - commit date: 2023-09-25

* Maybe get() and getOrElse() API changes
* getting a better handle on type annotation
  * work-in-progress
  * erroneous LSP error messages greatly reduced

### Version 0.5.2.1 - PyPI release date: 2023-09-24

* data structures now support a much more FP style for Python
  * implemented Maybe monad
  * introduces the use of type annotations for this effort
  * much better test coverage

### Version 0.5.0.0 - commit date: 2023-09-20

* begin work on a more functional approach
  * create a monadic Option class
  * drop the subclassing of NONE
  * put this effort on a new branch: feature_maybe
* some flaws with previous approach
  * the OO redirection not best
    * for a class used in computationally intense contexts
    * adds way too much complexity to the design
  * some Python library probably already implemented this
    * without looking, these probably throw tons of exceptions
    * more fun implementing it myself
      * then being dissatisfied with someone else's design

### Version 0.4.0.0 - commit date: 2023-09-11

* subtle paradigm shift for Stack class
  * empty Stacks no longer returned for nonexistent stacks
    * like the tail of an empty stack
    * singleton Stack.stackNONE class object returned instead
  * Stack & _StackNONE classes inherit from _StackBase
  * still working out the API

### Version 0.3.0.2 - PyPI release date: 2023-09-09

* updated class Dqueue
  * added __eq__ method
  * added equality tests to tests/test_dqueue.py
* improved docstrings

### Version 0.2.3.0 - commit date: 2023-09-06

* added __eq__ method to Stack class
* added some preliminary tests
  * more tests are needed
* worst case O(n)
  * will short circuit fast if possible

### Version 0.2.2.2 - PyPI release date: 2023-09-04

* decided base package should have no dependencies other than
  * Python version (>=2.10 due to use of Python match statement)
  * Python standard libraries
* made pytest an optional \[test\] dependency
* added src/ as a top level directory as per
  * https://packaging.python.org/en/latest/tutorials/packaging-projects/
  * could not do the same for tests/ if end users are to have access

### Version 0.2.1.0 - PyPI release date: 2023-09-03

* first Version uploaded to PyPI
* https://pypi.org/project/grscheller.datastructures/
* Install from PyPI
  * $ pip install grscheller.datastructures==0.2.1.0
  * $ pip install grscheller.datastructures # for top level version
* Install from GitHub
  * $ pip install git+https://github.com/grscheller/datastructures@v0.2.1.0
* pytest made a dependency
  * useful & less confusing to developers and end users
    * good for systems I have not tested on
    * prevents another pytest from being picked up from shell $PATH
      * using a different python version
      * giving "package not found" errors
    * for CI/CD pipelines requiring unit testing

### Version 0.2.0.2 - github only release date: 2023-08-29

* First version able to be installed from GitHub with pip
* $ pip install git+https://github.com/grscheller/datastructures@v0.2.0.2

### Version 0.2.0.1 - commit date: 2023-08-29

* First failed attempt to make package installable from GitHub with pip

### Version 0.2.0.0 - commit date: 2023-08-29

* BREAKING API CHANGE!!!
* Stack push method now returns reference to self
* Dqueue pushL & pushR methods now return references to self
* These methods used to return the data being pushed
* Now able to "." chain push methods together
* Updated tests - before making API changes
* First version to be "released" on GitHub

### Version 0.1.1.0 - commit date: 2023-08-27

* grscheller.datastructures moved to its own GitHub repo
* https://github.com/grscheller/datastructures
  * GitHub and PyPI user names just a happy coincidence

### Version 0.1.0.0 - initial version: 2023-08-27

* Package implementing data structures which do not throw exceptions
* Did not push to PyPI until version 0.2.1.0
* Initial Python grscheller.datastructures for 0.1.0.0 commit:
  * dqueue - implements a double sided queue class Dqueue
  * stack - implements a LIFO stack class Stack
