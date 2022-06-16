#!/bin/bash

set -euxo pipefail

OUTPUT_ZIP="recordingdate.zip"

mkdir -p _build
rm -Rf _build/recordingdate
mkdir -p _build/recordingdate
cp __init__.py recording_date.py _build/recordingdate/

rm _build/"$OUTPUT_ZIP"
(cd _build && zip "$OUTPUT_ZIP"  recordingdate/*)
