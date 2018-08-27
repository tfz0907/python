def select_sort(args_list):
    args_list_len = len(args_list)

    for i in range(0,args_list_len-1):
        min_index = i
        for j in range(i+1, args_list_len):
            if args_list[min_index] > args_list[j]:
                min_index = j
            if i!=min_index:
                args_list[min_index],args_list[i]=args_list[i],args_list[min_index]

if __name__ == '__main__':
   mylist = [234,12,45,13,44,33]
   print("原列表为：{}".format(mylist))
   select_sort(mylist)
   print("新列表为：{}".format(mylist))