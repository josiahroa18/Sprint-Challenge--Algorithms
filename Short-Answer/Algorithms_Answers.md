#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) n * n * n = 3n and when analyzing the time complexity of an algorithm, we can drop the constant which means we can look at 3n as n. Also, since we are multipling a by 2n, we can look at 3n/2n as n. This implies that the runtime for worst case scenario as the input n increases is - O(n).


b) Since we are multiplying j by 2, the amount of times the inner loop runs is n / 2. The outer loop runs at O(n). This implies that our algorithm's worst case scenario will be - O(nlog(n)).


c) For each input, there is a recusrive call. This makes the time complexity - O(n).

## Exercise II
We can start dropping eggs from the middle floor. If it breaks, then we want to go lower, if it doesn't break, we can go higher. We keep repeating this process until we reach the two floors where the egg breaks and the egg does not break.

start = 0
end = n
middle = (start + end) // 2

If the egg breaks, we need to go lower
start = 0
end = middle - 1
middle = (start + end) // 2

If the egg does not break, we can go higher
start = middle + 1
end = n
middle = (start + end) // 2

Repeat this process until an egg doesn't break at floor(middle) and floor(middle + 1) does break

This algorithm will run in O(log(n)) time because we are dividing the input by two on each iteration.

====== Psuedo Code ======
current_floor = False (if it does not break, set to true)
next_floor = False (if it breaks, set to true)
optimal_floor = None
start = 0
end = n (n represents number of floors)
while not current_floor and not next_floor:
    middle = (start + end) // 2
    if middle does not break egg and middle + 1 breaks egg:
        current_floor = True
        next_floor = True
        optimal_floor = middle
    elif middle does break:
        end = middle - 1
    else:
        start = middle + 1
return optimal_floor




