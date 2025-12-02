# 🎬 PyFlix - Streaming Service Management

A Python project simulating the backend logic of a streaming service (like Netflix).
This project demonstrates the integration of **Object-Oriented Programming (OOP)** for structure and **Functional Programming (FP)** for data analysis.

## 🚀 Key Features

### 1. Object-Oriented Structure (OOP)
* **Inheritance & Polymorphism:** Created a base `Content` class with specific `Movie` and `Series` implementations.
* **Abstract Base Classes (ABC):** Enforced a strict interface using `ABC` and `@abstractmethod` to ensure all content types implement a `play()` method.
* **Data Modeling:** Modeled complex entities with attributes like duration, episodes, rating, and views.

### 2. Functional Programming Logic (FP)
Utilized Python's functional tools to analyze the library data without side effects:
* **Lambda Functions:** For concise, inline logic.
* **Filter:** To extract top-rated content and specific data types.
* **Map:** To transform data (e.g., creating recommendation strings or extracting durations).
* **Reduce:** To aggregate data (e.g., calculating the total duration of a movie marathon).

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** `abc`, `functools`

## 💻 Code Example

Here is how the system filters top-rated content using functional programming:

```python
# Filtering content with a rating higher than 8.0
top_rated = list(filter(lambda c: c.rating > 8.0, library))
```
## 📝 How to Run
1. Clone the repository.
2. Run the script:
```bash
python main.py
```
