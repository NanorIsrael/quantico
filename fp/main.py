def is_in(x: str, y: str) -> bool:
    if not x:
        return True
    idx = y.lower().find(x[0].lower())
    if idx == -1:
        return False
    return is_in(x[1:], y[:idx] + y[idx + 1:])


print(is_in("Aaron", "Aron city"))

from random import choices
print(f"{''.join(str(num) for num in choices(range(10), k=3))}")