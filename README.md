# 📘 Day 42: Two Sum – Pair with Given Sum
## 🧩 Problem Statement
You are given an array arr[] of positive integers and an integer target. The task is to determine whether there exist two distinct indices such that the sum of their elements equals the target.

## ✅ Approach
We use a Hash Set to keep track of the elements we’ve seen so far.

## Steps:
1. Initialize an empty set seen.

2. For each element num in the array:

- Compute the complement: complement = target - num.

- If complement is already in the set, return True (we’ve found our pair).

- Otherwise, add num to the set.

3. If no such pair is found, return False.

This approach avoids using nested loops and achieves optimal performance.

## 📊 Complexity Analysis
- Time Complexity: O(n)
We iterate through the array only once.

- Space Complexity: O(n)
In the worst case, we may store all n elements in the set.

## 🧠 Concepts Practiced
- Hashing

- Two-pointer logic

- Space-time tradeoff

- Optimal search techniques

## 📌 Tags
#TwoSum #Hashing #Array #DSA #ProblemSolving #InterviewPrep
