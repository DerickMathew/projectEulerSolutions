class ProjectEulerProblem:
    
    title = """Even Fibonacci numbers"""
    subTitle = """Problem 2 """
    ProblemStatement = """
    Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    def fibo(self,n):
        a,b=0,1
        fibs=[a,]
        while(b<=n):
            a,b=b,a+b
            fibs.append(a)
        return fibs

    def implementation(self):
        print reduce(lambda x,y:x+y, [x for x in self.fibo(4*(10**6)) if x%2==0])


def main():
    ProjectEulerProblem().implementation()

if __name__ == "__main__":
    main()