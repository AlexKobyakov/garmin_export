# Garmin Export 1.3.0 — release checklist

## Scope

Release 1.3.0 delivers the G6 Processing Provider and G7 release hardening:

- seven algorithms under Processing → Toolbox → Garmin Export;
- QGIS Modeler, Batch and processing.run() support with stable ASCII parameter IDs;
- TYP modes, code-page and mapping JSON validation, MP preview;
- dependency diagnostics/download with opt-in network access and auto-discovery;
- typed mkgmap tuning, project-layer batch export and explicit run manifest output;
- plugin-only release ZIP packaging and the Qt6 checker rewrite/diff guard.

## Release gates

- Owner smoke confirmed QGIS 3.44/Qt5 and QGIS 4.2/Qt6.
- pytest: 167 passed.
- Full flake8, compileall and Bandit: passed.
- Build and verify:

  python scripts/build_plugin.py --output dist/garmin_export-1.3.0.zip
  python scripts/verify_plugin_archive.py dist/garmin_export-1.3.0.zip

The verified ZIP must contain only the garmin_export/ plugin tree and must not
contain docs, tests, plan, wheels, scripts, CI files, examples or JAR files.

## GitHub publication

Create tag v1.3.0 through the normal repository workflow. The release workflow
builds and uploads the named asset garmin_export-1.3.0.zip. Users must download
that asset rather than GitHub's automatically generated Source code archive.
