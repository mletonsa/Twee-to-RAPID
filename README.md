# Twee-to-RAPID

These are draft codes for an upcoming conference article. Link to conference paper and more information will be added later to provide further explanation.

Our older version from Twine twee stories to Arduino can be found at [https://github.com/digitarina/TweeToArduino/]

## Universal Turing Machine 4-6.twee

An example of Universal Turing Machine implementation in Twine twee format. Here is an example how the code looks like:

```
:: Start
You are at the beginning of the tape, in state q0.
[[Read 0->q0_0]] | [[Read 1->q0_1]] | [[Read 2->q0_2]] | [[Read 3->q0_3]] | [[Read 4->q0_4]] | [[Read 5->q0_5]]

:: q0
You are in state q0.
[[Read 0->q0_0]] | [[Read 1->q0_1]] | [[Read 2->q0_2]] | [[Read 3->q0_3]] | [[Read 4->q0_4]] | [[Read 5->q0_5]]

:: q0_0
You read symbol 0 in state q0. You will write 1 and move right.
[[Move to q1->q1]]
```

## trans.py

Takes UTM.twee and converts it to RAPID code saving result to UTM.rapid. 

Currently it is not general twee to rapid translator but works as an example code. General translator requires some common guidelines what is allowed in the code and how it is connected to robots.

## UTM.rapid

An example of Universal Turing Machine automatically translated from Twee to RAPID. Here is an example how the code looks like:

```
q0:
GetSymbol;
Test symbol
Case 0:
    Goto q0_0;
Case 1:
    Goto q0_1;
Case 2:
    Goto q0_2;
Case 3:
    Goto q0_3;
Case 4:
    Goto q0_4;
Case 5:
    Goto q0_5;

q0_0:
PutSymbol 1;
TurnRobot_right;
Goto q1;

q0_1:
PutSymbol 2;
TurnRobot_left;
Goto q2;
```

q0, q1, q2 and q3 are the four states in this machine and switching states is implemented by Goto commands. Functions GetSymbol, PutSymbol, TurnRobot_left, and TurnRobot_right need to be implemented in RobotStudio. Here a single turning robot is chosen so turn left and right correspond to move left and right in a tape.

Notice that we have mapped the original symbols using: {0, 1, b, b_left, b_right, c} → {0,1,2,3,4,5}

And we use the following UTM(4,6) program by Rogozhin (Rogozhin, Y. "Small universal Turing machines." Theoretical Computer Science 168, no. 2 (1996): 215-240.):

```
q1 1b Lq1	q2 10 Rq2	q3 11 Rq3	q4 10 Rq4
q1 bb Rq1	q2 bb Lq3	q3 bb Rq4	q4 bc Lq2
q1 bb Lq1	q2 bb Rq2	q3 bb Rq3	q4 bb Rq4
q1 60 Rq1	q2 bb Lq2	q3 b -	        q4 -
q1 05 Lq1	q2 01 Lq2	q3 0c Rq1	q4 0c Lq2
q1 c0 Rq4	q2 cb Rq2	q3 cl Rq1	q4 cb Rq4
```
