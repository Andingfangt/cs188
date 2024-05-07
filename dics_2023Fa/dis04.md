# Regular Discussion 4

## 1. Games

(a)

                 4   
          /      |       \    
         3       2       4
       / | \   / | \   / | \     
      10 8  3 2  15 7  6  5  4

(b)
The 15 and 7 can be pruned, cause when check the node 2, front node give alpha = 3, and since $2\leq \alpha$, so the followed branches will be cut.

(c)

                 8   
          /      |      \    
         7       8       5
       / | \   / | \   / | \     
      10 8  3 2  15 7 6  5  4

(d)
In chance node, we can't prune.

## 2. Nonzero-sum Games

(a)
![图 0](../images/6f5cb7b57915588b420421fa0ea2a0bcc93ddc606224fff1ff5649c71b24fac2.png)  

(b)
No nodes can be pruned. Because this game is non-zero-sum, there can exist a leaf node anywhere in the tree that is good for both player A and player B.






