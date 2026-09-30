def binary_search(data: str, lookup: str) -> None:
    print(f"Searching for {lookup} in {data}")
    print("-------------------------------------------")
    lower: int = 0
    upper: int = len(data)
    is_found: bool = False

    while lower < upper:
        mid: int = (lower + upper) // 2
        mid_str: str = data[mid]

        if mid_str > lookup:
            upper = mid
        elif mid_str < lookup:
            lower = mid + 1
        else:
            print(f"Found {lookup} at Index {mid}")
            is_found = True
            break  

    if not is_found:
        print(f"{lookup} not found in {data}")




if __name__ == '__main__':
    sample_string = "abcdefghijklmnopqrstuvwxyz"
    search_string = "z"
    binary_search(sample_string, search_string)
