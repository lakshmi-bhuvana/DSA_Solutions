class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their corresponding opening brackets
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for char in s:
            # If it is a closing bracket
            if char in bracket_map:
                # Pop the top element if stack isn't empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the mapping matches
                if bracket_map[char] != top_element:
                    return False
            else:
                # It is an opening bracket, push to stack
                stack.append(char)
                
        # If the stack is empty, all brackets were matched correctly
        return not stack
