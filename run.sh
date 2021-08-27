#!/bin/bash
flask db upgrade
PYTHONPATH=/var/code python -m schlepwise_api runserver
