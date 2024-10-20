# PyImportCheck

<p align="center">
  <img src="https://github.com/user-attachments/assets/b245ace4-40a1-4372-99f2-77fdea12d6f6">
</p>

Pyimportcheck is
[a static code analyser](https://en.wikipedia.org/wiki/Static_program_analysis)
for Python 3.

This project aims to provide quick detection of:
-  circular imports flow
-  missing exported symbols (special `__all__` symbol)
-  bad package declaration (missing of `__init__.py` files)

Pyimportcheck analyses your code without actually running it. It checks for
errors, enforces a coding standard, and can make suggestions about how the code
could be refactored (see the screenshot above).

> [!WARNING]
> This project was originaly designed for my personal use to quickly detect arbitrary
> "errors" (e.g exported symbols) in some "big" projects since the report from the
> python interpreter is not easy to interpret for some edge cases (like circular import)
>
> Note that you probably want to use [CodeQL](https://github.com/github/codeql) with
> [default python query](https://github.com/github/codeql/blob/main/python/ql/src/Imports/CyclicImport.ql)
> that can perform the same job as my tool.
>
> If you want to know what I plan to do with this project, you can check the
> [Roadmap issue](https://github.com/YannMagnin/PyImportCheck/issues/1) that evolves
> with time

## Install

Install and update using [pip](https://pip.pypa.io/en/stable/getting-started/)
or [poetry](https://python-poetry.org/docs/):
```bash
pip install pyimportcheck
poetry add pyimportcheck
```

> [!NOTE]
> Stable branches are named as `<version>` (e.g `0.1`) (the `master` has been reserved
> for the next release), so, if you plan to build manually the project, do not forget to switch
> to the appropriate branch before !

## How to use

You can use the `--help` flag to display information about what you can do with this tool.
Most of the time, you simply need to indicate the path name to the package or file you
want to check.
```bash
pyimportcheck /path/to/local/package
```

You can export any detected notification into a (rudumentary) JSON format with `--json`
followed by the output path. You can also use `--json-only` to only perform the export
without displaying anything:
```bash
pyimportcheck /path/to/local/file.py --json-only /path/to/json_output_file.json
```

## Notes

> [!TIP]
> I recommend you resolve each circular dependency in the order that they
> are displayed. This is because I do not detect if a circular import has
> already been detected (It will be the case in the future).
>
> So, resolving one circular import can clear, at least, two errors (or more
> if you have a long loop)

> [!CAUTION]
> This project only supports "absolute" imports `from <package> ... import ...` and
> `import <package> ...`. Canonical imports (like `from .<module> ... import ...`)
> and special workarounds, like with `typing.TYPE_CHEKING`, are not supported
> (ignored for now).
