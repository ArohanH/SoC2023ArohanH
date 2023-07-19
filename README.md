# SoC2023ArohanH
Seasons of Code 2023 Repo Arohan Hazarika


Week 0:
  * Week 0 was based on getting acquainted with Reinforcement Learning, what it is, what are the terms rewards, action, value function, policy, environment etc.         After that we covered Markov Reward/Decision Process where I learnt things like Bellman Equation, probability transition matrix, how do we relate the                 State/Action Value function with all the further states' value function using Bellman Equations. It ended with getting an idea of optimal policy which is             for maximising the final reward.
  * We were assigned a task of writing a game where we needed to use numpy library to generate probabilities based on which the game was played. I have attached the     file game.py
  * There was one more optional task related to writing a MDP where we had a problem where based on our actions that we choose, the environment was randomly             assigning us a state based on their respective probabilities, here we had a reward value which was getting updating after we reached each state. I have attached     the file as MDP.py


Week 1:
  * Week 1 was based on Multi armed bandits and for our week 1 task we had to go through probability theory,random variables and different distributions( poisson,       gaussian, exponential etc). Multi armed bandits was based on epsilon greedy algorithms and updation of the action value(Q) of an action based on the reward we       get after choosing that particular action(Q value learning algorithm).
  * I have attached the code bandit_aarohan.py and a desc file describing the algorithm of the program.
    
Week 2 and 3:
  * Week 2 and 3 had theory task of following David Silver's 3rd, 4th, 5th and 6th Lecture, where we had to cover Dynamic Programming(Value and Policy Iteration,   
    Synchronus DP etc), Monte Carlo and TD Learning etc. Also covered SARSA and Q Learning. Read about Gradient Descent Algorithm.
  * We were assigned task of choosing an environment from OpenAI Gym Environments and test MC/Q Learning algorithms and thereafter do an analysis. I had chosen         Taxi Game Environment and there I could see Q Learning algorithm working much better than MC.
  * I have uploaded the project on my repo and it has been trained for around 1000 episodes for both MC and Q Learning algorithms. A desc file is also attached         explaining the environnment and my brief analysis.
    
Week 4,5,6:
  * These 3 weeks mainly focussed on coverage of theory.
  * Covered Neural Networks, how do they operate-Gradient Descent Algorithm, Cost Functions, Weights/Biases etc. Currently doing rest of the David Silver Lectures      where more complex algorithms like Actor-Critic etc are covered.
    
Week 7,8(Final Task):
  * Final Project to be done on making an agent learn play Street Fighter 2. 
