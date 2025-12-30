clear all
close all
clc
alpha=0.1;
Q_table=zeros(5,5)
epsilon=0.8;
gamma=0.5;
for days=1:3000
    state=1 ;    %state==room
    for token=1:50
        action=e_greedy(Q_table,state,epsilon);
        reward=reward_function(state,action);
        Q_table(state,action)=Q_table(state,action)+...
            alpha*(reward-gamma*Q_table(state,action));
        state=action;
    end
    epsilon=epsilon*0.9999
end