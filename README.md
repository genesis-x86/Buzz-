# Buzz!

Buzz is a low level programming language for a cpu known as [woodpecker](https://github.com/radical-semiconductor/woodpecker)
, created by Radical Semiconductor. The cpu is turing-like and has four different operations:
```
INV
LOAD
INC
CDEC
```
Woodpecker programs must have a single operation per line, which makes large programs extremely confusing and tedious. The purpose of Buzz is to allow for more flexibility and control over the base operations provided. Buzz has support for basic expressions, recursive operations, and functions which help in the development of larger woodpecker programs.

## Documentation

Buzz program files end in .bz and produce a .wpk file.

### Single operations

Single operations are the same, except Buzz allows for multiple operations on a single line as well as functions:

```
INV, LOAD, INV
```
Compiler output:

```
INV
LOAD
INV
```


### Recursive Operations

Recursive operations repeat an operation or function n amount of times:

```
def func: LOAD, CDEC

5(INC)
2(func) 
```

Compiler output:

```
INC
INC
INC
INC
INC
LOAD
CDEC
LOAD
CDEC
```
Recursive operations can also contain recursive operations:

```
INC, 2(INV, 2(INC, LOAD))
```

Compiler output:

```
INC
INV
INC
LOAD
INC
LOAD
INV
INC
LOAD
INC
LOAD
```

### Variables

Variables must be whole numbers or a binary expression:

```
let var = 5
let exp = 10 + 5 - 8
```

Variables can be used for recursive operations: 

```
exp(INV)
```

Compiler output:
```
INV
INV
INV
INV
INV
INV
INV
```

Currently only addition and subtraction are supported. If the result of an expression is negative or zero the compiler will interpret it as 1.

### Functions

Functions are "bundles" of the operations which can be called in code by its identifier. Below is an example of a basic function:

```
def ILV: INV, LOAD, INV
```

Functions can also contain recursive operations, and declared functions:

```
def split: ILV, 5(CDEC), INC
```

Functions can be utilized if you would like to rename the base operations:

```
def I: INV
def N: INC
def L: LOAD
def C: CDEC
```

## Example programs

### Challenge 0: XOR

```
let A = 1
let B = 1 
let O = 1
let S = A+B+O

def ILV: INV,LOAD,INV

def split: ILV,S(CDEC),INC

split
split
S(INC)
INV
2(INC)
ILV
7(CDEC)
INC
INV
```
