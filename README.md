# Python, Twisted, Reactor, Examples

An exercise in python patterns

## Topics
* Factory patterns
* Singleton patterns
* Facade patterns
* Best Practices
* Parameter Passing
* Object Oriented Nuances
* Packages
* Namespaces

## Good References
* http://www.brpreiss.com/books/opus7/html/book.html
* http://shop.oreilly.com/product/0636920025016.do

## Examples

* python scripts using python modules in project directory structure

This is a recurring pattern.  I want my binaries in a bin/ directory.
When run, it starts python and this pattern shows how to ensure that
the script can find its modules in your git hierarchy.  This is useful
for testing and for deploying code that can be run without fancy
installation.

In this case, the example program is fibonacci, the _binary_ or executable
python script is in our bin/ directory, the modules needed to run it are in
../app.

To run the script, just type:
```shell
./bin/fibo 56

```

* Basic usage of twisted

* Poker deck for blackjack


