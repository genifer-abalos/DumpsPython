
from dataclasses import dataclass, field

@dataclass
class C:
    a: int
    b: int
    c: float = field(init=False, repr=False)

    def __post_init__(self):
        self.c = self.a + self.b

c = C(1.0, 2.0)
print(c)