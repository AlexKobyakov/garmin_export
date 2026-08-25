# GitHub repository profile

The repository About panel is remote GitHub metadata and is not stored in the
working tree. Recommended values:

- Description: QGIS plugin for exporting vector layers to Garmin IMG maps via mkgmap; Qt5/Qt6, 12-language UI, TYP styling, Processing Toolbox/Modeler algorithms and reliable cancellation-safe workflows.
- Homepage: https://github.com/AlexKobyakov/garmin_export
- Topics: qgis, qgis-plugin, pyqgis, garmin, garmin-img, mkgmap, gis, vector-data, map-export, qt5, qt6, typ, multilingual

After authenticating GitHub CLI, apply them with:

~~~bash
gh repo edit AlexKobyakov/garmin_export   --description "QGIS plugin for exporting vector layers to Garmin IMG maps via mkgmap; Qt5/Qt6, 12-language UI, TYP styling, Processing Toolbox/Modeler algorithms and reliable cancellation-safe workflows."   --homepage "https://github.com/AlexKobyakov/garmin_export"   --add-topic qgis --add-topic qgis-plugin --add-topic pyqgis   --add-topic garmin --add-topic garmin-img --add-topic mkgmap   --add-topic gis --add-topic vector-data --add-topic map-export   --add-topic qt5 --add-topic qt6 --add-topic typ --add-topic processing --add-topic qgis-modeler --add-topic multilingual
~~~

This command requires an authenticated gh auth login; no credentials are
stored in the repository.
