import numpy as np
import random
import matplotlib.pyplot as plt
class Actions:
    def __init__(self, name):
        self.name=name
        self.mean=0
        self.N=0
    def choose(self,name):
        if name=="Poisson":
            return np.random.poisson(2,None)
        if name=="Gaussian":
            return np.random.normal(2,1,None)
        if name=="FairCoinToss":
            toss=np.random.randint(2)
            if toss==0:
                return 5.0
            else:
                return -6.0
        if name=="Exponential":
            return np.random.exponential(3,None)
        if name=="CrazyButton":
            chance=np.random.randint(4)
            if chance==0:
                return  np.random.poisson(2,None)
            elif chance==1:
                return  np.random.normal(2,1,None)
            elif chance==2:
                toss=np.random.randint(2)
                if toss==0:
                    return 5.0
                else:
                    return -6.0
            else:
                return np.random.exponential(3,None)        
    def update(self, x):
        self.N+=1
        # self.mean = (1-1.0/self.N)*self.mean + 1.0/self.N*x
        self.mean = self.mean + (1.0/self.N)*(x-self.mean)
def run_experiment(eps, N=1000, S=100):
    actions=[Actions("Poisson"), Actions("Gaussian"), Actions("FairCoinToss"), Actions("Exponential"), Actions("CrazyButton")]
    data= np.empty(N)
    for i in range(N):
        v =0
        for j in range(S):
            p=np.random.random()
            if p < eps:
                j=np.random.choice(5)
            else:
                j=np.argmax([a.mean for a in actions])
            x=actions[j].choose(actions[j].name)
            actions[j].update(x)
            v +=x
        data[i]=v/S
    #cumulative_average = np.cumsum(data)/(np.arange(N)+1);
    return data
    #plt.plot(cumulative_average)
    #plt.show()
if __name__ == '__main__':
    c_1=run_experiment(0,100)
    c_2=run_experiment(0.01,100)
    c_3=run_experiment(0.1,100)
    plt.plot(c_1, color='red')
    plt.plot(c_2, color='green')
    plt.plot(c_3, color='blue')
    plt.xlabel('Time Steps')
    plt.ylabel('Cumulative Average Reward')
    plt.legend(['eps=0, greedy', 'eps=0.01, greedy', 'eps=0.1, greedy'])
    plt.show()
    plt.show()

        
