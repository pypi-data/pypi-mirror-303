import json
import os


class DictFile:
    """
    # Usage
    ```
    df = DictFile("mydict.json") # Use it like a regular dictionary
    df["key1"] = "value1"
    df["key2"] = [1, 2, 3]

    print(df["key1"])  # Outputs: value1
    print(len(df))  # Outputs: 2, The changes are automatically saved to "mydict.json"

    # You can also use other dictionary methods
    df.update({"key3": "value3", "key4": {"nested": "dict"}})
    print(df.keys())  # Outputs: dict_keys(['key1', 'key2', 'key3', 'key4'])

    # Clear the dictionary
    # df.clear()
    # The file "mydict.json" will now contain an empty JSON object: {}
    ```
    """

    def __init__(self, filename):
        self.filename = filename
        self.data = {}
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.data = json.load(f)

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent="\t")

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value
        self.save()

    def __delitem__(self, key):
        del self.data[key]
        self.save()

    def __contains__(self, key):
        return key in self.data

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()

    def get(self, key, default=None):
        return self.data.get(key, default)

    def clear(self):
        self.data.clear()
        self.save()

    def update(self, *args, **kwargs):
        self.data.update(*args, **kwargs)
        self.save()

    def pop(self, key, default=None):
        value = self.data.pop(key, default)
        self.save()
        return value

    def popitem(self):
        item = self.data.popitem()
        self.save()
        return item

    def setdefault(self, key, default=None):
        if key not in self.data:
            self.data[key] = default
            self.save()
        return self.data[key]

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"DictFile({self.filename})"
