import random

def media(X):
    return sum(X) / len(X)

if __name__ == '__main__':
    X = [random.randint(0, 20) for i in range(20)] 
    mu = media(X)

    print(X)
    print(mu)