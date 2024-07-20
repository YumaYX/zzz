class Pac:
    """
    A class to represent a block of text with a key and associated values.

    Attributes:
        key (str): The key or heading of the block.
        values (list): A list of values or lines associated with the key.
    """

    def __init__(self, key):
        """
        Initializes a new instance of the Pac class.

        Args:
            key (str): The key or heading of the block.
        """
        self.key = key
        self.values = []

    def push(self, element):
        """
        Adds a new element to the block's values.

        Args:
            element (str): The element to add to the values list.
        """
        self.values.append(element)

    def pac(self):
        """
        Returns the block's key and values as a list.

        Returns:
            list: A list containing the key followed by the values.
        """
        return [self.key] + self.values
