# Algorithm to solve system of linear inequalities
This is a algorithm solves system of inequalities to find out solutions of the system of linear inequalities.

## The theoretical basis of the algorithm
The algorithm follows two basic rules as follows:

### 1. "Additional side" rule

The first is the "additional side" property of two inequalities. When adding both sides of two inequalities in the same direction, the resulting inequality is always correct and does not change direction.

$$
\[\left\{ \begin{array}{l}
{a_1}.{x_1} + {a_2}.{x_2} +  \ldots  + {a_n}.{x_n} \ge {V_1}\\
{b_1}.{x_1} + {b_2}.{x_2} +  \ldots  + {b_n}.{x_n} \ge {V_2}
\end{array} \right.\]
$$

$$
\to ({a_1} + {b_1}).{x_1} + ({a_2} + {b_2}).{x_2} +  \ldots  + ({a_n} + {b_n}).{x_n} \ge {V_1} + {V_2}
$$

### 2. Multiply the inequality by a constant

Property of multiplying a positive number by an inequality. When multiplying both sides of an inequality by a positive integer, the inequality is always correct and does not change direction.

With:

$$ {a_1}.{x_1} + {a_2}.{x_2} +  \ldots  + {a_n}.{x_n} \ge V $$

And $c$ ( $\forall c \in \mathbb{R}, c \ge 0$ ), there's always:

$$c.{a_1}.{x_1} + c.{a_2}.{x_2} +  \ldots  + c.{a_n}.{x_n} \ge c.V$$

## Usage
### Download
To download the tool, type in Command Prompt on Windows or Terminal on other operating systems as follows:
    
    git clone https://github.com/Truongphi20/inequaltion.git

### Check settings
Move the terminal's working directory to the downloaded "inequation" directory (`cd inequation`).
    
    python .\sinequal.py -h
    
Output:

    usage: sinequal.py [-h] [-f FILE_INPUT] [-v]

    optional arguments:
      -h, --help            show this help message and exit
      -f FILE_INPUT, --file_input FILE_INPUT
      -v, --version         show version
      
### Run examples
#### Input file structure
Look at the file "example1.csv", the structure of the input file has the following structure:

        2*a+b<=6
        a+b>=0
        a-b>=1

        {'a':0,'b':0}

The first components are the inequalities, which are the first 3 lines in the example. The inequalities are separated by line breaks.
The second element is the variable declaration and its extrema type, separated from the first element by a blank line.
There are three types of extrema:

   - $0$ is none extrema
   - $1$ is maxima
   - $-1$ is minima

_Note: If there are many extrema conditions, the algorithm will solve the extrema in order from right to left in the variable declaration._

#### Run example 1
Assume or find the values of $a$ and $b$, ( $a,b \in \mathbb{Z}$ ) to satisfy the following linear inequalities:

$$
\left\{ {\begin{array}{*{20}{l}}
{2a + b \le 6}\\
{a + b \ge 0}\\
{a - b \ge 1}
\end{array}} \right
$$

To solve the system of inequalities in example 1 above, we run the following command line:

    python .\sinequal.py -f .\example1.csv
    
Output:

    (['a', 'b'], [[6, -6], [5, -5], [4, -4], [5, -4], [3, -3], [4, -3], [2, -2], [3, -2], [4, -2], [1, -1], [2, -1], [3, -1], [1, 0], [2, 0], [3, 0], [2, 1]])

As a result, the list has two components: the names of the variables and the the list of solutions of those corresponding variables.
So the solutions $(a,b)$ of the system of inequalities are:

<p align="center">
$(6,-6)$, $(5,-5)$, $(4,-4)$, $(5,-4)$, $(3,-3)$, $(4,-3)$, $(2,-2)$, $(3,-2)$, $(4,-2)$, $(1,-1)$, $(2,-1)$, $(3,-1)$, $(1,0)$, $(2,0)$, $(3,0)$, $(2,1)$
</p> 

#### Run example 2
Also with the above system of inequalities, if we want to find a solution such that $a + b$ is the largest. Then the system of inequalities will look like this:

$$
\left\{ {\begin{array}{*{20}{l}}
{2a + b \le 6}\\
{a + b \ge 0}\\
{a - b \ge 1}\\
{a + b -P = 0}
\end{array}} \right
$$

We consider P as a variable to be solved and to find its maximum value. So the variable declaration component in input file will be as follows:

    {'a':0,'b':0,'P':1}

Similarly, to run example 2 we run the following command:

    python .\sinequal.py -f .\example2.csv
    
Output:

    (['a', 'b', 'P'], [[3, 0, 3], [2, 1, 3]])
    
So the maximum value of $a+b$ is 3 when $(a,b) = (3,0),(2,1)$.

As we can also see in Example 1, when adding the extreme condition P, only the above two solutions are satisfied.

#### Run example 3
Not stopping there, if we add one more extreme condition that a-b must be minimal. We have an inequalities system as follows:

$$
\left\{ {\begin{array}{*{20}{l}}
{2a + b \le 6}\\
{a + b \ge 0}\\
{a - b \ge 1}\\
{a + b -P = 0}\\
{a-b-M = 0}
\end{array}} \right
$$

Similarly, we consider M to be an extreme variable to be solved, declare the variable, and set it to be the minima.

    {'a':0,'b':0,'M':-1,'P':1}
    
Run the following command to solve:
    
    .\sinequal.py -f .\example3.csv
    
Output:
    
    (['a', 'b', 'M', 'P'], [[2, 1, 1, 3]])

From example 2 it is also easy to predict that the solution of the system of inequalities of example 3 is $(a,b) = (2,1)$

So the meaning of the solution process in example 3 is that first find the solutions that satisfy the condition in example 2, $a+b$ is the maxima, and among those solutions, choose the solutions that satisfy the second condition that $a-b$ must be minima.

Therefore, it is necessary to pay attention to the order of extreme solutions when declaring variables. A different order will lead to different results
