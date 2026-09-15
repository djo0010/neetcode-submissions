class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        if len(s2) < len(s1):
            return False

        s1CharCounts = defaultdict(int)

        for char in s1:
            s1CharCounts[char] += 1
    
        s2SubarrayCharCounts = defaultdict(int)
        subarrayLength = len(s1)

        for j in range(0, subarrayLength):
            s2SubarrayCharCounts[s2[j]] += 1

        filtered_dict1 = {k: v for k, v in s1CharCounts.items() if v != 0}
        filtered_dict2 = {k: v for k, v in s2SubarrayCharCounts.items() if v != 0}
        if filtered_dict1 == filtered_dict2:
            return True

        print(s2SubarrayCharCounts)


        for i in range(1, len(s2) - subarrayLength + 1):
            s2SubarrayCharCounts[s2[i - 1]] -= 1
            s2SubarrayCharCounts[s2[i + subarrayLength - 1]] += 1
            filtered_dict1 = {k: v for k, v in s1CharCounts.items() if v != 0}
            filtered_dict2 = {k: v for k, v in s2SubarrayCharCounts.items() if v != 0}
            if filtered_dict1 == filtered_dict2:
                return True
            print(s2SubarrayCharCounts)
        return False
            

            