#!/bin/bash

set -euxo pipefail

./build.sh
cp -v _build/recordingdate.zip ~/Library/Preferences/MusicBrainz/Picard/plugins/recordingdate.zip
