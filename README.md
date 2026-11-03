# printer-driver-version-checker

Check every printer's driver against the minimum version for its model, so outdated drivers are found before users report print failures.

## How to run

```sh
python3 main.py printers.csv
```

## Example output

```
PRN-01: OK (meets minimum)
PRN-02: OUTDATED (below minimum 2.1)
1 printer(s) with outdated drivers.
```

Standard library only. Run the tests with `python3 -m unittest discover`.
