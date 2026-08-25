# Garmin Export 1.2.1 — release and support checklist

## Scope

The 1.2.1 release includes the previously planned 1.2.0 modernization scope.
There is no separate 1.2.0 tag or archive: the Qt5/Qt6 boundary, UI contract,
bounded GUI refactor and 12-language/i18n work were completed and released
together with the G4/G5 reliability work as 1.2.1.

The carried scope includes:

- shared QGIS 3/Qt5 and QGIS 4/Qt6 compatibility helpers and checker guards;
- retranslate-safe composite widgets/dialogs, retained layout references,
  translated tooltips/placeholders/actions and readable combo/check controls;
- 12-language registry, SVG flags, Arabic RTL, live/restart persistence and
  translation parity tests;
- production Python modules bounded to 500 lines or less.


Release 1.2.1 closes the bounded G0-G5 track. It contains the Qt5/Qt6 boundary,
UI and translation contract, 12-language flags/RTL support, dependency
reliability and the cancellation-safe export lifecycle. Processing Provider work is tracked as the post-1.2.1 G6 feature scope;
the current branch contains the implementation and owner smoke confirmation,
while the separate 1.3.0 release gate remains a metadata/tag decision.

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

- pytest -q: 167 passed (current branch baseline).
- Critical and full Flake8: passed.
- compileall: passed.
- Bandit: passed.
- git diff --check: passed.

## Version and artifact

- metadata.txt version: 1.2.1.
- Git tag: v1.2.1.
- Build command: python scripts/build_plugin.py --output dist/garmin_export-1.2.1.zip.

## Post-1.2.1 Processing smoke

For the G6 feature scope, repeat in QGIS 3.44/Qt5 and QGIS 4.2/Qt6:

1. Confirm the Garmin Export group and plugin icon in Processing -> Toolbox.
2. Run environment validation with valid and invalid Java/mkgmap/splitter paths.
3. Validate mapping JSON, build TYP, and generate an MP preview.
4. Run IMG export with generated, existing and disabled TYP modes, levels,
   code page and advanced tuning.
5. Run dependency diagnostics with AUTO_DOWNLOAD off and on only when network
   access is intended.
6. Check STATUS, ERRORS, MANIFEST and cancellation behavior.
7. Open the algorithms in Modeler and run a small batch with distinct outputs.

The owner confirmed the QGIS 3.44 and 4.2 smoke matrix for the current branch.
