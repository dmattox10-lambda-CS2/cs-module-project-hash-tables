class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.min_capacity = MIN_CAPACITY
        if capacity > self.min_capacity:
            self.capacity = capacity
        else:
            self.capacity = self.min_capacity
        self.data = [None] * self.capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size/self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        hval = 0x811c9dc5
        fnv_32_prime = 0x01000193
        uint32_max = 2 ** 32
        for s in key:
            hval = hval ^ ord(s)
            hval = (hval * fnv_32_prime) % uint32_max
        return hval

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.data[index] == None:
            self.data[index] = HashTableEntry(key, value)
            self.size += 1
        else:
            current = self.data[index]
            while current.next != None and current.key != key:
                current = current.next

            if current.key == key:
                current.value = value
            else:
                new_entry = HashTableEntry(key, value)
                new_entry.next = self.data[index]
                self.data[index] = new_entry
                self.size += 1
        if self.get_load_factor() > .7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.data[index].key == key:
            if self.data[index].next == None:
                self.data[index] = None
                self.size -= 1
            else:
                new_head = self.data[index].next
                self.data[index].next = None
                self.data[index] = new_head
                self.size -= 1
        else:
            if self.data[index] == None:
                return None
            else:
                current = self.data[index]
                prev = None
                while current.next is not None and current.key != key:
                    prev = current
                    current = current.next
                if current.key == key:
                    prev.next = current.next
                    self.size -= 1
                    return current.value
                else:
                    return None

        if self.get_load_factor() < .2:
            if self.capacity/2 > 8:
                self.resize(self.capacity//2)
            elif self.capacity > 8:
                self.resize(8)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.data[index] is not None and self.data[index].key == key:
            return self.data[index].value
        elif self.data[index] is None:
            return None
        else:
            current = self.data[index]
            while current.next != None and current.key != key:
                current = self.data[index].next
            if current == None:
                return None
            else:
                return current.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_table = self.data[:]
        self.capacity = new_capacity
        self.data = [None] * new_capacity
        for i in range(len(old_table)):
            if old_table[i] is not None:
                if old_table[i].next is not None:
                    current = old_table[i]
                    while current.next is not None:
                        self.put(current.key, current.value)
                        current = current.next
                    self.put(current.key, current.value)
                else:
                    self.put(old_table[i].key, old_table[i].value)


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
