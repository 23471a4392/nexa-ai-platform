# Contributing to NexaAI Platform

We welcome contributions from the community! Please follow these guidelines to keep our codebase maintainable and reliable.

## Development Workflow

1. **Fork or Branch**:
   Create a new branch with a descriptive name:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

2. **Code Standards**:
   - Follow PEP 8 guidelines for Python.
   - Maintain clear docstrings and comments where necessary.
   - Keep REST endpoints idempotent and well-structured under `/api/`.

3. **Running Tests**:
   Before committing, ensure all tests pass:
   ```bash
   PYTHONPATH=backend pytest tests/ -v
   ```

4. **Pull Requests**:
   - Write clear PR titles using Conventional Commits (`feat:`, `fix:`, `docs:`, `ci:`, `chore:`).
   - Reference any relevant issues in the PR description.
   - Ensure CI checks pass on your branch.
