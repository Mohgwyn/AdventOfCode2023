import re


def main(input):
    digit_pattern = re.compile(r"\d")
    for line in input.splitlines():
        matches = digit_pattern.findall(line)
        print(f"El codigo es {matches[0]}{matches[-1]}")


if __name__ == "__main__":
    input = """1ab32c3
    uah2ihcu7gau
    178h67huvya23wdw"""
    main(input)