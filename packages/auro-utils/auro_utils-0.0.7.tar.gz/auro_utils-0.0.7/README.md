[![Official](https://img.shields.io/badge/Official%20-Auromix-blue?style=flat&logo=world&logoColor=white)](https://github.com/Auromix) &nbsp;
[![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04-green)](https://ubuntu.com/) &nbsp;
[![LICENSE](https://img.shields.io/badge/license-Apache--2.0-informational)](https://github.com/Auromix/auro_joystick/blob/main/LICENSE) &nbsp;
[![GitHub Repo stars](https://img.shields.io/github/stars/Auromix/auro_utils?style=social)](https://github.com/Auromix/auro_utils/stargazers) &nbsp;
[![Twitter Follow](https://img.shields.io/twitter/follow/Hermanye233?style=social)](https://twitter.com/Hermanye233) &nbsp;

# 🛠️ Auro Utils

Auro Utils is a utility toolkit, providing enhanced logging, performance profiling, etc.

## ⚙️ Installation

To install Auro Utils, you can use one of the following methods:

```bash
# Install from PyPI
pip install auro_utils
```

```bash
# Install from the current directory (local development)
git clone https://github.com/Auromix/auro_utils
cd auro_utils
pip install -e .
```

## 🔥 Quickstart

You can find detailed examples for the project in the `examples` directory of the repository.

### logger

Logger is a class that can be used to log messages to the console and to a file. It is a wrapper around loguru.

```python
from auro_utils import Logger
my_logger = Logger()
my_logger.log_info("This is a info log test.")
```

![logger_cmd](/assets/images/logger/logger_cmd.png)

### profiler

Decorator for profiling and analyzing performance of functions. It is a wrapper around yappi.

```python
# Import the profiler
from auro_utils.profiler import auro_profiler


# Use the profiler as a decorator
@auro_profiler
# Your code here
def your_function_code():
    # Simulate your time-consuming operations
    import time

    time.sleep(2)
```

![profiler_cmd](/assets/images/profiler/profiler_cmd.png)

![profiler_web](/assets/images/profiler/profile_results.png)

### manager

Functions in manager can be used to read and write files and process paths.

```python
# Load the configuration from the specified TOML file
loaded_config = au.load_config(
    config_file_path, relative_to=home_dir, file_type="toml"
)

# Print the loaded configuration data
print("Loaded configuration:", loaded_config)
```

## 🧪 Test

```bash
cd auro_utils
python3 -m pytest -v .
```

## 🧑‍💻 Documentation

For comprehensive documentation, please refer to the comments within the source code and examples.

## 🙋 Troubleshooting

If you encounter any issues or have questions regarding this package, please contact the maintainers:

- Herman Ye @Auromix (Email: <hermanye233@icloud.com>)

## 📜 License

```text
Copyright 2023-2024 Herman Ye@Auromix

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at:

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the specific
language governing permissions and limitations under the License.
```

## 🏆 Contributing

Contributions are welcome! Please follow the guidelines provided in the repository for contributing.
