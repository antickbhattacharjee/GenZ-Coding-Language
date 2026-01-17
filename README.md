# 🚀 GenZLang — Learn Coding Fundamentals the Fun Way

GenZLang is a beginner-friendly programming language designed to teach **real coding fundamentals**
using modern, Gen-Z style keywords.  
Internally it runs on Python, but learners only focus on GenZLang syntax and logic.

This document explains **core programming concepts** using GenZLang examples.

---

## 1️⃣ Hello World

```genz
yeet("Hello World")
```

**What this teaches**
- How to display output
- Program execution flow
- String literals

---

## 2️⃣ Variables (Storing Data)

Use `lock` to create variables.

```genz
lock name = "Antick"
lock age = 25
```

Print variables:

```genz
yeet(name)
yeet(age)
```

**Key concepts**
- Variables store data
- No need to define data types
- Type is decided automatically by the value

---

## 3️⃣ Data Types

GenZLang supports common programming data types:

| Type | Example |
|----|----|
| Text | `"hello"` |
| Integer | `10` |
| Decimal | `3.14` |
| Boolean | `true`, `false` |
| List | `[1, 2, 3]` |
| Map | `{"a": 1}` |

---

## 4️⃣ Type Conversion (Built-in Functions)

```genz
lock a = "10"
lock b = numbruh(a)
yeet(b + 5)
```

Available converters:

- `textvibe()` → string  
- `numbruh()` → integer  
- `decimaldrip()` → float  
- `truetrip()` → boolean  
- `squad()` → list  
- `mapfr()` → dictionary  

---

## 5️⃣ User Input

### Text Input
```genz
lock name = askin("What is your name?")
yeet(name)
```

### Number Input
```genz
lock age = askinnumbruh("Enter your age:")
yeet(age)
```

---

## 6️⃣ Operators & Expressions

### Arithmetic Operations
```genz
lock total = 10 + 5 * 2
yeet(total)
```

### Comparison Operators

| GenZ | Meaning |
|----|----|
| `samevibe` | == |
| `diffvibe` | != |
| `>` `<` `>=` `<=` | standard comparison |

Example:
```genz
lock a = 10
yeet(a samevibe 10)
```

---

## 7️⃣ Conditional Statements

GenZLang uses readable keywords for decisions:

- `nocap` → if  
- `deadass` → else if  
- `cap` → else  

```genz
lock marks = 85

nocap (marks >= 90):
    yeet("Excellent")
deadass (marks >= 60):
    yeet("Passed")
cap:
    yeet("Try Again")
```

Logical operators:
- `andfr` → and  
- `orwhateva` → or  
- `nah` → not  

---

## 8️⃣ Loops (Repetition)

### Range Loop
```genz
spam i from 1 to 5:
    yeet(i)
```

### While-style Loop
```genz
lock i = 1
spam i <= 5:
    yeet(i)
    lock i = i + 1
```

### Infinite Loop
```genz
spam always:
    yeet("Running forever")
    nospam
```

`nospam` works like `break`.

---

## 9️⃣ Functions (Reusable Code)

### Defining a Function
```genz
vibe add(a, b):
    spit a + b
```

### Calling a Function
```genz
yeet(add(5, 3))
```

**Key Concepts**
- `vibe` defines a function
- `spit` returns a value
- Functions reduce repetition

---

## 🔟 Error Handling (tryhard)

GenZLang uses `tryhard` for handling errors.

```genz
tryhard:
    lock x = 10 / 0
sus err:
    yeet("Something went wrong")
frfr:
    yeet("Execution finished")
```

Errors appear in GenZ style:
- `NoDivideVibes`
- `WrongTypeBruh`
- `IDontKnowBro`

---

## 1️⃣1️⃣ Program Rules

- Indentation matters
- Blocks end when indentation ends
- No semicolons required
- Clean and readable syntax

---

## 🎯 Why Learn with GenZLang?

GenZLang helps beginners:
- Understand logic clearly
- Learn real-world programming concepts
- Build confidence before moving to Python, Java, or C++
- Enjoy the learning process

---

## 🧠 What You Learn

- Variables & data types  
- Conditions & loops  
- Functions & modular thinking  
- Error handling  
- Program execution flow  

GenZLang is not a toy language.  
It teaches **real fundamentals** in a friendly way.

## Execution Process

Follow these steps to run a GenZLang program:

1. Write your program and save it with the `.genz` extension  
   Example:
   ```text
   hello.genz
2. Open a terminal in the project root directory
3. Run the program using the kickoff script:

   ./kickoff <path_to_program_file>

Example:
    
    ./kickoff vibecode/hello.genz
4. Press Enter
5. Your GenZLang code will now be parsed and executed line by line.


