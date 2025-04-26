# Python Tips
## 🧠 Constants vs Variables in Python

In Python, both **constants** and **variables** are used to store data — but their purpose and usage are different.

---

### 🔍 What's the Difference?

| Concept       | Constants                            | Variables                              |
|---------------|----------------------------------------|------------------------------------------|
| **Meaning**   | Fixed values, meant to stay unchanged  | Values that can change over time         |
| **Mutability**| Should not change (by convention)      | Designed to be updated or reassigned     |
| **Syntax**    | `ALL_CAPS` (naming convention)         | `snake_case` (standard Python style)     |
| **Enforced?** | ❌ No, Python doesn't enforce it        | ✅ Yes, you can reassign freely           |
| **Example**   | `PI = 3.14159`                         | `radius = 5`                             |

---

### 🧪 Example Code

```py
# Constant (by convention)
PI = 3.14159

# Variable
radius = 5
area = PI * radius ** 2

print(f"Area of the circle: {area}")
```