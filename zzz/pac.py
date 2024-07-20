class Pac:
    """
    Represents a Pac object that stores a key and a list of values.
    """

    def __init__(self, key):
        """
        Initialize a Pac object with a key and an empty list of values.

        :param key: The key associated with the Pac object.
        """
        self.key = key
        self.values = []

    def push(self, element):
        """
        Add an element to the list of values.

        :param element: The element to be added to the values list.
        """
        self.values.append(element)

    def pac(self):
        """
        Return a list containing the key followed by the list of values.

        :return: A list containing the key and all values stored.
        """
        return [self.key] + self.values
