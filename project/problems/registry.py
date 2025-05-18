# problems/registry.py

PROBLEM_REGISTRY = {}

def register_problem(cls):
    PROBLEM_REGISTRY[cls.__name__] = cls
    return cls
