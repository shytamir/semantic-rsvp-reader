# S-035A Development Environment Contract Validation

## Automated Evidence

- The known-successful managed Windows environment runs Python `3.12.13` with Flask `3.1.3`, pytest `9.1.1`, Click `8.1.8`, spaCy `3.7.5`, and `en-core-web-sm` `3.7.1`; `python -m pip check` passes.
- A disposable clean Windows `core` environment installed from `requirements-core.txt`, reported the accepted Flask/pytest versions, passed `python -m pip check`, passed the rule-based smoke test, and passed 15 focused environment/service/storage tests.
- The current standard environment passes the pinned parser/API suite. A separate disposable clean `standard` installation did not finish within the automated execution window and is not recorded as passed.
- Ubuntu Python 3.12 and Node.js 22 are CI configuration claims; this preparation did not inspect a resulting remote run.
- POSIX procedures are documented but were not executed on this Windows host.

## Fixed Human Protocol

Use the committed [Development Environment Contract](../development/environment_contract.md) and record the target commit, shell, operating system, profile, and every command outcome.

1. In Windows PowerShell, follow the clean `standard` procedure from a new virtual environment. Confirm installation, `python -m pip check`, the accepted dependency versions, the parser-default smoke test, and `/health` identity. Record any unclear or incorrect step.
2. Confirm the environment-identity commands capture commit SHA, profile, Python, key dependency versions, and configured/active chunker state without manual reconstruction.
3. If a POSIX-compatible Python 3.12 environment is actually available, execute one documented profile procedure and record its result. If unavailable, record this step as `skipped`; do not mark it passed.
4. Review the configuration table against actual startup behavior, especially that only `RSVP_CHUNKER_MODE` has the documented app-config/environment precedence and that the three Flask-config-only settings are not presented as environment variables.
5. Record `passed`, `partially_passed`, `failed`, or `inconclusive`, plus any separate issue needed for a contradiction requiring application-level configuration redesign.

## Human Disposition

Validation failed in the first step of the protocol. no POSIX-compatible environment is actually available or necessary for this work. the rest of the protocol is blocked. Output of the error appended below:

