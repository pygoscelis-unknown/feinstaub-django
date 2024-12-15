#!/usr/bin/env bash
# exit on error
set -o errexit

if [ -f "./.env" ]; then
    source "./.env"

    if [ -z ${DJANGO_PROJECT_NAME+x} ]; then
        echo "DJANGO_PROJECT_NAME is unset."
    else
        DJANGO_SETTINGS_MODULE=$DJANGO_PROJECT_NAME.settings pylint --load-plugins pylint_django .;
    fi
fi
