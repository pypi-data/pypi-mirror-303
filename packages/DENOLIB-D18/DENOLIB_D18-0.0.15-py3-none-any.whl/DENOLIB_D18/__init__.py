import os
from math import *
os.system('cls' if os.name == 'nt' else 'clear')
class function():
    def GiaiThua(n):
        if(n ==0 or n==1):
            return 1
        return n*function.GiaiThua(n-1)
    def SNT(n):
        if(n<2):
            return 0
        for i in range(2,int(n/2)+1):
            if n%i==0:
                return 0
        return 1
    def UCLN(a,b):
        return gcd(a,b)
    def BCNN(a,b):
        return lcm(a,b)
    def FIB(n):
        if(n==0 or n==1):
            return 1
        return function.FIB(n-1)+function.FIB(n-2)
class LIST():
    def TBC(a):
        sum1 = 0
        count1 = 0
        for i in range(len(a)):
            if(a[i]>0):
                sum1+=a[i]
                count1+=1
        return float(sum1/count1)
    def SXTANG(a):
        a.sort()
        return a
    def vitriamdautien(a):
        temp = 0
        for i in range(len(a)):
            if(a[i]<0):
                temp = a[i]
                break
        return temp
    def maxvavitri(a):
        temp = 0
        for i in range(len(a)):
            if(a[i]==max(a)):
                temp = i
        return max(a),temp
    def SNT(a):
        b = []
        for i in range(0,len(a)):
            # if(a[i]<2):
            #     return 0
            if(function.SNT(a[i])):
               b.append(a[i])
        return b
    def soduonglientiep(a):
        count1 = 0
        maxcount = 0
        for i in range(len(a)):
            if a[i]>0:
                count1+=1
                maxcount = max(maxcount,count1)
            else:
                count1 =0 
        return maxcount
    def soluongdandau(a):
        count1 = 0
        maxcount = 0
        for i in range(len(a)):
            if(a[i]*a[i-1]<0):
                count1+=1
                maxcount = max(maxcount,count1)
            else:
                count1 = 1
        return maxcount
    def xoasophantuthuk(a,k):
        for i in range(len(a)):
            if(i==k):
                a.remove(a[i])
        return a
    def chenX(a,X):
        a.append(X)
        a.sort()
        return a
class TUPLE():
    def tachdau(s):
        a = s.split(",")
        return tuple(a)
    def tachnua(t):
        a = list(t)
        d = len(a)
        return(tuple(a[:int(d/2)])),tuple(a[int(d/2):])
    def sochan(t):
        a = list(t)
        b = []
        for i in range(len(a)):
            if a[i] %2 == 0:
                b.append(a[i])
        return tuple(b)
class SET():
    def sxchuoi(s):
        a = s.split(' ')
        b = sorted(set(a))
        return b
    def loaibokitutrunglap(s):
        return set(s)
    def xaucondainhat(s):
        maxxau = ""
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                xaucon = s[i:j]
                if(len(xaucon)==len(set(xaucon)) and len(xaucon)>len(maxxau)):
                    maxxau = xaucon
        return maxxau
class DICT():
    def THONGKEDIEM(d):
        count = {}
        for i  in range(11):
            count[11-i-1] = 0
        for diem in d.values():
            count[diem] +=1
        return count
class STRING():
    def invadaonguoc(s):
        return s[::-1]
    def demxaucon(s,s1):
        count = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if(s1==s[i:j]):
                    count+=1
        return count
    def demchuhoavathuong(s):
        lower = 0
        upper = 0
        for a in s:
            if(a.islower()):
                lower+=1
            elif(a.isupper()):
                upper+=1
        return upper,lower
    def SXkitu(s):
        a = ""
        for i in sorted(s):
            a+=i
        return a
    def xaucon(s):
        a = []
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                a.append(s[i:j])
        return a
    def ketthucbangxaucon(s,s1):
        for i in range(len(s)):
            if(s[i:len(s)]==s1):
                return True
        else:
            return False
    def kituxuathienitnhat(s):
        d = {}
        a = []
        for i in s:
            c = s.count(i)
            d[i]=c
        min1 = min(d.values())
        for key,values in d.items():
            if(values==min1):
                a.append(key)
        return a
    def batdaubangxaucon(s,s1):
        for i in range(1,len(s)+1):
            print(s[0:i])
            if(s[0:i]==s1):
                return True
        else:
            return False
    def kituxuathiennhieunhat(s):
        d = {}
        a = []
        for i in s:
            c = s.count(i)
            d[i]=c
        max1 = max(d.values())
        for key,values in d.items():
            if(values==max1):
                a.append(key)
        return a