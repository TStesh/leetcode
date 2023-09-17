from Other.SpecFunctions import binary_search

def three_sum(nums: [int]) -> [[int]]:
	nl = len(nums)
	if nl < 3:
		return []
	if nums[0] == 0 and nums[1] == 0 and [0] * len(nums) == nums:
		return [[0, 0, 0]]
	sort_nums = sorted(nums)
	d, t = {}, {}
	if sort_nums[0] > 0 or sort_nums[-1] < 0:
		return []
	res = []
	for i, a in enumerate(sort_nums):
		if a > 0:
			break
		if a in d:
			continue
		else:
			d[a] = 1
		for j in range(i + 1, nl - 1):
			b = sort_nums[j]
			if (a, b) in t:
				continue
			ab = a + b
			if ab < 0 and -ab > sort_nums[-1]:
				continue
			if binary_search(sort_nums, -ab, lo=j + 1, hi=nl):
				res.append([a, b, -ab])
				t[(a, b)] = 1
	return res


assert (three_sum([0, 1, 1]) == [])
assert (three_sum([0, 0, 0]) == [[0, 0, 0]])

print(three_sum([-1, 0, 1, 0]))
