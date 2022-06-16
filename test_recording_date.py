import unittest

from recording_date import add_recording_metadata

def track_with_relation(relation):
    return track_with_relations([relation])

def track_with_relations(relations):
    return {
        "relations": relations,
    }

class ScriptVariablesTest(unittest.TestCase):
    def test_with_both_dates(self):
        metadata = {}

        track = track_with_relation({
            "target-type": "work",
            "type": "performance",
            "direction": "forward",
            "begin": "1932-04-03",
            "end": "1932-04-04",
        })
        add_recording_metadata(metadata, track)

        self.assertEqual(metadata["~work:forward:performance:begin"], "1932-04-03")
        self.assertEqual(metadata["~work:forward:performance:end"], "1932-04-04")
        self.assertEqual(metadata["~work:forward:performance:first"], "1932-04-03")
        self.assertEqual(metadata["~work:forward:performance:last"], "1932-04-04")

    def test_with_no_dates(self):
        metadata = {}

        track = track_with_relation({
            "target-type": "work",
            "type": "performance",
            "direction": "forward",
            "begin": None,
            "end": None,
        })
        add_recording_metadata(metadata, track)

        self.assertEqual(metadata["~work:forward:performance:begin"], None)
        self.assertEqual(metadata["~work:forward:performance:end"], None)
        self.assertEqual(metadata["~work:forward:performance:first"], None)
        self.assertEqual(metadata["~work:forward:performance:last"], None)

    def test_with_begin_date(self):
        metadata = {}

        track = track_with_relation({
            "target-type": "work",
            "type": "performance",
            "direction": "forward",
            "begin": "1932-04-03",
            "end": None,
        })
        add_recording_metadata(metadata, track)

        self.assertEqual(metadata["~work:forward:performance:begin"], "1932-04-03")
        self.assertEqual(metadata["~work:forward:performance:end"], None)
        self.assertEqual(metadata["~work:forward:performance:first"], "1932-04-03")
        self.assertEqual(metadata["~work:forward:performance:last"], "1932-04-03")

    def test_with_end_date(self):
        metadata = {}

        track = track_with_relation({
            "target-type": "work",
            "type": "performance",
            "direction": "forward",
            "begin": None,
            "end": "1932-04-04",
        })
        add_recording_metadata(metadata, track)

        self.assertEqual(metadata["~work:forward:performance:begin"], None)
        self.assertEqual(metadata["~work:forward:performance:end"], "1932-04-04")
        self.assertEqual(metadata["~work:forward:performance:first"], "1932-04-04")
        self.assertEqual(metadata["~work:forward:performance:last"], "1932-04-04")

    def test_relationship_type_with_space(self):
        metadata = {}

        track = track_with_relation({
            "target-type": "area",
            "type": "recorded in",
            "direction": "backward",
            "begin": "1932-04-03",
            "end": None,
        })
        add_recording_metadata(metadata, track)

        self.assertEqual(metadata["~area:backward:recorded_in:begin"], "1932-04-03")

class MetadataTest(unittest.TestCase):
    def test_standalone_recording(self):
        metadata = {}

        track = {
            "relations": [
                {
                    "target-type": "work",
                    "type": "performance",
                    "direction": "forward",
                    "begin": "1932-04-03",
                    "end": "1932-04-04",
                }
            ]
        }
        add_recording_metadata(metadata, track)

        self.assertEqual(metadata["recordingdate"], "1932-04-04")

    def test_recorded_in_date(self):
        metadata = {}

        track = track_with_relation({
            "target-type": "area",
            "type": "recorded in",
            "direction": "backward",
            "begin": "1932-04-03",
            "end": "1932-04-04",
        })
        add_recording_metadata(metadata, track)

        self.assertEqual(metadata["recordingdate"], "1932-04-04")

    def test_recorded_at_place_date(self):
        metadata = {}

        track = track_with_relations([
            {
                "target-type": "area",
                "type": "recorded in",
                "direction": "backward",
                "begin": "1932-04-03",
                "end": "1932-04-04",
            }, {
                "target-type": "place",
                "type": "recorded at",
                "direction": "backward",
                "begin": "1932-04-05",
                "end": "1932-04-06",
            }
        ])
        add_recording_metadata(metadata, track)

        self.assertEqual(metadata["recordingdate"], "1932-04-06")

    def test_recorded_at_event_date(self):
        metadata = {}

        track = track_with_relations([
            {
                "target-type": "area",
                "type": "recorded in",
                "direction": "backward",
                "begin": "1932-04-03",
                "end": "1932-04-04",
            }, {
                "target-type": "place",
                "type": "recorded at",
                "direction": "backward",
                "begin": "1932-04-05",
                "end": "1932-04-06",
            }, {
                "target-type": "event",
                "type": "recorded at",
                "direction": "backward",
                "begin": "1932-04-07",
                "end": "1932-04-08",
            }
        ])
        add_recording_metadata(metadata, track)

        self.assertEqual(metadata["recordingdate"], "1932-04-08")

    def test_performance_date(self):
        metadata = {}

        track = track_with_relations([
            {
                "target-type": "area",
                "type": "recorded in",
                "direction": "backward",
                "begin": "1932-04-03",
                "end": "1932-04-04",
            }, {
                "target-type": "place",
                "type": "recorded at",
                "direction": "backward",
                "begin": "1932-04-05",
                "end": "1932-04-06",
            }, {
                "target-type": "event",
                "type": "recorded at",
                "direction": "backward",
                "begin": "1932-04-07",
                "end": "1932-04-08",
            }, {
                "target-type": "work",
                "type": "performance",
                "direction": "forward",
                "begin": "1932-04-09",
                "end": "1932-04-10",
            }
        ])
        add_recording_metadata(metadata, track)

        self.assertEqual(metadata["recordingdate"], "1932-04-10")

    def test_performance_date_no_end(self):
        metadata = {}

        track = track_with_relation({
            "target-type": "work",
            "type": "performance",
            "direction": "forward",
            "begin": "1932-04-03",
            "end": None,
        })
        add_recording_metadata(metadata, track)

        self.assertEqual(metadata["recordingdate"], "1932-04-03")

if __name__ == '__main__':
    unittest.main()
