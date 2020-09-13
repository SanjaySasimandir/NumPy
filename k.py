
def longestSubarray(A, N, X):
    maxLen = 0
    beginning = 0
    window = {}
    start = 0
    for end in range(N):
        if A[end] in window:
            window[A[end]] += 1
        else:
            window[A[end]] = 1
        minimum = min(list(window.keys()))
        maximum = max(list(window.keys()))
        if maximum - minimum <= X:
            if maxLen < end - start + 1:
                maxLen = end - start + 1
                beginning = start

        else:
            while start < end:

                window[A[start]] -= 1

                if window[A[start]] == 0:
                    window.pop(A[start])

                start += 1

                minimum = min(list(window.keys()))
                maximum = max(list(window.keys()))

                if maximum - minimum <= X:
                    break

    for i in range(beginning, beginning + maxLen):
        print(A[i], end=' ')


arr = [15, 10, 1, 2, 4, 7, 2]
X = 5
n = len(arr)
longestSubarray(arr, n, X)
