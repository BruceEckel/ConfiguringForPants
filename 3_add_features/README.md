# Step 3: Add Features

- Copy the contents of the directory `2_run_tailor` into a new directory and
  **`cd`** into it.

- Add more abilities to your Pants build. Modify `pants.toml` so
  `backend_packages` looks like this:
```
backend_packages = [
  "pants.backend.python",
  "pants.backend.python.lint.docformatter",
  "pants.backend.python.lint.black",
  "pants.backend.python.lint.flake8",
  "pants.backend.python.lint.isort",
  "pants.backend.python.typecheck.mypy",
]
```

- Now you can run **`./pants lint ::`** and you will see warnings and errors from
  applying the various linting tools.

- You can run **`./pants check ::`** and you will see an error produced by `mypy`.

- Optional: Add a *source root* (see
  <https://www.pantsbuild.org/docs/source-roots>) to `pants.toml`:
```
[source]
root_patterns = ["/"]
```
Because this project is quite straightforward it can omit this and use the default source roots
described [here](https://www.pantsbuild.org/docs/source-roots#configuring-no-source-roots).
