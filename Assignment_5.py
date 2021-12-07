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

test = Link(2, Link(3, Link(4, Link(1, Link(2, None)))))
repr(test)

# %%
repr(bubber_sort(test))
# %%
class Link(object):
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

def to_list(itr):
    link = None
    for val in reversed(itr):
        link = Link(val, None, link)
        if link.next is not None:
            link.next.prev = link
    return link