def count_matching_brackets(text: str) -> int:
    mapping = {')':'(',']':'[','}':'{'}
    open_brackets = set(mapping.values())
    match_count = 0
    stack = []

    print(mapping)

    return match_count


if __name__ == '__main__':
    print(count_matching_brackets("(abc)[123]{}"))
