class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Pair each car's position with its speed
        pairs = [(p, s) for p, s in zip(position, speed)]
        
        # Sort cars by position in descending order (closest to target first)
        pairs.sort(reverse=True)

        stack = []  # This will store the "time to reach target" for each fleet

        for p, s in pairs:
            # Calculate time for current car to reach the target
            time = (target - p) / s
            stack.append(time)

            # If the current car catches up to the fleet ahead,
            # it becomes part of that fleet instead of forming a new one
            # So we remove it from stack (merge fleets)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        # Number of fleets = number of distinct times left in stack
        return len(stack)