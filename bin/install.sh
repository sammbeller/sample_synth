#!/bin/bash

TMP_DIR="/tmp/sample_synth"

if hash virtualenv 2>/dev/null; then
  echo "virtualenv available"
else
  echo >&2 "virtualenv not available. Please install before continuing";
  exit 1;
fi

## Download sms-tools
echo "Downloading sms-tools"
mkdir $TMP_DIR
(cd $TMP_DIR && curl -LO "https://github.com/MTG/sms-tools/archive/master.zip")
unzip -q ${TMP_DIR}/master.zip -d $TMP_DIR
cp -R ${TMP_DIR}/sms-tools-master ./lib/sms-tools
rm -rf $TMP_DIR

source bin/activate
pip install -r requirements.txt
(cd lib/sms-tools/software/models/utilFunctions_C && python compileModule.py build_ext --inplace)
deactivate
