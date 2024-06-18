from typing import List


class CusotmerPiplineComponent:
    steps: List["CustomerRunnable"]

    def __init__(self, *steps):
        self.steps = steps

    def __or__(self, other: "CusotmerPiplineComponent"):
        return CusotmerPiplineComponent(
            *self.steps, other
        )

    def __ror__(self, other: "CusotmerPiplineComponent"):
        print(other)

    def __str__(self):
        return ",".join(map(lambda item: item.name, self.steps))

    def invoke(self,**kwargs):
        print("kwargs:", kwargs)
        for item in self.steps:
            print(item.name)


class CustomerRunnable:
    name: str

    def __init__(self, name: str):
        self.name = name

    def __or__(self, other: "CustomerRunnable"):
        # print(self.name,",",other.name)
        return CusotmerPiplineComponent(
            self, other
        )

    def __ror__(self, other: "CustomerRunnable"):
        if not other:
            return
        # print(self.name,"+",other.name)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    res = CustomerRunnable("a") | CustomerRunnable("b") | CustomerRunnable("c")
    res.invoke(**{"input":12})