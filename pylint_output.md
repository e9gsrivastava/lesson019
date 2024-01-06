(venv) fox@enine014:~/Day19/lesson019$ pylint answer.py 
************* Module answer
answer.py:22:14: R1721: Unnecessary use of a comprehension, use list(n) instead. (unnecessary-comprehension)
answer.py:44:4: W0106: Expression "[fibb.append(fibb[-1] + fibb[-2]) for _ in range(2, n + 1)]" is assigned to nothing (expression-not-assigned)
answer.py:79:13: R1721: Unnecessary use of a comprehension, use list(final) instead. (unnecessary-comprehension)
answer.py:90:11: R1721: Unnecessary use of a comprehension, use dict(zip(list1, list2)) instead. (unnecessary-comprehension)
answer.py:145:19: R1721: Unnecessary use of a comprehension, use list(args) instead. (unnecessary-comprehension)
answer.py:165:19: R1721: Unnecessary use of a comprehension, use list(args) instead. (unnecessary-comprehension)
answer.py:201:15: W0612: Unused variable 'arg' (unused-variable)

------------------------------------------------------------------
Your code has been rated at 9.43/10 (previous run: 9.34/10, +0.08)
