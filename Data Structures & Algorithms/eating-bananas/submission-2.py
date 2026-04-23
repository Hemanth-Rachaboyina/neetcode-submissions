class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We are using Binary Search on the answer (k = eating speed)
        
        # Minimum possible speed is 1 banana/hour
        # Maximum possible speed is max pile (eat whole pile in 1 hour)
        low, high = 1, max(piles)

        # Binary search to find the minimum valid speed
        while low < high:
            mid = (low + high) // 2  # Try a candidate eating speed

            hours = 0  # Total hours needed at this speed

            # Calculate total hours needed to finish all piles at speed = mid
            for pile in piles:
                # Add full divisions
                hours += pile // mid
                
                # If there is a remainder, we need one extra hour
                if pile % mid != 0:
                    hours += 1

                # (Alternative cleaner way you can remember later:)
                # hours += (pile + mid - 1) // mid

            # If we can finish within h hours, try smaller speed
            if hours <= h:
                high = mid
            else:
                # Otherwise, speed is too slow → increase it
                low = mid + 1

        # At the end, low == high → minimum valid speed
        return low