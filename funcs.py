from MS.kvidea.store import Store
from MS.kvidea.store import MESSAGES
import pprint
import uuid


class Base:
    def __init__(self, namespace: str = None):
        self.store = Store()
        self.namespace = namespace

    def createBase(self):
        self.store = Store()
        self.store.save()

    def _showBase(self):
        self.store = Store()
        result = self.store.load()
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(self.store._store)

    def _createId(self):
        return uuid.uuid4().hex

    def createUser(self, document: dict, userKey: str):
        """
        Document = słownik z danymi użytkownika
        Key = klucz, którym identyfikowany będzie użytkownik
        """
        self.store = Store()
        result = self.store.load()

        result = self.store.get(userKey, namespace=self.namespace)

        if not result["deliver"]:
            idd = self._createId()
            document["_ii"] = idd
            result = self.store.put(userKey, document, namespace=self.namespace)
            result = self.store.save()
            print(MESSAGES.USER_ADDED)
        else:
            print(MESSAGES.USER_EXIST)

    def deleteUser(self, userKey: str):
        self.store = Store()
        result = self.store.load()
        result = self.store.get(userKey, namespace=self.namespace)
        if not result["deliver"]:
            print(MESSAGES.USER_DOES_NOT_EXISTS)
            return
        else:
            result = self.store.delete(userKey, namespace=self.namespace, guard=result["guard"])
            result = self.store.save()
            print(MESSAGES.USER_DELETED)

    def createFile(self, userKey: str, tags: list, document: dict):
        self.store = Store()
        result = self.store.load()

        result = self.store.get(userKey, namespace=self.namespace)
        if not result["deliver"]:
            print(MESSAGES.USER_DOES_NOT_EXISTS)
            return
        document["_ii"] = self._createId()

        for tag in tags:
            data = self.store.get(userKey + "_" + tag, namespace=self.namespace)
            if not data["deliver"]:
                result = self.store.put(userKey + "_" + tag, [document], namespace=self.namespace)
            else:
                data["value"].append(document)
                result = self.store.put(userKey + "_" + tag, data["value"], namespace=self.namespace,
                                        guard=data["guard"])

        result = self.store.save()
        print(MESSAGES.FILE_ADDED)

    def deleteFileFromTag(self, userKey: str, tag: str, fileName: str):
        self.store = Store()
        result = self.store.load()
        result = self.store.get(userKey + "_" + tag, namespace=self.namespace)
        if not result["deliver"]:
            print(MESSAGES.TAG_DOES_NOT_EXISTS)
            return
        files = result["value"]
        for file in files:
            if file["nazwa"] == fileName:
                files.remove(file)
                result = self.store.put(userKey + "_" + tag, files, namespace=self.namespace, guard=result["guard"])
                result = self.store.save()
                print(MESSAGES.FILE_DELETED)
                return
        print(MESSAGES.FILE_DOES_NOT_EXISTS)
        return

    def searchFileByTag(self, userKey: str, tag: str):
        self.store = Store()
        result = self.store.load()
        result = self.store.get(userKey + "_" + tag, namespace=self.namespace)
        if not result['deliver']:
            print(MESSAGES.TAG_DOES_NOT_EXISTS)
            return
        print(MESSAGES.FILES_FOUND)
        print(result["value"])

    def addTagToFile(self, userKey: str, newTag: str, fileName: str):
        self.store = Store()
        result = self.store.load()

        result = self.store.get(userKey, namespace=self.namespace)
        if not result["deliver"]:
            print(MESSAGES.USER_DOES_NOT_EXISTS)
            return

        namespace = self.namespace
        if namespace is None:
            namespace = "__default__"

        for key in self.store._store[namespace].keys():
            if key.startswith(userKey + "_"):
                result = self.store.get(key, namespace=self.namespace)
                files = result["value"]
                for file in files:
                    if file["nazwa"] == fileName:
                        data = self.store.get(userKey + "_" + newTag, namespace=self.namespace)
                        if not data["deliver"]:
                            result = self.store.put(userKey + "_" + newTag, [file], namespace=self.namespace)
                            self.store.save()
                            print(MESSAGES.TAG_ADDED)
                            return
                        else:
                            data["value"].append(file)
                            result = self.store.put(userKey + "_" + newTag, data["value"], namespace=self.namespace,
                                                    guard=data["guard"])
                            self.store.save()
                            print(MESSAGES.TAG_ADDED)
                            return

    def deleteTag(self, userKey: str, tag: str):
        self.store = Store()
        result = self.store.load()
        result = self.store.get(userKey + "_" + tag, namespace=self.namespace)
        if not result["deliver"]:
            print(MESSAGES.TAG_DOES_NOT_EXISTS)
            return

        result = self.store.delete(userKey + "_" + tag, namespace=self.namespace, guard=result["guard"])
        result = self.store.save()
        print(MESSAGES.TAG_DELETED)
