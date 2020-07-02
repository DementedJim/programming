# "A Curious Course on Coroutines and Concurrency" by David Beazley

This tutorial is a practical exploration of using Python coroutines (extended generators) for solving problems in data processing, event handling, and concurrent programming. The material starts off with generators and builds to writing a complete multitasking environment that can run thousands of concurrent tasks without using threads or using code based on event-driven callbacks (i.e., the "reactor" model).

## Requirements
* You need Python 2.5 or newer

* No third party extensions

* We're going to be looking at a lot of code http://www.dabeaz.com/coroutines/

* Go there and follow along with the examples

* I will indicate file names as appropriate

### Uses of Coroutines
Coroutines apparently might be possibly useful in various libraries and frameworks

### Disclaimers
* Concurrency - One of the most difficult topics in computer science (usually best avoided)

* Most of the groundwork for coroutines occurred in the 60s/70s and then stopped in favor of alternatives (e.g., threads, continuations)

## Part 1. Generators

A generator is a function that produces a sequence of results instead of a single value

```python3
In [ ]:
def countdown(n):
 while n > 0:
 yield n
 n -= 1
>>> for i in countdown(5):
... print i,
...
5 4 3 2 1
>>>
```
Instead of returning a value, you generate a series of values (using the yield statement).

Typically, you hook it up to a for-loop Behavior is quite different than normal func.

Calling a generator function creates an generator object. However, it does not start running the function.

```python3
In [ ]:
def countdown(n):
print "Counting down from", n
while n > 0:
yield n
n -= 1
>>> x = countdown(10)
>>> x
<generator object at 0x58490>
>>>
Generator Functions¶
When the generator returns, iteration stops

In [ ]:
>>> x.next()
1
>>> x.next()
Traceback (most recent call last):
File "<stdin>", line 1, in ?
StopIteration
>>>
```

## Part 2 Coroutines, Pipelines, and Dataflow

Coroutines can be used to set up pipes coroutine coroutine coroutine send() send() send().

You just chain coroutines together and push data through the pipe with send() operations.

### Interlude

Coroutines provide more powerful data routing possibilities than simple iterators

**If you built a collection of simple data processing components, you can glue them together into complex arrangements of pipes, branches, merging, etc. (Although there are some limitations)**

In preparing this tutorial, I found myself wishing that variable assignment was an expression

However, I'm not holding my breath on that...

Actually, I'm expecting to be flogged with a rubber chicken for even suggesting it.

## Part 3 Coroutines and Event Dispatching

**Coroutines can be used to write various components that process event streams**

### XML Parsing
There are many possible ways to parse XML. An old-school approach: SAX. SAX is an event driven interface.

### Some Issue
SAX is often used because it can be used to incrementally process huge XML files without a large memory footprint.

 However, the event-driven nature of SAX parsing makes it rather awkward and low-level to deal with.

### Event Processing
To do anything interesting, you have to process the event stream

Example: Convert bus elements into dictionaries (XML sucks, dictionaries rock)

## Part 4 From Data Processing to Concurrent Programming

**Coroutines are similar to generators**

* You can create collections of small processing components and connect them together

* You can process data by setting up pipelines, dataflow graphs, etc.

* You can use coroutines with code that has tricky execution (e.g., event driven systems)

### Limitations

**You also can't create loops or cycles source coroutine**

* Stacked sends are building up a kind of call-stack (send() doesn't return until the target yields)

* If you call a coroutine that's already in the process of sending, you'll get an error

* send() doesn't suspend coroutine execution

## Part 5 Coroutines as Tasks
### The Task Concept

In concurrent programming, one typically subdivides problems into "tasks". Tasks have a few essential features:

* Independent control flow

* Internal state

* Can be scheduled (suspended/resumed)

* Can communicate with other tasks

**Claim : Coroutines are tasks**

### Are Coroutines Tasks?

**Coroutines can be suspended and resumed**

* yield suspends execution

* send() resumes execution

* close() terminates execution

### I'm Convinced

Very clearly, coroutines look like tasks. But they're not tied to threads or subprocesses.

A question : Can you perform multitasking without using either of those concepts?

Multitasking using nothing but coroutines?

## Part 6 A Crash Course in Operating Systems

**CPUs don't know anything about multitasking**

### An Insight

The yield statement is a kind of "trap". When a generator function hits a "yield" statement, it immediately suspends execution.

Control is passed back to whatever code made the generator function run (unseen).

If you treat yield as a trap, you can build a multitasking "operating system"--all in Python!

## Part 7 Let's Build an Operating System

### Some Motivation

* There has been a lot of recent interest in alternatives to threads (especially due to the GIL)

* Non-blocking and asynchronous I/O

Example: servers capable of supporting thousands of simultaneous client connections

* A lot of work has focused on event-driven systems or the "Reactor Model" (e.g.,Twisted)

* Coroutines are a whole different twist...

### Design Discussion

* Real operating systems have a strong notion of "protection" (e.g., memory protection).

* Application programs are not strongly linked to the OS kernel (traps are only interface)

For sanity, we are going to emulate this:

* Tasks do not see the scheduler

* Tasks do not see other tasks

* yield is the only external interface

## Part 8 The Problem with the Stack

### A Problem

* The yield statement can only be used to suspend a coroutine at the top-most level

* You can't push yield inside library functions

* Digression: this limitation is one of the things that is addressed by Stackless Python

### A Solution

* There is a way to create suspendable subroutines and functions

* However, it can only be done with the assistance of the task scheduler itself

* You have to strictly stick to yield statements

* Involves a trick known as "trampolining"
