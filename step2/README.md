# Step 2

- NOTE that running `./pants tailor ::` at this point accomplishes nothing,
  although it produces output that seems to indicate everything is OK.

- add `backend_packages = ["pants.backend.python"]` to `pants.toml`

- `pants.toml` now looks like this:

```
[GLOBAL]
pants_version = "2.14.0"
backend_packages = ["pants.backend.python"]
```

- Now when you run `./pants tailor ::`, the `BUILD` files will be
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

- Pants also complains about `[anonymous-telemetry]`. To silence this,
  add to the end of `pants.toml`:

```
[anonymous-telemetry]
enabled = false
```

- At this point, pants *seems* to be configured. But running `./pants test ::`
  does nothing, and running `./pants run main/main.py` produces an error message.
