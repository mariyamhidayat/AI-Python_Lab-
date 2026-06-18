def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):

    # Base case: if we reach leaf node (final depth)
    if depth == 3:
        return values[nodeIndex]

    # If current player is Maximizer
    if maximizingPlayer:
        best = -1000  # initialize best as very small value

        # Explore left and right child (binary tree)
        for i in range(2):

            # Recursive call for next depth, switch to Minimizer
            val = alphabeta(depth + 1,
                            nodeIndex * 2 + i,
                            False,
                            values,
                            alpha,
                            beta)

            # Update best value for Maximizer
            best = max(best, val)

            # Update alpha (best value Maximizer can guarantee)
            alpha = max(alpha, best)

            # Alpha-Beta Pruning condition
            # If beta is less than or equal to alpha,
            # no need to explore further branches
            if beta <= alpha:
                break

        return best

    # If current player is Minimizer
    else:
        best = 1000  # initialize best as very large value

        # Explore left and right child
        for i in range(2):

            # Recursive call for next depth, switch to Maximizer
            val = alphabeta(depth + 1,
                            nodeIndex * 2 + i,
                            True,
                            values,
                            alpha,
                            beta)

            # Update best value for Minimizer
            best = min(best, val)

            # Update beta (best value Minimizer can guarantee)
            beta = min(beta, best)

            # Alpha-Beta Pruning condition
            # If beta <= alpha, stop exploring further
            if beta <= alpha:
                break

        return best


# Leaf node values of the game tree
values = [3, 2, 6, 9, 1, 8, 0, -1]

# Start Alpha-Beta pruning from root
# depth=0, nodeIndex=0, Maximizer starts first
result = alphabeta(0, 0, True, values, -1000, 1000)

print("Optimal Value:", result)