PLUGIN_NAME = "Recording date"
PLUGIN_AUTHOR = "Aaron VonderHaar (avh4)"
PLUGIN_DESCRIPTION = '''
This plugin has the goal of tagging music with the original recording date,
but also provides several additional variables for use in scripting.

Details at <a href="https://github.com/avh4/picard-recordingdate/#readme">https://github.com/avh4/picard-recordingdate/#readme</a>
'''
PLUGIN_VERSION = '0.1.0'
PLUGIN_API_VERSIONS = ['2.7']
PLUGIN_LICENSE = "MIT"
PLUGIN_LICENSE_URL = "https://opensource.org/licenses/MIT"

from picard.plugins.recordingdate.recording_date import add_recording_metadata

from picard import config, log
from picard.metadata import (register_track_metadata_processor)

def process_track(album, metadata, track, release):
    if track.get("recording"):
        # It's a track from a release
        recording = track["recording"]
    else:
        # It's a standalone recording
        recording = track

    def on_result(response, reply, error):
        if not error:
            add_recording_metadata(metadata, response)
        album._requests -= 1
        album._finalize_loading(error)

    album._requests += 1
    album.tagger.webservice.get(
        config.setting["server_host"],
        config.setting["server_port"],
        "/ws/2/%s/%s" % ('recording', recording["id"]),
        on_result,
        queryargs={"inc": "area-rels+artist-rels+event-rels+place-rels+work-rels"},
    )

register_track_metadata_processor(process_track)
