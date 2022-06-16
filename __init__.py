PLUGIN_NAME = "Recording date"
PLUGIN_AUTHOR = "Aaron VonderHaar (avh4)"
PLUGIN_DESCRIPTION = '''
This plugin has the goal of tagging music with the original recording date,
but also provides several additional variables for use in scripting.

Details at <a href="https://github.com/avh4/picard-recordingdate/#readme">https://github.com/avh4/picard-recordingdate/#readme</a>
'''
PLUGIN_VERSION = '0.1.0'
PLUGIN_API_VERSIONS = ['2.7', '2.8']
PLUGIN_LICENSE = "MIT"
PLUGIN_LICENSE_URL = "https://opensource.org/licenses/MIT"

from picard.plugins.recordingdate.recording_date import add_track_metadata

from picard import config, log
from picard.metadata import (register_track_metadata_processor)

def process_track(album, metadata, track, release):
    return add_track_metadata(metadata, track)

register_track_metadata_processor(process_track)
