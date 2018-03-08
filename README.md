# email-backup-converter
This script splits raw email folder backup files into to single email files which you can then import using a tool like ImportExportTools (https://addons.mozilla.org/de/thunderbird/addon/importexporttools/)

By default this script expects backups in the subdirectory `email-backup` and saves the converted emails to `email-backup`. Both directories must exist. Default charset is `ANSI`. Edit converter.py to change any of these defaults.
