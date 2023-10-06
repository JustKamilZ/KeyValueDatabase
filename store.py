import uuid
import json
from constants import MESSAGES


class Store:

    def __init__(self):
        self._store = {"__default__": {}}
        self._currentNamespace = None

    def createNamespace(self, namespace):
        if namespace == "__default__":
            return MESSAGES.INCORRECT_NAMESPACE

        self._store[namespace] = {}
        return MESSAGES.OK

    def put(self, key, value, *, namespace=None, guard=None):
        namespace = self._checkNamespace(namespace)
        if namespace is None:
            return MESSAGES.INCORRECT_NAMESPACE

        if not self._guardKVArgs(key):
            return MESSAGES.INCORRECT_TYPE

        if not (namespace in self._store):
            self._store[namespace] = {}

        if key in self._store[namespace]:
            elem = self._store[namespace][key]
            if elem["guard"] == guard:
                elem["guard"] = uuid.uuid4().hex
                elem["value"] = value
            else:
                return MESSAGES.INCORRECT_GUARD

        else:
            self._store[namespace][key] = {"value": value, "guard": uuid.uuid4().hex}

        return MESSAGES.OK

    def get(self, key, *, namespace=None):
        namespace = self._checkNamespace(namespace)
        if namespace is None:
            return MESSAGES.INCORRECT_NAMESPACE

        if not isinstance(key, str) and len(key) > 0:
            return MESSAGES.INCORRECT_TYPE

        if not (namespace in self._store):
            return MESSAGES.INCORRECT_NAMESPACE

        if not (key in self._store[namespace]):
            return MESSAGES.INCORRECT_KEY

        if isinstance(self._store[namespace][key]["value"], dict) or isinstance(
            self._store[namespace][key]["value"],
                list):

            value = self._store[namespace][key]["value"].copy()
        else:
            value = self._store[namespace][key]["value"]

        return MESSAGES.ok(
                value,
                self._store[namespace][key]["guard"]
                )

    def delete(self, key, *, namespace=None, guard=None):
        namespace = self._checkNamespace(namespace)

        if namespace is None:
            return MESSAGES.INCORRECT_NAMESPACE

        if not isinstance(key, str) and len(key) > 0:
            return MESSAGES.INCORRECT_TYPE

        if not (namespace in self._store):
            return MESSAGES.INCORRECT_NAMESPACE

        if key in self._store[namespace]:
            elem = self._store[namespace][key]
            if elem["guard"] == guard:
                del self._store[namespace][key]
                return MESSAGES.OK
            else:
                return MESSAGES.INCORRECT_GUARD
        else:
            return MESSAGES.INCORRECT_KEY

    def _checkNamespace(self, namespace):
            if namespace == "__default__":
                return None
            elif namespace is None:
                if not self._currentNamespace is None:
                    return self._currentNamespace
                else:
                    return "__default__"
            return namespace

    def _guardKVArgs(self, key):
        if isinstance(key, str) and len(key) > 0:
            return True
        else:
            return False

    def save(self):
        file = open("baza.json", "w")
        json.dump(self._store, file)
        file.close()
        return MESSAGES.OK

    def load(self):
        file = open("baza.json", "r")
        self._store = json.load(file)
        file.close()
        return MESSAGES.OK
