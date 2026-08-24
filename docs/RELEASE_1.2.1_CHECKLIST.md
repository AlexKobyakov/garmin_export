# Garmin Export 1.2.1 — release and support checklist

## Scope

Release 1.2.1 closes the bounded G0-G5 track. It contains the Qt5/Qt6 boundary,
UI and translation contract, 12-language flags/RTL support, dependency
reliability and the cancellation-safe export lifecycle. Processing Provider and
other feature work are outside this release.

## Runtime prerequisites

- QGIS 3.22+; owner smoke was run on QGIS 3.44 with Qt5 and QGIS 4.2 with Qt6.
- Java JRE 8+; use the Java diagnostics in the Tools tab.
- mkgmap and splitter must be complete ZIP distributions with their lib/
  directories. A standalone JAR without lib/ is rejected.

## Dependency source order

- Russian UI: Yandex.Disk -> GitHub wheels -> Dropbox -> official site.
- Other languages: official site -> GitHub wheels -> Dropbox -> Yandex.Disk.

The source repository may contain wheels/ mirrors. The installable ZIP does not
contain wheels/, plan/, tests/ or docs/.

## Export lifecycle checks

1. Start a normal export and confirm the success result.
2. Cancel during layer processing and during mkgmap; confirm no success message.
3. Close and reopen the dialog, then run again.
4. Confirm the output folder contains .garmin_export/run_manifest.json.
5. Confirm output path and size appear in the manifest only after success.
6. Confirm a failed or cancelled run leaves the previous tool installation usable.

## Offline release gates

- pytest -q: 155 passed.
- Critical and full Flake8: passed.
- compileall: passed.
- Bandit: passed.
- git diff --check: passed.

## Version and artifact

- metadata.txt version: 1.2.1.
- Git tag: v1.2.1.
- Build command: python scripts/build_plugin.py --output dist/garmin_export-1.2.1.zip.
