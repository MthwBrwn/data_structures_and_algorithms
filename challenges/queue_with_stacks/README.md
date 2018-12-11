# Queue with Stacks

**Author**: Matthew Brown
**Version**: 1.0.0

## Challenge
This application sets up a class of pseudocode that creates objects that act as queues made up of two stacks and their methods push pull and peek

## Approach & Efficiency
The concept of the having two stacks A (enqueue ) and B (dequeue) and moving all the nodes from A to B if dequeue is called and B to A if enqueue is called is a O(n) for time operation The actual transfer at the top of each stack is O(1) so it really depends on the depth of the stacks. This function stays with the same stack it starts with so space is O(1)

## Architecture
This application is written in Python3.6
This uses Pytest for unit testing

## Solution
