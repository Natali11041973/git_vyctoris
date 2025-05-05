import traceback
class Calculator:
    last_res = None
    def sum(self, n1, n2):
        self.last_res = n1 + n2
        return n1 + n2
    def divide(self, n1,n2):
        try:
            res = n1 / n2
            self.last_res = res
            return res
        except:
            traceback.print_exc()
    def min(self, n1, n2):
        self.last_res = n1-n2
        return n1 - n2

    def multiply(self, n1, n2):
        self.last_res = n1 * n2
        return n1 * n2

    def print_last_res(self):
        print(self.last_res)
