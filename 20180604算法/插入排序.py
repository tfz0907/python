def insert_sort(args_list):
    args_list_len=len(args_list)
    for i in range(1,args_list_len):
        for j in range(i,0,-1):
            if args_list[j]<args_list[j-1]:
                args_list[j],args_list[j-1]=args_list[j-1],args_list[j]
            else:
                break
if __name__ == '__main__':
    mylist=[12,34,22,15,53,32]
    print("原列表为：{}".format(mylist))
    insert_sort(mylist)
    print("新列表为：{}".format(mylist))
