from typing import Any
import pickle, json


def load_pkl(path: str) -> Any:
    """Load a pickle."""

    if not path.endswith(".pkl"):
        path += ".pkl"

    f = open(path, "rb")
    content = pickle.load(f)
    f.close()
    return content


def save_pkl(obj: Any, path: str) -> None:
    """Create a pickle file out of the given object."""

    if not path.endswith(".pkl"):
        path += ".pkl"

    f = open(path, "wb")
    pickle.dump(obj, f)
    f.close()


def load_json(path: str) -> object:
    """Read the JSON file and gets its content."""

    if not path.endswith(".json"):
        path += ".json"

    f = open(path)
    obj = json.load(f)
    f.close()
    return obj


def save_json(obj: object, path: str) -> None:
    """Replace the JSON file with the given object."""

    if not path.endswith(".json"):
        path += ".json"

    f = open(path, "w")
    f.write(json.dumps(obj, indent=4, ensure_ascii=False))
    f.close()
