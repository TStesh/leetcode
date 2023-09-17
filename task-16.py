def threeSumClosest(nums: [int], target: int) -> int:
    nl = len(nums)
    if nl == 3:
        return sum(nums)
    sort_nums = sorted(nums)
    t, diff = 0, 15000
    for i in range(nl - 2):
        a = sort_nums[i]
        for j in range(i + 1, nl - 1):
            b = sort_nums[j]
            for k in range(j + 1, nl):
                c = sort_nums[k]
                new_t = a + b + c
                new_diff = abs(abs(target) - abs(new_t))
                print(a, b, c, new_t, new_diff, t, diff)
                if diff > new_diff:
                    t, diff = new_t, new_diff
    return t

assert (threeSumClosest([-1, 2, 1, -4], 1) == 2)
assert (threeSumClosest([0, 0, 0], 1) == 0)
