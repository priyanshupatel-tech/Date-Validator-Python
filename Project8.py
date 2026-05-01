class Solution:
    def isValidDate(self, d, m, y):
        # code here 
        if y>1800 and y<9999:
            if (y%400==0) or (y%4==0 and y%100!=0):
                if m==2:
                    if d>0 and d<30:
                        return 1
                    else:
                        return 0
                else:
                    if m==4 or m==6 or m==9 or m==11:
                        if d>0 and d<31:
                            return 1
                        else:
                            return 0
                    elif m>0 and m<13:
                        if d>0 and d<32:
                            return 1
                        else:
                            return 0
                    else:
                        return 0
            else:
                if m==4 or m==6 or m==9 or m==11:
                    if d>0 and d<31:
                        return 1
                    else:
                        return 0
                elif m==2:
                    if d>0 and d<29:
                        return 1
                    else:
                        return 0
                elif m>0 and m<13:
                    if d>0 and d<32:
                        return 1
                    else:
                        return 0
                else:
                    return 0
                    
        else:
            return 0
a=Solution()
print(a.isValidDate(3,4,2008))
