# Fifo animal shelter

**Author**: Matthew Brown
**Version**: 1.0.0

## Challenge
This application models an animal shelter that holds dogs and cats and has the rule that animals first in must be first out- A choice can be made as to whether a dog is selected a cat is selected or no preference.

## Approach & Efficiency
This goes about solving the challenge by having two queues one a dog and the other a cat. when a selection is made, a dequeue_cat or dequeue_dog will remove the front node. This action is a O(1). This model was chosen as any type of traversal along the nodes of the queue would result in a greater time complexity.

## Architecture
This application is written in Python3.6
This uses Pytest for unit testing.

## Solution
![](../../assets/fifo-animal-shelter.jpg)
