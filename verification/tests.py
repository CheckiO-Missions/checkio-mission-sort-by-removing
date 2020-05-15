"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[3, 5, 2, 6]],
            "answer": [3, 5, 6],
        },
        {
            "input": [[7, 6, 5, 4, 3, 2, 1]],
            "answer": [7],
        },
        {
            "input": [[3, 3, 3, 3]],
            "answer": [3, 3, 3, 3],
        },
        {
            "input": [[5, 6, 7, 0, 7, 0, 10]],
            "answer": [5, 6, 7, 7, 10],
        },
        {
            "input": [[1, 5, 2, 3, 4, 7, 8]],
            "answer": [1, 5, 7, 8],
        },
        {
            "input": [[1, 7, 2, 3, 4, 5]],
            "answer": [1, 7],
        },
        {
            "input": [[]],
            "answer": [],
        },
    ],
    "Extra": [
        {
            "input": [[6, 7, 8,10, 8, 8]],
            "answer": [6, 7, 8, 10],
        },
        {
            "input": [[10, 0, 0]],
            "answer": [10],
        },
    ]
}
