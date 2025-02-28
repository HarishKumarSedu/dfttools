# Informal definition of a language for Inventvm's automatic testing

Should we give it a name ? I think so, but have no idea right now.

## Why defining a new language

Yes, why ? Are we really sure we can't use some other already existing
language ? Like https://www.ivifoundation.org/downloads/SCPI/scpi-99.pdf
for instance. Or maybe add some extensions to an existing languange.
Or using python in a smart way and make it look like a testing language.
Python is object oriented, there are ways to check types at runtime and do
different things accordingly, overload operators and so on ....

This is a very important section !

## Some simple usage example

Not too many, but let's make sure we cover all the routines we actually need
to describe, from the simplest one to the most complicated.
This is very important too.

## Overview

Just some random questions coming to my mind right now:

Interpreted or compiled ? Interpreted I guess ..., even though this is actually
not so important now.
Structure of a program ? Structure of a statement ?
Minimal main program (our hello world) ?
Procedures calls ? Variables and declarations ? Including/reusing code ?
Program result/exit code ?
Are statements run one by one or can there be any parallel execution (maybe
two measurements to be performed in parallel at the same time) ?

## Syntax

List of Keywords and their description with examples

## Semantics

How to put keywords and other elements in the right order to describe some
actual operation. This is what I was calling grammar yesterday.
Examples welcome here too.

## Relationship with hw test machines.

This is interesting. Since there's general agreement on the fact that we cannot
deal with each and every ATE supplier, we must put a boundary somewhere and
CLEARLY define some sort of high level interface, so that suppliers can
implement the hw interface part without needing too much support. This would
concern both describing the operations to be performed and how to return the
results, so it is much like I/O in computers, but more complicated in some
respects because we must deal with lots of different devices.

Assuming we're implementing the interpreter (or whatever) in python, I would
suggest generating a list of objects, each describing an elementary operation.
This list could then become a json file or we could store it in a mongo-like db
like Harish was suggesting. From this json like description we could produce
any other representation, like Excel or simple text or whatever.
Note that one could also think of translating each elementary operation in a
different way depending on the operation itself. For instance "write an i2c
register and then take a voltage measurement of signal X" could become
a register write encoded like we do in our i2c scripts followed by an
scpi instruction or program to deal with the voltmeter.
So in this case, an ATE supplier should just provide a translator from the
"high level" operation to his/her equipment's language.

## Notes on implementation

I've initialized an empty poetry project, I guess it is fine for Harish.

Whatever we do, we need to test it thoroughly. I'm learning pytest and like it,
but I'm not a guru on the subject, so maybe there's something better.
