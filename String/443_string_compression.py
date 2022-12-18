class Solution:
    def compress(self, chars) -> int:
        
        left, index = 0, 0
        
        while index < len(chars):
		
            chars[left] = chars[index]
            count = 1
			
            while index < len(chars) - 1 and chars[index] == chars[index + 1]:
                index += 1
                count += 1
			
            if count > 1:
                for char in str(count):
                    left += 1
                    chars[left] = char
            
            index += 1
            left += 1
        
        return left
if __name__ =='__main__':
    chars = ["a","a","b","b",'b','b',"c","c","c"]
    ob = Solution()
    ans = ob.compress(chars)
    print(ans)
