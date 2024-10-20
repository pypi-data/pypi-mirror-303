class DynamicObject:
    def __init__(self, **entries):
        self.__dict__.update(entries)

    def __repr__(self):
        return f"{self.__dict__}"


def normalize_pandas_dataFrame_to_objects(pandas_data):
    try:
        if len(pandas_data):
            normalized_obj = [DynamicObject(**row.to_dict()) for _, row in pandas_data.iterrows()]
            return normalized_obj
        else:
            return []
    except Exception as error:
        return f"There is something wrong: {error}"