import json
from remodel.object_handler import ObjectSet


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectSet):
            return list(obj)
        elif hasattr(obj, "__json__"):
            return obj.__json__()
        return json.JSONEncoder.default(self, obj)


def json_dumps(obj):
    return json.dumps(obj, cls=JSONEncoder)
