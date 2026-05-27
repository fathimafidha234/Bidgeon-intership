def merge_and_sort_names(list1,list2):
    return sorted(list(set(list1+list2)))
list_a=["Abhi","Chinnu","Sara","Dani"]
list_b=["Eiza","Sara","Abhi","Fidha"]
result=merge_and_sort_names(list_a,list_b)
print(result)
