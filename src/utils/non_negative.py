def non_negative(x: int, label: str = "Value") -> int:
    if x < 0:
        raise ValueError(f"{label.title()} must be positive")
    return x


if __name__ == "__main__":
    print(non_negative(1))

    try:
        print(non_negative(-1))
    except ValueError as e:
        print(e)
