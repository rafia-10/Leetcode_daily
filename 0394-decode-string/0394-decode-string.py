class Solution:
    def decodeString(self, s: str) -> str:
        # We need a helper function because the main decodeString
        # doesn't need to return the index. The helper will.
        # Initialize our pointer
        self.ptr = 0
        return self._decode(s)

    def _decode(self, s: str) -> str:
        current_string_segment = [] # Stores characters and decoded substrings
        current_num = 0             # Stores the repetition count

        while self.ptr < len(s):
            char = s[self.ptr]

            if '0' <= char <= '9':
                # Build the number (e.g., '1' then '2' becomes 12)
                current_num = current_num * 10 + int(char)
                self.ptr += 1
            elif char == '[':
                # This is where recursion kicks in.
                # We've found a new subproblem.
                self.ptr += 1 # Move past the '['
                decoded_inner_string = self._decode(s) # RECURSIVE CALL!
                
                # After the recursive call returns, we've decoded the
                # string inside the brackets. Now, append it `current_num` times.
                current_string_segment.append(decoded_inner_string * current_num)
                
                # Reset current_num for the next segment
                current_num = 0
            elif char == ']':
                # We've completed a segment enclosed by brackets.
                # Time to return to the previous recursive call.
                self.ptr += 1 # Move past the ']'
                return "".join(current_string_segment)
            else:
                # It's a letter. Just append it.
                current_string_segment.append(char)
                self.ptr += 1
        
        # If we reach here, it means we've processed the entire string
        # (or the current top-level segment).
        return "".join(current_string_segment)