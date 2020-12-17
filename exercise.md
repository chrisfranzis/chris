# Introduction to Programming Exercise 01

* Submission by Sunday (10-01-2021) 16:59:59 over OLAT https://lms.uibk.ac.at/olat/dmz/
* Compress your solution as tar.gz or zip file
* Do not forget to mark solved exercises
* Prepare your exercises so that you are able to present them during the course
* You might want to open this file in a program supporting markdown syntax or in 
  [gitlab](https://git.uibk.ac.at/c7031289/eidp_python)
* Code should be formatted as presented in the lecture slides (this includes naming conventions)

## Searching for Help

* You can always ask for help in the OLAT forum channel
* You can also contact me for questions by E-Mail [harald.schweiger@uibk.ac.at](mailto:harald.schweiger@uibk.ac.at)

## Tests and Documentation

Make sure that your solutions can be run with Python version 3.7 or higher.
Documenting your code is appreciated as it helps to understand the purpose of your code.
In case of faulty code good documentation can help in gathering points.


## Exercise A: Looping with For (2 Points)

Import from `module_a` the `randfun` function.
This function generates a sequence of numbers, over which can be iterated.
The usage of randfun(size) is similar to the `range` function.

    for x in randfun(n):
        print(x)

The task is to calculate the **maximum** and **minimum** value as well as the **average** and **variance** of a sequence 
over around 1000 numbers by using a for loop. Your are not allowed to use built-in functions such as min, max, sum or 
similar to solve this task.  

Also answer the question: "What happens when `random.seed(42)` is executed before `randfun` is used?"
To answer this question you will need to import the random module and execute the program more than one time in the row.

**Submit as:** exercise_a.py


## Exercise B: Rock Paper Scissors (3 Points)

In this exercise your should implement the [rock paper scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors) 
game. It is the goal to win 3 games against the computer, which picks one of the three tools randomly.
If the user or the computer opponent wins the game, the program will print a win or game over message and will exit.  
The following steps should be implemented:

* Write a function `tool(choice)` which converts the integers 0, 1, 2 to the strings 'Rock', 'Paper' and 'Scissors'
respectively. The integer is given by the parameter `choice` and the corresponding name of the tools will be returned as 
a string by the function. Implement also some kind of error handling, if choice is not an integer between 0 and 2.

* Implement a function `who_wins(user_a, user_b, choice_a, choice_b)` which returns:
    * The parameter `user_a` if `choice_a` wins over `choice_b`
    * The parameter `user_b` if `choice_b` wins over `choice_a`
    * `None` if it is a draw. Both users picked the same tool.
    
* Create a function which returns randomly the integers 0, 1 or 2.
You might want to import `random` module to simulate this behavior.

* Implement a function menu() which prints out all possible choices and waits till the user made an input.
If users make an invalid input, let them repeat this step till they make a correct one.
The valid input should be returned from the function.

* Create a function `single_player(player_name)` which contains the main logic for this game.
It will use the functions defined above and keeps track of the number of wins for the computer and the user.
If one opponent has more than 3 wins, the game will stop.  

The end result of this exercise could look similarly as shown below:

    Player Name: Test_User
    
    --- Make a choice
    --- ROCK:       0
    --- PAPER:      1
    --- SCISSORS:   2
    --- Quit:       q
    Choice:	        1

    SCISSORS wins against PAPER
    Computer scored 1 Point

        0 --- | --- 1
    --- Make a choice
    --- ROCK:       0
    --- PAPER:      1
    --- SCISSORS:   2
    --- Quit:       q
    Choice:	        2

    ...

    Its a draw
    --- Make a choice
    --- ROCK:       0
    --- PAPER:      1
    --- SCISSORS:   2
    --- Quit:       q
    Choice:	        0

    ROCK wins against SCISSORS
    Test_User scored 1 Point

    3 --- | --- 1
    Test_User has won the game!

**Submit as:** exercise_b.py


## Exercise C: Monty Hall Problem (3 Points)

The Monty Hall problem is a brain teaser, which proofs that the majority of people can shut oneself off from the truth 
if the truth seems to be counterintuitive. Numerous scientists have been fooled and it is now your job to show them the
truth by simulating thousands of runs to confirm the probability distribution of 
[The Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem).

    Suppose you're on a game show, and you're given the choice of three doors: 
    Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, 
    who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, 
    "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

The following rules apply:
    
    1. The host must always open a door that was not picked by the contestant.
    2. The host must always open a door to reveal a goat and never the car.
    3. The host must always offer the chance to switch between the originally chosen door and the remaining closed door.

To solve this task, implement the following function that should guide you to the solution.

* Take a look in the `random` module and find a function which takes a sequence and returns randomly
one element of this sequence. Remember that one sequence we have introduced so far are tuples.

* Write a function `pick_other(pair, elem)` which takes a pair which is a tuple with two elements.
The function should return the element of the pair that is different from elem.

* Implement a function `remove_from_three(triple, elem):` which takes a tuple with three elements and returns a pair.
The pair should contain all elements of the triple but not the one represented by the parameter `elem`.

* Implement the behavior of the moderator, who picks one door with a goat behind.
Remember the moderator is not allowed to pick the door that has been chosen by the player.
The moderator should pick between two doors randomly if the player has chosen the door with a car behind. 
The door chosen by the moderator should be returned by this function.

* Write a function that implements the logic of one game session.
    * A winning door is randomly selected
    * The player selects randomly one door
    * Monty will remove one door with a goat
    * The player chooses the other remaining door
    * The function returns True if the player has won the car
    
* Measure in around 10000 iterations, how often the player wins the car using this strategy.
    
**Submit as:** exercise_c.py

## Exercise D: Recursion (2 Points)

Similar as in `Exercise D` of the last assignment [Euler's number](https://www.mathsisfun.com/numbers/e-eulers-number.html) 
should be approximated by a given precision.
However, this time you are not allowed to use any while or for loops.
Use instead recursion and implement the following two functions:

* `factorial(n)` will return the factorial of n
* `euler(n)` will return the euler number by precision n

You can use the mathematical notion of the base case and recursive case as seen below to implement the two functions.

![equation1](equations/factorial.png)
   
   
![equation2](equations/euler.png)


**Submit as:** exercise_d.py