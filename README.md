# GitHub Actions Practice Repository

This repository is designed for practicing a typical Git and GitHub workflow, including branching, making changes, and passing a CI/CD pipeline.

## Instructions

Follow these steps to complete the exercise:

1.  **Get Assigned an Issue:** Each person or team will be assigned a GitHub Issue. This issue will correspond to one of the unimplemented functions in the `src/` directory.

2.  **Create a Branch:** Create a new branch for your issue. It's good practice to name your branch something descriptive, like `issue-<number>/<short-description>`. For example:
    ```bash
    git checkout -b issue-1/implement-addition
    ```

3.  **Implement the Function:**
    *   Navigate to the `src/` directory and find the Python file corresponding to your assigned function.
    *   Implement the function logic. Remember to add type hints for the parameters and the return value to pass the checks!

4.  **Update `main.py`:**
    *   Open `main.py` in the root directory.
    *   Uncomment the import statement for your function.
    *   Call your function and print its result to the console. For example:
        ```python
        # i.e. print(function(input_1, input_2))
        result = add(5, 3)
        print(f"The result of add(5, 3) is: {result}")
        ```

5.  **Commit Your Changes:** Stage and commit your changes with a clear commit message.
    ```bash
    git add src/<your-file>.py main.py
    git commit -m "feat: Implement <your-function-name> function"
    ```

6.  **Rebase with `main`:** Before pushing, make sure your branch is up-to-date with the `main` branch.
    ```bash
    git fetch origin
    git rebase origin/main
    ```

7.  **Push and Create a Pull Request:** Push your branch to the remote repository and open a pull request to merge your branch into `main`.
    ```bash
    git push origin <your-branch-name>
    ```

8.  **Pass the CI/CD Pipeline:** Your pull request will automatically trigger the CI/CD pipeline, which runs `ruff` for linting and `mypy` for type checking. **You will not be able to merge your pull request until all checks pass.**

Good luck!