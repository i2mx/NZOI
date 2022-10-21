class Spell:
    def __str__(self) -> str:
        return f"{(self.A + self.B) % 10000} {(self.C + self.D) % 10000}"

    def __mul__(self, other):

        new_A = self.A * other.A + self.B * other.C
        new_B = self.A * other.B + self.B * other.D
        new_C = self.C * other.A + self.D * other.C
        new_D = self.C * other.B + self.D * other.D

        new_A %= 10000
        new_B %= 10000
        new_C %= 10000
        new_D %= 10000

        return Spell(new_A, new_B, new_C, new_D)

    def __pow__(self, power):
        half_power = power // 2
        half2_power = power - half_power

        if power in self.dp.keys():
            a,b,c,d = self.dp[power]
            return Spell(a, b, c, d)
        
        ans = self**half_power * self**half2_power
        self.dp[power] = (ans.A, ans.B, ans.C, ans.D) 
        return ans

    def __init__(self, A, B, C, D) -> None:
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        
        self.dp = {0: (1,0,0,1), 1: (A,B,C,D)}


A, B, C, D = map(int, input().split())
N = int(input())

print(Spell(A, B, C, D) ** N)
