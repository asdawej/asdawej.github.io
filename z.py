from math import gcd

D={0:'零', 1:'一', 2:'二', 3:'三', 4:'四', 5:'五', 6:'六', 7:'七', 8:'八', 9:'九'}

def hanzishuzi(s: int) -> str:
    '将数字转化为汉字'
    return ''.join([D[int(x)] for x in str(s)])

class Daifenshu(object):
    '《九章算术》使用带分数运算, 定义带分数类'

    def __init__(self, zhengshu: int, fenzi: int, fenmu: int):
        if fenmu==0:
            raise ZeroDivisionError
        
        self.zhengshu=zhengshu
        self.fenzi=fenzi
        self.fenmu=fenmu
    
    def std(self) -> 'Daifenshu':
        '带分数标准化'
        a=self
        a.fenzi+=a.zhengshu*a.fenmu
        a.zhengshu=a.fenzi//a.fenmu
        a.fenzi=a.fenzi%a.fenmu
        a.fenzi, a.fenmu=a.fenzi//gcd(a.fenzi, a.fenmu), a.fenmu//gcd(a.fenzi, a.fenmu)
        return a

    def __str__(self):
        '打印'
        a=self.std()
        hzsz=hanzishuzi
        if a.zhengshu==0:
            if a.fenzi==0:
                return '零'
            else:
                return '{}分之{}'.format(hzsz(a.fenmu), hzsz(a.fenzi))
        else:
            if a.fenzi==0:
                return hzsz(a.zhengshu)
            else:
                return '{}又{}分之{}'.format(hzsz(a.zhengshu), hzsz(a.fenmu), hzsz(a.fenzi))

    def jiafenshu(self) -> 'Daifenshu':
        '将带分数化为假分数'
        return Daifenshu(
            zhengshu=0,
            fenzi=self.fenzi+self.fenmu*self.zhengshu,
            fenmu=self.fenmu
        )

    def __add__(self, other: 'Daifenshu') -> 'Daifenshu':
        '通分加法'
        a=self.jiafenshu()
        b=other.jiafenshu()
        return Daifenshu(
            zhengshu=0,
            fenzi=a.fenzi*b.fenmu+a.fenmu*b.fenzi,
            fenmu=a.fenmu*b.fenmu
        )

def jingfenshu(renshu: Daifenshu, qianshu: Daifenshu) -> Daifenshu:
    '经分术, 输入人数和钱数, 输出每人分得的钱数'
    renshu=renshu.jiafenshu()
    qianshu=qianshu.jiafenshu()
    return Daifenshu(
        zhengshu=0,
        fenzi=qianshu.fenzi*renshu.fenmu,
        fenmu=qianshu.fenmu*renshu.fenzi
    )

if __name__=='__main__':
    #测试: 今有七人，分八钱三分钱之一。问人得几何？答曰：人得一钱、二十一分钱之四。
    print(jingfenshu(
        renshu=Daifenshu(
                zhengshu=7,
                fenzi=0,
                fenmu=1
            ),
        qianshu=Daifenshu(
                zhengshu=8,
                fenzi=1,
                fenmu=3
            )
        )
    )
    #测试: 又有三人，三分人之一，分六钱三分钱之一，四分钱之三。问人得几何？答曰：人得二钱、八分钱之一。
    print(jingfenshu(
        renshu=Daifenshu(
                zhengshu=3,
                fenzi=1,
                fenmu=3
            ),
        qianshu=Daifenshu(
                zhengshu=6,
                fenzi=1,
                fenmu=3
            )+Daifenshu(
                zhengshu=0,
                fenzi=3,
                fenmu=4
            )
        )
    )