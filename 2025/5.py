class Range:
    """An inclusive range of two numbers"""

    def __init__(self, low: int, high: int):
        self.low = low
        self.high = high

    # Is the given number contained within this range?
    def contains(self, num: int):
        return num >= self.low and num <= self.high

    # Does this range overlap with the other range?
    def overlaps(self, other):
        return (
            self.contains(other.low)
            or self.contains(other.high)
            or other.contains(self.low)
            or other.contains(self.high)
        )


# Is the given number included in the list of fresh ranges?
def is_fresh(ranges: list[Range], item_num: int):
    for range in ranges:
        if range.contains(item_num):
            return True

    return False


# Insert the given new range into the list of existing ranges, either by
# merging it with an existing overlapping range, or by adding it at the end
def insert_range_smart(ranges: list[Range], new_range: Range):
    for range in ranges:
        if range.overlaps(new_range):
            new_range = Range(
                min(range.low, new_range.low), max(range.high, new_range.high)
            )
            ranges.remove(range)
            return insert_range_smart(ranges, new_range)

    ranges.append(new_range)
    return ranges


def solution(ranges: list[Range], item_nums: list[int] = [], is_part_2: bool = False):
    if is_part_2:
        return sum([(range.high - range.low + 1) for range in ranges])

    num_fresh = 0
    for item_num in item_nums:
        if is_fresh(ranges, item_num):
            num_fresh += 1

    return num_fresh


with open("2025/inputs/5.txt") as inpt:
    ranges = []
    item_nums = []
    reading_items = False
    for line in inpt:
        if line == "\n":
            reading_items = True
            continue
        if reading_items:
            item_nums.append(int(line))
        else:
            low, high = line.split("-")
            ranges = insert_range_smart(ranges, Range(int(low), int(high)))

    print("Solution for part 1: ", solution(ranges, item_nums))
    print("Solution for part 2: ", solution(ranges, is_part_2=True))
