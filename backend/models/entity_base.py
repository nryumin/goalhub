class EntityBase:
    def __init__(self, data):
        for key in data.keys():
            if not key.startswith("__"):
                setattr(self, key, data[key])

    def get_dto(self):
        result = {}

        for field in self.dto_fields:
            if hasattr(self, field):
                result[field] = getattr(self, field)

        result['_id'] = str(result['_id'])
        return result
