# Green's Function ODE Solver

## Overview
This project provides a solution to two Ordinary Differential Equations (ODEs):
1. The homogeneous solutions for:
   - \( y'' + 2y' + y = 0 \)
   - \( y'' + y = 0 \)
2. A Green's function approach to solve \( y'' + y = t^2 \) using numerical integration.

## Features
- Symbolic solving of ODEs using SymPy
- Numeric evaluation and plotting of homogeneous solutions
- Green’s function implementation with numerical integration
- Graphical visualization of the solutions using Matplotlib

## Installation
### Prerequisites
Ensure you have Python installed (preferably 3.7 or later). You also need the following libraries:
- `sympy`
- `numpy`
- `matplotlib`

You can install them using pip:
```sh
pip install sympy numpy matplotlib
```

## Usage
### Running the Script
Clone the repository and navigate to the project directory. Run the script using:
```sh
python main.py
```
This will:
1. Solve the homogeneous ODEs symbolically.
2. Convert the symbolic solutions into numeric functions.
3. Plot the homogeneous solutions.
4. Define and numerically integrate the Green’s function solution.
5. Plot the Green’s function-based solution.

### Expected Output
- Two plots showing the homogeneous solutions.
- A third plot displaying the numerical solution using Green’s function.

## File Structure
```
project-root/
│-- main.py          # Main script to solve and plot ODE solutions
│-- README.md        # This documentation
```

## Contributions
Feel free to submit pull requests or report issues!

## License
This project is open-source under the MIT License.

