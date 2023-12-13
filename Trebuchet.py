import re


def main(input):
    digit_pattern = re.compile(r"\d")
    sum = 0

    for line in input:
        matches = digit_pattern.findall(line)
        #print(f"El codigo es {matches[0]}{matches[-1]}")
        sum += int(matches[0] + matches[-1])

    print(sum)


if __name__ == "__main__":
    with open("input_1.txt") as f:
        input = f.readlines()
    main(input)