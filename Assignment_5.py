#%%
class Link(object):
    def __init__(self, val, nxt) -> None:
        self.val = val
        self.tail = nxt

    def __repr__(self) -> str:
        return f'Link({self.val}, {self.tail})'

def to_list(itr):
    link = None
    for val in reversed(itr):
        link = Link(val, link)
    return link

def min_link(lst):
    current_min = lst
    while lst is not None:
        if lst.val < current_min.val:
            current_min = lst
        lst = lst.tail
    return current_min

def swap_val(link1, link2):
    link1.val, link2.val = link2.val, link1.val

def selection_sort(lst):
    x = lst
    while x is not None:
        smallest = min_link(x)
        swap_val(x, smallest)
        x = x.tail
    return lst

def swap(link):
    link.val, link.tail.val = link.tail.val, link.val
#%%
'''
Exercise: Can you also implement selection sort for a persistent linked list structure, 
i.e., one where you do not modify the existing list but create a new one? What is the running time?

Answer:
In order to construct a sorted copy, we could iteratively run through the list, to find the largest element, and prepend it to the new list
In that case there are n elements to sort, it takes O(n) to find each element, 
and we would have to do it n times which would result in a worst case running time in O(n^2).
'''

def bubber_sort(liste:Link)->Link:
    led = liste
    while led.tail is not None:
        if led.val > led.tail.val:
            while led.tail is not None:
                swap(led)
                led = led.tail
            led = liste
        else:
            led = led.tail
    return liste

test = Link(3, Link(2, Link(4, Link(1, Link(2, None)))))
repr(test)

# %%
repr(bubber_sort(test))
# %%

'''
Exercise: Implement a function that moves a value forward in the list by swapping values between two neighbouring links.
It will serve as the inner loop in insertion sort.
'''
class DLink(object):
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next
    
    def __str__(self) -> str:
        x = []
        link = self
        while link:
            x.append(link.val)
            link = link.next
        return str(x)

def to_list(itr):
    link = None
    for val in reversed(itr):
        link = DLink(val, None, link)
        if link.next is not None:
            link.next.prev = link
    return link

def insertion_sort(x):
    link = x
    while link is not None:
        print(x)
        swap_down(link)
        link = link.next
    return x

''' Swap down implementation:'''
def swap_down(x:DLink):
    # Move the value in x forward in the lislt
    # until it finds a value smaller than itself
    while x.prev and x.val <= x.prev.val:
        x.val ,x.prev.val = x.prev.val, x.val
        x = x.prev

''' Testing'''
#%%
o = [3, 2, 4, 1, 2]
test = to_list(o)
print(test)
# %%
insertion_sort(test)
print(test)
# %%
''' Swapping cells.'''
class Link(object):
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next



class List(object):
    def __init__(self, x):
        self.dummy = Link(None, None, None)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

        for val in reversed(x):
            new_link = Link(val, self.dummy, self.dummy.next)
            new_link.prev.next = new_link
            new_link.next.prev = new_link
    
    def __str__(self) -> str:
        x = []
        if self.dummy.next:
            link = self.dummy.next
        else: 
            link = self.dummy
        while link is not self.dummy:
            x.append(link.val)
            link = link.next
        return str(x)

'''
Exercise: Write a function that swaps a link and its successor in a linked list, not the values, they should remain the same,
but the order the links have in the list.

Implementation:
'''
def swap_link(link:Link):
    #l1 , l2 = link, link.next
    #l1.next, l2.next = l2.next, l1.next
    
    link.next, link.next.next.prev, link.prev, link.prev.next, link.next.prev, link.next.next =\
        link.next.next, link.next.prev, link.next, link.next, link.prev, link.next.prev
    return
	# Implement this
''' we tried using the above implementation, but couldn't get it to work, and we're unsure why. We think it might be a problem with the 
__str__ method, but since we can't figure out what goes wrong we cant verify if it works.'''


'''Testing:'''
#%%
x = List([1, 2, 5, 2, 5, 9, 3])
# %%
print(x)
swap_link(x.dummy.next.next.next)
print(x)
# %%

'''
Exercise: Update your implementation of insertion sort to use link-swapping instead of value-swapping.

Updated swap down implementation if we had a working swap_link:
'''
#%%
def swap_down(x:DLink):
    # Move the value in x forward in the lislt
    # until it finds a value smaller than itself
    while x.prev.val and x.val <= x.prev.val:
        swap_link(x.prev) #since our implementation swaps a link with its next, we have to call it on the previous to x
        x = x.prev