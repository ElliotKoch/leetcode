class RecentCounter:

    def __init__(self):
        self.requests = []
        self.index = -1
        

    def ping(self, t: int) -> int:

        # Initialize the counter for the recent requests
        past_requests = 0
        
        # Count the number of requests that are in the interval [t - 3000, t]
        self.requests.append(t)
        for i in range(self.index+1,len(self.requests)):
            if self.requests[i] >= t-3000 and self.requests[i] <= t:
                past_requests += 1
            else:
                # Remember the index of the "old" requests to bybass them at the next call of ping
                self.index = i

        return past_requests
