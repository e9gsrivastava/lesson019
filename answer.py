
"""this is assiagment no to write good and concise code"""


import math

def nested_prime(n):
    """Write a function nested_prime() to generate a list of prime numbers
    upto using only a nested list comprehension"""

    prime = [i for i in range(2, n) if all(bool(i % j) for j in range(2, i))]
    return prime


def old_school_reverse(n):
    """Write a function old_school_reverse() that reverses a string or number without using
    .reverse() or [::-1] slicing and returns any other value passed to the function as is.
    """
    if isinstance(n,int):
        n = str(n)

    my_list = [i for i in n]
    result = [my_list.pop() for _ in range(len(my_list))]
    reversed_n = "".join(result)
    return reversed_n


def dict_a_noodle(data):
    """key:value to value:key"""
    changed_dict = {value: key for key, value in data.items() if isinstance(key, str)}
    unchanged_dict = {
        key: value for key, value in data.items() if not isinstance(key, str)
    }
    changed_dict.update(unchanged_dict)
    return changed_dict


def fib_squares(n):
    """Write a function fib_squares() that returns a list of numbers where each element
    is the number if the number is not a fibonacci number and the square of the number
    if the number is a fibonacci number for a given range of numbers."""

    fibb = [0, 1]
    [fibb.append(fibb[-1] + fibb[-2]) for _ in range(2, n + 1)]
    result = [i**2 if i in fibb else i for i in range(n + 1)]
    return result


def flatten(data):
    """func to flatten the list"""
    if not bool(data):
        return data
    if isinstance(data[0], list):
        return flatten(*data[:1]) + flatten(data[1:])

    return data[:1] + flatten(data[1:])


def dict_of_lists(data):
    """takes a deeply nested list of lists and flattens it out,
    ignores any dict elements, and"""
    result = flatten(data)
    print(result)
    final = {
        i: result.count(i)
        for i in result
        if isinstance(i, (list, str, tuple, set, int))
    }
    return final


def list_of_lists(data):
    """
    takes a deeply nested list of lists and flattens it out,
    ignores any dict elements, and
    returns a sorted list of unique values of the combined list.
    """
    final = dict_of_lists(data)
    result = [i for i in final]

    return result


def dict_from_lists(list1, list2):
    """takes 2 lists
    create a dict such that the keys are elements from the first list and
    the values are elements from the second list
    """

    data = {i: j for i, j in zip(list1, list2)}
    return data


def my_secret(message):
    """write secret msg"""
    my_list = message.split(" ")
    str_message = "".join(my_list)

    length = math.ceil(len(str_message) ** 0.5)

    for i in range(0, len(str_message), length):
        print(str_message[i : i + length])


def phone_words(ph1: str, ph2: str):
    """create words as per numbers"""
    hash_dict = {
        "2": "ABC",
        "3": "DEF",
        "4": "GHI",
        "5": "JKL",
        "6": "MNO",
        "7": "PRS",
        "8": "TUV",
        "9": "WXY",
    }

    def words(phone_number):
        """it creates word"""
        if "0" in phone_number or "1" in phone_number:
            return []
        combinations = [""]
        for digit in phone_number:
            letters = hash_dict[digit]
            new_combinations = []
            for prefix in combinations:
                for letter in letters:
                    new_combinations.append(prefix + letter)
            combinations = new_combinations

        return combinations

    result = {ph1: words(ph1), ph2: words(ph2)}
    return result


def set_complement(*args, verbose=True):
    """find complement"""
    result = []
    for i, list1 in enumerate(args[: len(args) - 1]):
        for list2 in args[i : len(args)]:
            if set(list1) - set(list2):
                result.append(list(set(list1) - set(list2)))
    if verbose:
        all_data = [i for i in args]
        return all_data + result
    return result


def set_intersection(*args, verbose=False):
    """find intersection"""
    result = []
    for i, list1 in enumerate(args[: len(args) - 1]):
        for list2 in args[i + 1 : len(args)]:
            if set(list1) & set(list2):
                result.append(list(set(list1) & set(list2)))

    all_intersection = set(args[0])
    for i, list1 in enumerate(args[1 : len(args)]):
        all_intersection &= set(args[i])

    result.append(list(all_intersection))

    if verbose:
        all_data = [arg for arg in args]
        return all_data + result
    return result


def dict_compare(*args):
    """compare dict"""
    if not args:
        return []

    result = []

    def compare(d1, d2):
        """compares dict"""
        if d1 == d2:
            return True

        if isinstance(d1, dict) and isinstance(d2, dict) and d1.keys() == d2.keys():
            return all(compare(d1[key], d2[key]) for key in d1)

        if isinstance(d1, list) and isinstance(d2, list) and len(d1) == len(d2):
            return all(
                compare(item1, item2) for item1, item2 in zip(sorted(d1), sorted(d2))
            )

        return False

    def identical_combinations(args, current_combination):
        """finds identical combinatins"""
        if all(
            compare(args[i], args[j])
            for i in range(len(args))
            for j in range(i + 1, len(args))
        ):
            result.append(current_combination.copy())

        for i, arg in enumerate(args):
            if i not in current_combination:
                current_combination.append(i)
                identical_combinations(args, current_combination)
                current_combination.pop()

    identical_combinations(args, [])

    return result


if __name__ == "__main__":
    print(nested_prime(10))
    print(old_school_reverse("123"))
    print(fib_squares(10))
    print(
        dict_of_lists(
            [
                [
                    [1, 2, 3],
                    [4, [5, 6]],
                    6,
                    [7, 8, 9],
                    [8, [8, 9, "a"], {5: 6}, ["b"], "ab"],
                ],
                [5, 2, 1],
                1,
            ]
        )
    )
    print(dict_a_noodle({"answernum": 23, 1: "ans"}))
    print(dict_from_lists([1, 2, 3], ["a", "b", "c"]))
    print(
        my_secret(
            "If man was meant to stay on the ground god would have given us roots"
        )
    )
    print(phone_words("22", "1"))
    print(
        list_of_lists(
            [
                [
                    [1, 2, 3],
                    [4, [5, 6]],
                    6,
                    [7, 8, 9],
                    [8, [8, 9, "a"], {5: 6}, ["b"], "ab"],
                ],
                [5, 2, 1],
                1,
            ]
        )
    )
    print(set_complement([1, 2, 3, 4], [1, 3], [1, 2, 3]))
    print(set_intersection([1, 2, 3, 4], [1, 3], [1, 2, 3]))

    dict1 = {"a": 1, "b": [2, 3], "c": {"d": 4}}
    dict2 = {"c": {"d": 4}, "b": [2, 3], "a": 1}

    print(dict_compare(dict1, dict2))
