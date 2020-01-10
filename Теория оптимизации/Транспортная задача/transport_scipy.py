from scipy.optimize import linprog as lin
import time as t


class TransportTask:
    def __init__(self):
        # Стоимость доставки
        self.x = [1, 4, 9, 1, 7, 3, 8, 5, 1, 6, 1, 7, 9, 5, 6, 9, 5, 3, 8, 4, 7, 8, 3, 3, 5]
        self.quantityStock = [60, 42, 40, 39, 55]
        self.quantityOrdered = [20, 28, 32, 16, 10]

        self.a_ub = [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]]

        self.a_eq = [[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                     [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]]

    def taskOptimization(self):
        self.start = t.time()  # Время начала выполнения
        print(lin(self.x, self.a_ub, self.quantityStock, self.a_eq, self.quantityOrdered))  # Результат
        self.stop = t.time()  # Время завершения выполнения
        print("Время выполнения:")
        print(self.stop - self.start)


# Создаем экземпляр класса TransportTask
transportTask = TransportTask()
transportTask.taskOptimization()