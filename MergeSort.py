def mergelist(List):
    length = len(List)
    if length >1:
        LeftList = List[:(length//2)] 
        RightList = List[(length//2):]
        mergelist(LeftList)
        mergelist(RightList)
        i = 0;j = 0;k = 0
        #Add smaller number to the begining of the list 
        while i < len(LeftList) and j < len(RightList):
            if LeftList[i] < RightList[j]:
                List[k] = LeftList[i]
                i += 1
                #k += 1
                print('branch 1 ijk' ,i,j,k,List)
            else:
                #print('branch 2.1 ijk,LeftList,,RightList' ,i,j,k,List,LeftList,RightList)
                List[k] = RightList[j]
                #k += 1 
                j += 1
                print('branch 2 ijk{}{}{},,,,,{}' ,i,j,k,List)
            k += 1
        #Add the remaining number of Left List to the list.
        while i < len(LeftList):
            #print('Here RightList:{}|LeftList:{}|i:{}|j:{}|k:{}|List:{}'.format(RightList, LeftList, i,j,k,List))
            List[k] = LeftList[i]
            #print('There ')
            k += 1
            i += 1
            print('branch 3 ijk,' ,i,j,k,List)
        #Add the remaining number of Right List to the list.
        while j < len(RightList):
            List[k] = RightList[j]
            k += 1
            j += 1
            print('branch 4 ijk,,,List' ,i,j,k,List)
        return List
    return List


a = [1,2,3,4]
print(mergelist(a))
