from collections import ChainMap

def script_variables_for_relation(rel):
    key_base = '~{}:{}:{}'.format(rel["target-type"], rel["direction"], rel["type"])
    non_none = list(filter(lambda x: x is not None, [rel["begin"], rel["end"]]))
    return {
        key_base + ':begin': rel["begin"],
        key_base + ':end': rel["end"],
        key_base + ':first': min(non_none, default=None),
        key_base + ':last': max(non_none, default=None),
    }

def script_variables_for_recording(recording):
    relations = recording["relations"]
    script_variables = dict(ChainMap(*map(script_variables_for_relation, relations)))
    return script_variables

def add_recording_metadata(metadata, recording):
    relations = script_variables_for_recording(recording)
    for rel, date in relations.items():
        metadata[rel] = date
    metadata["recordingdate"] = relations.get("~work:forward:performance:last")
