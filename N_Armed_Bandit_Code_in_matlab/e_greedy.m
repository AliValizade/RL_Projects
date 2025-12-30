function[action]=e_greedy(Q_table,state,epsilon)
rand=random('uniform',0,1);
[m,index]=max(Q_table(state,:));
if rand<(1-epsilon)
    action=index;
else
    while(1)
    action=randi(size(Q_table,2));
    if action~=index
        break
    end
end
end
