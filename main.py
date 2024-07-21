# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
immutable_var=([11,15],1000)
tuple_=immutable_var
print(tuple_)
tuple_[0][1]=12
print(tuple_[0][1])
tuple_=([11,15],1000),+(10)
print(tuple_)
tuple_=(([11,15],1000),+(10))*2
print(tuple_)
print(type(immutable_var))
mutable_list=['window','door','44']
mutable_list[0]='table'
print(mutable_list)

