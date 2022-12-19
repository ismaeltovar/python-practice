
class NoHashElement(Exception):
    """Exception to indicate that element was not found in hash map.
    
    Arguments:
    key -- key that was searched for
    """

    def __init__(self, key):
        self.key = key

    def __str__(self):
        return f"Hash element not found with key {self.key}"


class HashMap():
    def __init__(self):
        self.map = []
        self.entries = 0
        self.size = 8
        self.create_entries(self.size)

    def create_entries(self, num):
        """Create a certain amount of entries for the hash map.
        
        Initialized entries are in the form of a list ([0, 1]) where:
        [0] == key
        [1] == value
        Both key and value default to None when creating empty entries.
        """
        new_els = [[None, None] for entry in range(num)]
        self.map.extend(new_els)

    def hash(self, key):
        """Hash function."""
        return int(key)
    
    def get_index(self, key):
        """Get an index for a certain key value."""
        return self.hash(key) % self.size

    def insert(self, key, val):
        """Insert key, value pair into hash map.
        
        Each hash map element is organized as a list ([0, 1]) where:
        [0] == key
        [1] == value
        """
        index = self.get_index(key)
        self.map[index][0] = key
        self.map[index][1] = val

    def get(self, key):
        """Return hash element with specified key if found.
        
        If element is not found, raise NoHashElement Exception.
        Element returned is in the list form [key, val].
        """
        index = self.get_index(key)
        val = self.map[index][1]
        if val is None:
            raise NoHashElement(key)
        else:
            return self.map[index]

    def remove(self, key):
        """Remove hash element with the specified key.
        
        If found, remove element from hash map and return True.
        Otherwise, return None.
        """
        try:
            el = self.get(key)
            index = self.map.index(el)
            self.map.pop(index)
            return True
        except NoHashElement:
            return None