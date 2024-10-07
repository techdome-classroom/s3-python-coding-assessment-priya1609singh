class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
       roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
  
        total = 0
        
     
        for i in range(len(s)):
           
            current_val = roman_map[s[i]]
            
           
            if i + 1 < len(s) and current_val < roman_map[s[i + 1]]:
                total -= current_val
            else:
                # Otherwise, add it
                total += current_val
                
        return total




