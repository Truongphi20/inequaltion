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

