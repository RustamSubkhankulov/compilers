# Lexical analyzer

Note: see README.md for russian version of this document.
Warning: this document is automatically translated, therefore mistakes are possible.

### 1. Informal description of the language **Yazik++**
Lexical units of **Yazik++** are integers, type identifiers, object identifiers, strings, keywords, and
comments.
- **Integers** are non-empty sequences of numbers 0 – 9.
- **Identifiers** are sequences of characters (except keywords) consisting of letters, numbers and an underscore.
Type identifiers begin with a capital letter.
Object IDs begin with a lowercase letter.
- **Special syntax characters** – parentheses, operator
assignments, arithmetic operators.
- **Strings** – sequences of any alphabetic characters, enclosed in quotation marks "...". Strings cannot contain EOF and \0, but they can contain \n. A string can be wrapped across multiple lines using '\' (C-like string literal).
- **Comment** begins with a pair of hyphens “--” and ends with a new one
string (or EOF) and includes all characters between them. Comments can also be written by enclosing the text in */*...*/*. The last comment form can be nested. Comments cannot
cross file boundaries.
- **Keywords** – *else, false, if, loop, then, while, not, true,
print, println*. With the exception of the *true* and *false* constants, the key
words are case insensitive. To comply with the rules
for other objects, the first letter of *true* and *false* must be lowercase;
other letters can be in upper or lower case.

### 2. flex/flex++

*flex*/*flex++* - a tool for creating scanners. A scanner is a program that recognizes lexical patterns in text. *flex* reads the given input files, or standard input if no file names are specified, to obtain a description of the scanner being created. The description is presented in the form of pairs of regular expressions and C/C++ code, called rules. *flex* generates as output a C source file, defaulting to lex.yy.c, which defines the yylex() function. This file can be compiled and linked with the *flex* runtime library to create an executable file. When the executable runs, it parses the input for regular expressions. Whenever it finds one, it executes the corresponding C/C++ code.

### 3. Structure
- *examples* - see paragraph **use**
- *rules* - contains rules for building a lexical analyzer
- *inc* - headers required for the lexer to work
- *tests* - json data for testing
- *scripts* - python-scripts for testing

### 4. Building and use

#### Building
To build the project, you need the CMake build system version 3.21 and higher, as well as the *flex* lexical analyzer generation utility installed.
To build the project, use the following commands:
- <code>cmake -B build -DDUMP_JSON=ON</code>
- <code>cmake --build build --target lexer</code>

The **DUMP_JSON** option enables output of lexer results in JSON format.

#### Usage
To test the operation of the analyzer, a directory *examples* has been prepared, containing an example program in the **Yazik++** language, intended to demonstrate the operation of the lexer.
To use the parser, run the executable file from the *build* directory and provide the program text or a pre-prepared program from *examples* as input.

### 5. Testing
To test the operation of the lexer, a *python script has been prepared that uses the output of the analyzer and pre-prepared token options in JSON format in **tests/test_data.json** in order to compare the result of the work with the expected class and value of the tokens.
To start testing, you can use the following command (after building the project):
<code>./scripts/etoe.py build/lexer tests/test_data.json</code>.
