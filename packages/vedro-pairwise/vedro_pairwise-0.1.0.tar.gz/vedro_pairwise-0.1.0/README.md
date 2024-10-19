# vedro-pairwise

[![PyPI Version](https://img.shields.io/pypi/v/vedro-pairwise)](https://pypi.org/project/vedro-pairwise/)
[![License](https://img.shields.io/github/license/mickeystreicher/vedro-pairwise)](https://github.com/mickeystreicher/vedro-pairwise/blob/main/LICENSE)

`vedro-pairwise` is a Python package that extends the [Vedro](https://vedro.io/) framework by enabling pairwise testing. Pairwise testing allows you to generate an optimal set of test cases, covering all possible pairs of parameter values. This approach reduces the number of test cases while ensuring good coverage, making it particularly useful for handling large sets of test combinations.

## Installation

Install [vedro-pairwise](https://pypi.org/project/vedro-pairwise/) using pip:

```sh
$ pip install vedro-pairwise
```

## Usage

To use `vedro-pairwise`, import the `params_pairwise` decorator from the package and apply it to your test scenarios in a `vedro` test suite.

### Example

Here is an example of how to use `vedro-pairwise` to test a web page's rendering on different browsers, resolutions, and operating systems:

```python
import vedro
from vedro_pairwise import params_pairwise

class Scenario(vedro.Scenario):
    subject = "Open /about page ({browser}, {resolution}, {os})"

    @params_pairwise(
        ["chrome", "firefox", "safari"],
        ["1024x720", "1920x1080", "800x600"],
        ["Windows", "Mac", "Linux"]
    )
    def __init__(self, browser, resolution, os):
        self.browser = browser
        self.resolution = resolution
        self.os = os

    def when_user_opens_page(self):
        self.page = open_about_page(self.browser, self.resolution, self.os)

    def then_it_should_show_main_content(self):
        assert self.page.main_content.is_visible()
```

Using pairwise testing for this set of parameters with three browsers, three resolutions, and three operating systems reduces the number of test cases while ensuring that every possible pair of values from different parameters is tested at least once. This minimizes the number of test cases below the full combination of NxMxO.

- **Browser**: `["chrome", "firefox", "safari"]` (3 values)
- **Resolution**: `["1024x720", "1920x1080", "800x600"]` (3 values)
- **Operating System**: `["Windows", "Mac", "Linux"]` (3 values)

With **full combinatorial testing**, the total number of test cases would be:

- ( 3 x 3 x 3 = 27 ) test cases.

With **pairwise testing**, it is only necessary to ensure that every pair of parameters (Browser + Resolution, Browser + OS, Resolution + OS) is covered at least once. This reduces the number of required test cases.

### Pairwise test cases:

| Test Case | Browser   | Resolution  | Operating System |
|-----------|-----------|-------------|------------------|
| 1         | chrome    | 1024x720    | Windows          |
| 2         | chrome    | 1920x1080   | Mac              |
| 3         | chrome    | 800x600     | Linux            |
| 4         | firefox   | 1024x720    | Mac              |
| 5         | firefox   | 1920x1080   | Linux            |
| 6         | firefox   | 800x600     | Windows          |
| 7         | safari    | 1024x720    | Linux            |
| 8         | safari    | 1920x1080   | Windows          |
| 9         | safari    | 800x600     | Mac              |

### Explanation:

- Each **browser** is paired with each **resolution** and **OS** at least once.
- Each **resolution** is paired with each **browser** and **OS** at least once.
- Each **OS** is paired with each **browser** and **resolution** at least once.

This results in **only 9 test cases**, a significant reduction from the 27 required for full combinatorial testing.

### Running Tests

Run the scenarios using the `vedro` command:

```sh
$ vedro run
```

The output will show the test cases executed, ensuring that all pairs of parameters are covered:

```sh
Scenarios
*
 ✔ Open /about page (chrome, 1024x720, Windows)
 ✔ Open /about page (firefox, 1920x1080, Windows)
 ✔ Open /about page (safari, 800x600, Windows)
 ✔ Open /about page (safari, 1920x1080, Mac)
 ✔ Open /about page (firefox, 1024x720, Mac)
 ✔ Open /about page (chrome, 800x600, Mac)
 ✔ Open /about page (chrome, 1920x1080, Linux)
 ✔ Open /about page (firefox, 800x600, Linux)
 ✔ Open /about page (safari, 1024x720, Linux)

# --seed a52af61f-01b8-4f3a-b44f-07af341b44ff
# 9 scenarios, 9 passed, 0 failed, 0 skipped (4.21s)
```

`vedro-pairwise` is a powerful tool for optimizing your test coverage without the overhead of exhaustive matrix testing. It balances test efficiency and coverage, making it an essential tool for managing complex test scenarios.
