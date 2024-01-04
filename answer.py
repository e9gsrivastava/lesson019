'''this is assiagment no to write good and concise code'''

def nested_prime(n):
    '''Write a function nested_prime() to generate a list of prime numbers
    upto using only a nested list comprehension'''
    
    prime=[i for i in range(2,n) if all(bool(i%j) for j in range(2,i) )]
    return prime



def old_school_reverse(n):
    '''Write a function old_school_reverse() that reverses a string or number without using 
    .reverse() or [::-1] slicing and returns any other value passed to the function as is.'''
    if type(n)==int:
        n=str(n)

    My_list=[i for i in n]
    result=[My_list.pop() for _ in range(len(My_list))]
    reversed_n=''.join(result)
    return reversed_n

def dict_a_noodle(data):
    
    data= {value:key   for key, value in data.items() if isinstance(key, str)  }
    # noodle_dictt = {value: key  for key, value in data.items() if not isinstance(key, str)}
    # noodle_dict.update(noodle_dictt)
    # return noodle_dict
    return data


def fib_squares(n):
    '''Write a function fib_squares() that returns a list of numbers where each element
    is the number if the number is not a fibonacci number and the square of the number
    if the number is a fibonacci number for a given range of numbers.'''

    fibb=[0,1]
    [fibb.append(fibb[-1]+fibb[-2]) for _ in range(2,n+1)]
    result=[i**2 if i in fibb  else i  for i in range(n+1)]
    return result

def flatten(data):
    '''func to flatten the list'''
    if not(bool(data)):
            return data
    if isinstance(data[0], list):
            return flatten(*data[:1]) + flatten(data[1:])
    
    return data[:1] + flatten(data[1:])



def dict_of_lists(data):
    result= flatten(data)
    final=[i for i in result if isinstance(i,(list,str,tuple,set,int))]
    return final        

# def set_complement(*args, verbose=False):

if __name__=='__main__':
    # print(nested_prime(10))
    # print(old_school_reverse('123'))
    # print(fib_squares(10))
    # print(dict_of_lists([[[1, 2, 3], [4, [5, 6]], 6, [7, 8, 9], [8, [8, 9, "a"], {5: 6}, ["b"], "ab"]], [5, 2, 1], 1]))
    print(dict_a_noodle({'answernum':23,1:'ans'}))
