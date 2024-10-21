from typing import List, Any, Dict, Union

class IndexableEventLog:
    def __init__(self, decoded_topics: List[Any], decoded_data: List[Any], param_names: Dict[str, int] = None):
        self.topics = decoded_topics
        self.data = decoded_data
        self.param_names = param_names or {}

    def __getitem__(self, key: Union[int, str]) -> Any:
        if isinstance(key, int):
            if key < len(self.topics):
                return self.topics[key]
            else:
                return self.data[key - len(self.topics)]
        elif isinstance(key, str):
            if self.param_names:
                index = self.param_names.get(key)
                if index is not None:
                    return self[index]
            raise KeyError(f"Parameter name '{key}' not found or named indexing is not supported for this event")
        else:
            raise TypeError("Invalid key type. Use int for index or str for name.")

    def __len__(self):
        return len(self.topics) + len(self.data)

    def __str__(self):
        return f"IndexableEventLog(topics={self.topics}, data={self.data})"

    def __repr__(self):
        return self.__str__()

class IndexableTransactionInput:
    def __init__(self, decoded_params: List[Any], param_names: Dict[str, int] = None):
        self.params = decoded_params
        self.param_names = param_names or {}

    def __getitem__(self, key: Union[int, str]) -> Any:
        if isinstance(key, int):
            return list(self.params.values())[key]
        elif isinstance(key, str):
            if key in self.params:
                return self.params[key]
            elif self.param_names:
                index = self.param_names.get(key)
                if index is not None:
                    return list(self.params.values())[index]
            raise KeyError(f"Parameter name '{key}' not found or named indexing is not supported for this transaction")
        else:
            raise TypeError("Invalid key type. Use int for index or str for name.")

    def __len__(self):
        return len(self.params)

    def __str__(self):
        return f"IndexableTransactionInput(params={self.params})"

    def __repr__(self):
        return self.__str__()