class TimeMap:

    def __init__(self):
        self.dictt = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictt:
            self.dictt[key] = {}
        if timestamp not in self.dictt[key]:
            self.dictt[key][timestamp] =[]
        self.dictt[key][timestamp].append(value)    

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictt:
            return ""
        seen = 0

        for time in self.dictt[key]:
            if time <= timestamp:
                seen = max(seen,time)
        return "" if seen==0 else self.dictt[key][seen][-1]
        
