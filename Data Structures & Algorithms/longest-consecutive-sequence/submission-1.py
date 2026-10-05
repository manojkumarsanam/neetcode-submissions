class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        parent = {}
        size = {}

        # Find with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Union by size
        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return

            # Keep rootA as the larger component
            if size[rootA] < size[rootB]:
                rootA, rootB = rootB, rootA

            parent[rootB] = rootA
            size[rootA] += size[rootB]

        # Create one node for every UNIQUE number
        for num in nums:
            if num not in parent:
                parent[num] = num
                size[num] = 1

        # Connect consecutive numbers
        for num in parent:
            if num - 1 in parent:
                union(num, num - 1)

        return max(size[find(num)] for num in parent)