```
python -m pip install -r requirements.txt
Collecting en-core-web-sm@ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl (from -r D:\Shy\semantic-rsvp-reader\requirements-nlp-spike.txt (line 7))
  Using cached https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl (12.8 MB)
Collecting Flask==3.1.3 (from -r D:\Shy\semantic-rsvp-reader\requirements-core.txt (line 1))
  Using cached flask-3.1.3-py3-none-any.whl.metadata (3.2 kB)
Collecting pytest==9.1.1 (from -r D:\Shy\semantic-rsvp-reader\requirements-core.txt (line 2))
  Using cached pytest-9.1.1-py3-none-any.whl.metadata (7.6 kB)
Collecting click==8.1.8 (from -r D:\Shy\semantic-rsvp-reader\requirements-nlp-spike.txt (line 5))
  Using cached click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting spacy==3.7.5 (from -r D:\Shy\semantic-rsvp-reader\requirements-nlp-spike.txt (line 6))
  Using cached spacy-3.7.5.tar.gz (1.3 MB)
  Installing build dependencies ... error
  error: subprocess-exited-with-error

  × installing build dependencies for spacy did not run successfully.
  │ exit code: 1
  ╰─> [559 lines of output]
      Ignoring numpy: markers 'python_version < "3.9"' don't match your environment
      Collecting setuptools
        Using cached setuptools-83.0.0-py3-none-any.whl.metadata (6.6 kB)
      Collecting cython<3.0,>=0.25
        Using cached Cython-0.29.37-py2.py3-none-any.whl.metadata (3.1 kB)
      Collecting cymem<2.1.0,>=2.0.2
        Using cached cymem-2.0.13-cp314-cp314-win_amd64.whl.metadata (9.9 kB)
      Collecting preshed<3.1.0,>=3.0.2
        Using cached preshed-3.0.13-cp314-cp314-win_amd64.whl.metadata (5.4 kB)
      Collecting murmurhash<1.1.0,>=0.28.0
        Using cached murmurhash-1.0.15-cp314-cp314-win_amd64.whl.metadata (2.3 kB)
      Collecting thinc<8.3.0,>=8.2.2
        Using cached thinc-8.2.5.tar.gz (193 kB)
        Installing build dependencies: started
        Installing build dependencies: finished with status 'error'
        error: subprocess-exited-with-error

        installing build dependencies for thinc did not run successfully.
        exit code: 1

        [534 lines of output]
        Ignoring numpy: markers 'python_version < "3.9"' don't match your environment
        Collecting setuptools
          Using cached setuptools-83.0.0-py3-none-any.whl.metadata (6.6 kB)
        Collecting cython<3.0,>=0.25
          Using cached Cython-0.29.37-py2.py3-none-any.whl.metadata (3.1 kB)
        Collecting murmurhash<1.1.0,>=1.0.2
          Using cached murmurhash-1.0.15-cp314-cp314-win_amd64.whl.metadata (2.3 kB)
        Collecting cymem<2.1.0,>=2.0.2
          Using cached cymem-2.0.13-cp314-cp314-win_amd64.whl.metadata (9.9 kB)
        Collecting preshed<3.1.0,>=3.0.2
          Using cached preshed-3.0.13-cp314-cp314-win_amd64.whl.metadata (5.4 kB)
        Collecting blis<0.8.0,>=0.7.8
          Using cached blis-0.7.11.tar.gz (2.9 MB)
          Installing build dependencies: started
          Installing build dependencies: finished with status 'done'
          Getting requirements to build wheel: started
          Getting requirements to build wheel: finished with status 'error'
          error: subprocess-exited-with-error

          Getting requirements to build wheel did not run successfully.
          exit code: 1

          [507 lines of output]

          Error compiling Cython file:
          ------------------------------------------------------------
          ...
          #
          # See __init__.cython-30.pxd for the real Cython header
          #

          # intentionally created compiler error that only triggers on Cython < 3.0.0
          DEF err = int('Build aborted: the NumPy Cython headers require Cython 3.0.0 or newer.')
                      ^
          ------------------------------------------------------------

          C:\Users\Usuario\AppData\Local\Temp\pip-build-env-t4fff4m2\overlay\Lib\site-packages\numpy\__init__.pxd:12:13: Error in compile-time expression: ValueError: invalid literal for int() with base 10: 'Build aborted: the NumPy Cython headers require Cython 3.0.0 or newer.'
		...
		  Error compiling Cython file:
          ------------------------------------------------------------
          ...
                          A.shape[0], A.shape[1],
                          alpha,
                          &A[0,0], A.shape[1], 1,
                          &B[0], 1,
                          beta,
                          <double*>out.data, 1)
                                     ^
          ------------------------------------------------------------

          blis\py.pyx:142:28: Accessing Python attribute not allowed without gil
          BLIS_COMPILER? None
          Compiling blis\cy.pyx because it changed.
          Compiling blis\py.pyx because it changed.
          [1/2] Cythonizing blis\cy.pyx
          [2/2] Cythonizing blis\py.pyx
          Traceback (most recent call last):
            File "D:\Shy\semantic-rsvp-reader\.venv\Lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 389, in <module>
              main()
              ~~~~^^
            File "D:\Shy\semantic-rsvp-reader\.venv\Lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 373, in main
              json_out["return_val"] = hook(**hook_input["kwargs"])
                                       ~~~~^^^^^^^^^^^^^^^^^^^^^^^^
            File "D:\Shy\semantic-rsvp-reader\.venv\Lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 143, in get_requires_for_build_wheel
              return hook(config_settings)
            File "C:\Users\Usuario\AppData\Local\Temp\pip-build-env-t4fff4m2\overlay\Lib\site-packages\setuptools\build_meta.py", line 333, in get_requires_for_build_wheel
              return self._get_build_requires(config_settings, requirements=[])
                     ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            File "C:\Users\Usuario\AppData\Local\Temp\pip-build-env-t4fff4m2\overlay\Lib\site-packages\setuptools\build_meta.py", line 301, in _get_build_requires
              self.run_setup()
              ~~~~~~~~~~~~~~^^
            File "C:\Users\Usuario\AppData\Local\Temp\pip-build-env-t4fff4m2\overlay\Lib\site-packages\setuptools\build_meta.py", line 317, in run_setup
              exec(code, locals())
              ~~~~^^^^^^^^^^^^^^^^
            File "<string>", line 305, in <module>
            File "C:\Users\Usuario\AppData\Local\Temp\pip-build-env-t4fff4m2\overlay\Lib\site-packages\Cython\Build\Dependencies.py", line 1115, in cythonize
              cythonize_one(*args)
              ~~~~~~~~~~~~~^^^^^^^
            File "C:\Users\Usuario\AppData\Local\Temp\pip-build-env-t4fff4m2\overlay\Lib\site-packages\Cython\Build\Dependencies.py", line 1238, in cythonize_one
              raise CompileError(None, pyx_file)
          Cython.Compiler.Errors.CompileError: blis\py.pyx
          [end of output]

          note: This error originates from a subprocess, and is likely not a problem with pip.
        ERROR: Failed to build 'blis' when getting requirements to build wheel
        [end of output]

        note: This error originates from a subprocess, and is likely not a problem with pip.
      ERROR: Failed to build 'thinc' when installing build dependencies for thinc
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.

[notice] A new release of pip is available: 25.3 -> 26.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip
ERROR: Failed to build 'spacy' when installing build dependencies for spacy
```