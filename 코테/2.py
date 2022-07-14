

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

class Solution(object):
    def __init__(self):
        # write your code in Python 3.6
        self.items = []
        self.cur_transaction = -1
        self.transaction_block = []

    def push(self, value):
        self.items.append(value)
        if self.cur_transaction > -1:
            self.transaction_block[self.cur_transaction][1] = self.items.copy()

    def top(self):
        if len(self.items) == 0:
            return 0
        else:
            return self.items[-1]

    def pop(self):
        if len(self.items) == 0:
            return
        else:
            self.items.pop()
            if self.cur_transaction > -1:
                self.transaction_block[self.cur_transaction][1] = self.items.copy()


    def begin(self):
        self.cur_transaction += 1
        self.transaction_block.append([self.items.copy(),self.items.copy()])


    def rollback(self):
        if self.cur_transaction > -1:
            self.items = self.transaction_block[-1][0]
            self.transaction_block.pop()
            self.cur_transaction -= 1
            return True
        else:
            return False

    def commit(self):
        if self.cur_transaction > -1:
            self.transaction_block.pop()
            self.cur_transaction -= 1
            return True
        else:
            return False


def test():
    # Define your tests here
    sol = Solution()
    sol.push(42)
    assert sol.top() == 42, "top() should be 42"
