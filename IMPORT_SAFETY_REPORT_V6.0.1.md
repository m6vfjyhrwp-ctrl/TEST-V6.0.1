# Import Safety Report

Imports are limited to JSON files up to 12 MB, parsed only as data, validated for expected structure and collection limits, and recursively rejected when dangerous prototype keys or excessive nesting are found. Existing state is retained on failure and a recovery snapshot is created before confirmed application.
