"""  Create a new list from two list using the following condition """

""" Tạo một danh sách mới từ hai danh sách bằng cách sử dụng điều kiện sau
Cho hai danh sách số, hãy viết chương trình tạo một danh sách mới sao cho danh sách mới phải 
chứa các số lẻ từ danh sách đầu tiên và các số chẵn từ danh sách thứ hai. """

def merge_lists(list1, list2):
    result_list = []
    for num in list1:
        if num % 2 != 0:
            result_list.append(num)
    for num in list2:
        if num % 2 == 0:
            result_list.append(num)
    return result_list

list1 = [1, 2, 3, 4, 5]
list2 = [10,20,33,56,67]
merge_lists(list1, list2)
print(" given list :", merge_lists(list1, list2))