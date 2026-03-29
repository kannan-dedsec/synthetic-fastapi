# FastAPI Project Coding Guidelines

## Code Style

- **Follow [PEP 8](https://peps.python.org/pep-0008/):**  
  - Use 4 spaces per indentation level.
  - Limit lines to 88 characters (black default).
  - Use blank lines to separate functions, classes, and major code sections.
- **Whitespace:**  
  - No trailing whitespace.
  - One space after commas, colons, and semicolons.
  - No spaces inside parentheses, brackets, or braces.
- **Indentation:**  
  - Always use spaces, never tabs.
  - Indent continued lines by 4 spaces from the last level.

## Import Organization

- **Order imports:**  
  1. Standard library imports  
  2. Third-party imports (e.g., `fastapi`, `pydantic`)  
  3. Local application imports
- **Separate each group with a blank line.**
- **Use absolute imports** for clarity.
- **Avoid wildcard imports** (`from module import *`).
- **Import only what you use.**
- Example:
  ```python
  import os
  from typing import List

  from fastapi import FastAPI
  from pydantic import BaseModel

  from app.models import User
  ```

## Naming Conventions

- **Variables and functions:**  
  - Use `snake_case`: `user_id`, `get_user_by_id`
- **Classes:**  
  - Use `CamelCase`: `UserModel`, `UserService`
- **Constants:**  
  - Use `UPPER_CASE`: `MAX_USERS`, `DEFAULT_TIMEOUT`
- **Modules and packages:**  
  - Use `lowercase` and underscores if needed: `user_routes.py`
- **Avoid ambiguous names:**  
  - Prefer `user_list` over `ul`, `response_data` over `rd`

## Documentation

- **Use docstrings for all public modules, classes, and functions.**
- **Format:**  
  - Use triple double quotes (`"""`).
  - First line: short summary.
  - Optionally, add arguments and return info.
- **Example:**
  ```python
  def get_user(user_id: int) -> User:
      """
      Retrieve a user by user_id.

      Args:
          user_id (int): Unique identifier for the user.

      Returns:
          User: The user object.
      """
      ...
  ```
- **Document endpoints:**  
  - Briefly describe purpose, parameters, and response.

## Common Pitfalls

### Mutable Defaults

- **Never use mutable objects as default function arguments.**
- **Why:**  
  - Defaults are evaluated once; can cause unexpected behavior.
- **Incorrect:**
  ```python
  def create_user(data: dict = {}):
      ...
  ```
- **Correct:**
  ```python
  def create_user(data: dict = None):
      if data is None:
          data = {}
      ...
  ```

### Indentation

- **Always use 4 spaces.**
- **No tabs allowed.**
- **Align continued lines with parentheses or by 4 spaces.**

### Other Pitfalls

- **Avoid global variables.**
- **Use type hints for function signatures.**
- **Handle exceptions gracefully; use FastAPI's exception handlers.**
- **Validate input with Pydantic models.**

---

## Summary

- Write clear, readable code.
- Follow PEP 8 and FastAPI best practices.
- Organize imports and name things consistently.
- Document code thoroughly.
- Avoid mutable defaults and indentation errors.

> For more details, see [PEP 8](https://peps.python.org/pep-0008/) and [FastAPI documentation](https://fastapi.tiangolo.com/).