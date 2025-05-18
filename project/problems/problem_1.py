# problems/problem_1.py
from problems.registry import register_problem

@register_problem
class Problem1:
    def run(self):
        print("Running Problem 1")