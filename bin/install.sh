#!/bin/bash

if hash virtualenv 2>/dev/null; then
  echo "virtualenv available"
else
  echo >&2 "virtualenv not available. Please install before continuing";
  exit 1;
fi
