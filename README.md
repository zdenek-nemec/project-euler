# project-euler
Zdenek versus Project Euler

My solutions for Project Euler problems. Visit https://projecteuler.net/ for
more information about the Project Euler.

## Definition of Done

### Structure
* The problem has its own directory.
* Python 3 is used and specified on the first line of the solution script.

### Code Style
* There is a class Solution() with init() and solve() methods.
* The main() calls Solution().solve() with constants.
* Classes and methods are sorted alphabetically with the exception of
Solution(), init(), solve() and main().
* There are no static methods.
* Apostrophe (') is the default for the strings, not the double quotes (").
* All names (variables, classes, methods, ...) are self-explanatory and do not
contain abbreviations.
* Long if statements are in parentheses with logical operator at the end of the
line.
* Closing parentheses are at the end of the last line of the block.
* There are no code-check warnings from PyCharm and no line exceeds 80
characters.
* Line endings are CRLF.
    
### Functionality
* The solution script can be run and displays only the result, which is accepted
by the Project Euler site.

### Tests
* Unit tests utilize expected and actual variables.
* Unit tests have at least a parameterized test for Solution().solve() method.
* The solution passes all the unit tests.

### Documentation
* The header within the solution script contains complete description of the
problem.
* Sphinx documentation is generated without errors and does not contain any
issues.
