# Step 2: Run Pants Tailor

- Copy the contents of the directory `1_install_pants` into a new directory and
  **`cd`** into it.

- To make Pants runnable you must execute **`chmod +x ./pants`**.

- NOTE that running **`./pants tailor ::`** at this point accomplishes nothing,
  although it produces output that seems to indicate everything is OK.

- add `backend_packages = ["pants.backend.python"]` to `pants.toml`

- `pants.toml` now looks like this:
  ```
  [GLOBAL]
  pants_version = "2.14.0"
  backend_packages = ["pants.backend.python"]
  ```

- Now when you run **`./pants tailor ::`**, the `BUILD` files will be
  created. You will see:
  ```
  Created main/BUILD:
    - Add python_sources target main
    - Add python_requirements target reqs
  Created test/BUILD:
    - Add python_tests target tests
  Created util/BUILD:
    - Add python_sources target util
  ```

- Note that each subdirectory now contains a `BUILD` file.

- Pants also complains about `[anonymous-telemetry]`. To silence this,
  add this to the end of `pants.toml`:
  ```
  [anonymous-telemetry]
  enabled = false
  ```

- Now run **`./pants test ::`** and you should see output like this:
  ```
  19:12:20.99 [INFO] Completed: Run Pytest - test/math_test.py:tests succeeded.
  19:12:20.99 [INFO] Completed: Run Pytest - test/main_test.py:tests succeeded.
  19:12:21.00 [INFO] Completed: Run Pytest - test/string_test.py:tests succeeded.

  ✓ test/main_test.py:tests succeeded in 0.26s.
  ✓ test/math_test.py:tests succeeded in 0.26s.
  ✓ test/string_test.py:tests succeeded in 0.27s.
  ```

- If you run **`./pants run main/main.py`** you should see output like this:
  ```
    Hello world!
  sys.version = '3.9.15 (main, Oct 12 2022, 19:14:37) \n[GCC 11.2.0]'
  ```
