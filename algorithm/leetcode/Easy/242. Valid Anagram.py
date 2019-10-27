# leetcode 242. Valid Anagram

class Solution(object):
	def isAnagram(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		for i in map(chr, range(97,123)):
			if s.count(i) != t.count(i):
				return False
		return True


s = Solution()
print(s.isAnagram("a1bcb", "acbb1"))
		
		
		
