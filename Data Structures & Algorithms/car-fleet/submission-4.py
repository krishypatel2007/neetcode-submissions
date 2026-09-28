class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # idea is to get pos and speed to a pairs, sort by pos, then go through all pos in descending order, work out speed, if <= to last on stack, this will create same fleet so ignore, else add to stack ie new fleet
        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse = True)
        stack = []
        for p,s in pair:
            # add time
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        