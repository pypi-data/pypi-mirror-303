# Quiz for Kids

**Quiz for Kids** is a Python library designed to create fun and educational quizzes for children. 

## Features
- Easy to use
- Customizable questions
- Suitable for children of all ages

## Installation

```bash
pip install quiz-for-kids
```

## Usage

```python
import quiz_for_kids as qfk

variables = ["x", "y", "z"]

equations, data = qfk.linear_system.integer_equations(variables, var_min=1,var_max=4, coef_min=-1,coef_max=3, in_extensive=True)

print("\n".join(equations))

print(data)
```

## License

This project is licensed under the GPLv3 License.
