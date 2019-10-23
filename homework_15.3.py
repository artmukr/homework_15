# Add a new method to our Worker-Boss program to the Boss class.
# This method is called (dump_workers). It must take all workers from
# workers list and output them into a .csv file (just the way we did it)
#
# Extra point for doing it using built-in csv library
# Extra point for doing it using 3rd party library pandas


from abc import ABC


class Person(ABC):
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company


class Boss(Person):
    def __init__(self, id_: int, name: str, company: str):
        super().__init__(id_, name, company)
        self.workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.workers.append(worker)

    def remove_worker(self, worker):
        self.workers.remove(worker)

    def dump_workers(self):
        with open("homework_directory/worker`s_list.csv", "w") as file:
            for obj in self.workers:
                file.write(f'{obj.name},{obj.company}\n')

    def __repr__(self):
        return f"{self.name} is a boss of {self.workers}"


class Worker(Person):
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        super().__init__(id_, name, company)
        self._boss = boss
        boss.add_worker(self)

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, boss):
        if isinstance(boss, Boss):
            self._boss.workers.remove(self)
            self._boss = boss
            self._boss.workers.append(self)

    def __repr__(self):
        return f'{self.name} is worker'


b1 = Boss(654, "Kevin", "Ford")
w1 = Worker(579, "Luke", "Ford", b1)
w2 = Worker(579, "Frank", "Ford", b1)
w3 = Worker(579, "Will", "Ford", b1)

b1.dump_workers()

