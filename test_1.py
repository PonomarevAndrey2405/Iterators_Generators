class FlatIterator:

    def __init__(self, list_of_list):
        self._stopped = False
        self._list = list_of_list
        self._i = 0
        self._j = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self._stopped:
            while self._i < len(self._list):
                if self._j < len(self._list[self._i]):
                    item = self._list[self._i][self._j]
                    self._j += 1
                    return item

                self._i += 1
                self._j = 0
            self._stopped = True
        raise StopIteration


def test_1():
    
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
