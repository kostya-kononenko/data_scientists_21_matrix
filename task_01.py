import numpy as np

class SomeMatrixError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        return f"Заборонена операція: {self.message}"

class MyCustomMatrix:
    def __init__(self, lst):
        self.lst = lst
        self.A = np.array(lst)

    def mult_number(self, num):
        return self.A * num

    def mult_matrix(self, col):
        try:
            if len(self.A[0]) == len(col.A):
                D = self.A.dot(col.A)
                return D
            else:
                raise SomeMatrixError("Кількість стовпчиків однієї "
                                      "матриці не дорівнює кількості "
                                      "рядків іншої матриці")
        except Exception as ex:
            return ex

    def transposition(self):
        return self.A.transpose()

    def sum(self, col):
        if len(self.A) < len(col.A):
            delta = len(col.A) - len(self.A)
            list = []
            for i in range(len(self.A[0])):
                list.append(0)
            for i in range(delta):
                self.lst.append(list)
            self.A = np.array(self.lst)
        if len(self.A) > len(col.A):
            delta = len(self.A) - len(col.A)
            list = []
            for i in range(len(col.A[0])):
                list.append(0)
            for i in range(delta):
                col.lst.append(list)
            col.A = np.array(col.lst)
        if len(self.A[0]) < len(col.A[0]):
            delta = len(col.A[0]) - len(self.A[0])
            for j in range(delta):
                for i in self.lst:
                    i.append(0)
            self.A = np.array(self.lst)
        if len(self.A[0]) > len(col.A[0]):
            delta = len(self.A[0]) - len(col.A[0])
            for j in range(delta):
                for i in col.lst:
                    i.append(0)
            col.A = np.array(col.lst)
        D = self.A + col.A
        return D

    def dif(self, col):
        if len(self.A) < len(col.A):
            delta = len(col.A) - len(self.A)
            list = []
            for i in range(len(self.A[0])):
                list.append(0)
            for i in range(delta):
                self.lst.append(list)
            self.A = np.array(self.lst)
        if len(self.A) > len(col.A):
            delta = len(self.A) - len(col.A)
            list = []
            for i in range(len(col.A[0])):
                list.append(0)
            for i in range(delta):
                col.lst.append(list)
            col.A = np.array(B.lst)
        if len(self.A[0]) < len(col.A[0]):
            delta = len(col.A[0]) - len(self.A[0])
            for j in range(delta):
                for i in self.lst:
                    i.append(0)
            self.A = np.array(self.lst)
        if len(self.A[0]) > len(col.A[0]):
            delta = len(self.A[0]) - len(col.A[0])
            for j in range(delta):
                for i in col.lst:
                    i.append(0)
            col.A = np.array(B.lst)
        D = self.A - col.A
        return D
