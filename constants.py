class MESSAGES:
    OK_CODE = 100
    USER_ADDED_CODE = 101
    FILE_ADDED_CODE = 102
    TAG_ADDED_CODE = 103
    USER_DELETED_CODE = 104
    TAG_DELETED_CODE = 105
    FILE_DELETED_CODE = 106
    FILES_FOUND_CODE = 107

    INCORRECT_NAMESPACE_CODE = 202
    INCORRECT_TYPE_CODE = 207
    INCORRECT_GUARD_CODE = 206
    INCORRECT_KEY_CODE = 205
    USER_EXISTS_CODE = 210
    USER_DOES_NOT_EXISTS_CODE = 211
    TAG_DOES_NOT_EXISTS_CODE = 212
    FILE_NOT_EXISTS_CODE = 213

    OK = {"code": OK_CODE, "deliver": True, "description": "OK"}
    USER_ADDED = {"code": USER_ADDED_CODE, "deliver": True, "description": "User added"}
    FILE_ADDED = {"code": FILE_ADDED_CODE, "deliver": True, "description": "File added"}
    TAG_ADDED = {"code": TAG_ADDED_CODE, "deliver": True, "description": "Tag added"}
    USER_DELETED = {"code": USER_DELETED_CODE, "deliver": True, "description": "User deleted"}
    TAG_DELETED = {"code": TAG_DELETED_CODE, "deliver": True, "description": "Tag deleted"}
    FILE_DELETED = {"code": FILE_DELETED_CODE, "deliver": True, "description": "File deleted"}
    FILES_FOUND = {"code": FILES_FOUND_CODE, "deliver": True, "description": "Files found"}

    INCORRECT_TYPE = {"code": INCORRECT_TYPE_CODE, "deliver": False, "description": "Incorrect type"}
    INCORRECT_NAMESPACE = {"code": INCORRECT_NAMESPACE_CODE, "deliver": False, "description": "Incorrect namespace"}
    INCORRECT_GUARD = {"code": INCORRECT_GUARD_CODE, "deliver": False, "description": "Incorrect guard"}
    INCORRECT_KEY = {"code": INCORRECT_KEY_CODE, "deliver": False, "description": "Incorrect key"}
    USER_EXIST = {"code": USER_EXISTS_CODE, "deliver": False, "description": "User already exists"}
    USER_DOES_NOT_EXISTS = {"code":  USER_DOES_NOT_EXISTS_CODE, "deliver": False, "description": "User doesn't exist"}
    TAG_DOES_NOT_EXISTS = {"code": TAG_DOES_NOT_EXISTS_CODE, "deliver": False, "description": "Tag doesn't exist"}
    FILE_DOES_NOT_EXISTS = {"code": FILE_NOT_EXISTS_CODE, "deliver": False, "description": "File doesn't exist"}

    @classmethod
    def ok(cls, value, guard):
        result = cls.OK.copy()
        result["value"] = value
        result["guard"] = guard

        return result
