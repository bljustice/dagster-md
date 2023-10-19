#!/bin/bash

DEPOT_DIRECTORY="$(pwd)/dagstermd/depot"

if [ -d "$DEPOT_DIRECTORY" ]; then
  echo "$DEPOT_DIRECTORY already exists. Deleting."
  rm -rf "$DEPOT_DIRECTORY"
fi

echo "Cloning dbt project"
git clone https://github.com/bljustice/depot $DEPOT_DIRECTORY

echo "Running dbt dependencies and creating manifest"
dbt deps --project-dir ./dagstermd/depot --profiles-dir ./dagstermd/depot
dbt parse --project-dir ./dagstermd/depot --profiles-dir ./dagstermd/depot

echo "Launching dagster dev"
dagster dev
