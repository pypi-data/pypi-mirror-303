class rangef:
    def __init__(self, start, stop=None, step=1.0):
        if stop is None:
            self.start = 0.0
            self.stop = start
            self.step = step
        else:
            self.start = start
            self.stop = stop
            self.step = step

        self.current = self.start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.stop is None:
            if self.current > float('inf'):
                raise StopIteration
            next_value = self.current
            self.current += self.step
            return next_value
        else:
            if self.current >= self.stop:
                raise StopIteration
            next_value = self.current
            self.current += self.step
            return next_value

    def __str__(self):
        return f"rangef({self.start}, {self.stop}, {self.step})"

    def __repr__(self):
        return f"rangef({self.start}, {self.stop}, {self.step})"

    def __len__(self):
        return int((self.stop - self.start) / self.step)


def find_closest(tar: float | int, enums: list[float | int]) -> tuple[int, float | int | None]:
    if not enums:  # 检查列表是否为空
        return (-1, None)  # 如果列表为空，返回(-1, None)

    min_diff = float('inf')
    closest_index = -1
    closest_value = None

    for index, value in enumerate(enums):
        diff = abs(value - tar)
        if diff < min_diff:
            min_diff = diff
            closest_index = index
            closest_value = value

    return (closest_index, closest_value)


