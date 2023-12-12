#!/usr/bin/python3

"""
This function retrieves and returns system information about CPU times.

Args:
    information_type (str, optional): The specific information to retrieve.
        - One of the following values:
            - user: Time spent by normal processes in user mode.
            - system: Time spent by the operating system in kernel mode.
            - idle: Time spent in the idle task.
            - iowait: Time spent waiting for I/O to complete.
            - irq: Time spent servicing hardware interrupts.
            - softirq: Time spent servicing software interrupts.
            - steal: Time stolen by a guest operating system.
            - nice: Time spent by normal processes in user mode with low priority.
            - guest: Time spent by a guest operating system.
            - guest_nice: Time spent by a guest operating system with low priority.
        - Defaults to None, which retrieves all available information.

Returns:
    dict: A dictionary containing the retrieved information and its value,
        or None if an error occurs.
"""

import psutil


def get_cpu_times(information_type=None):
    try:
        cpu_times = psutil.cpu_times()
        available_types = {attr for attr in dir(cpu_times) if not callable(getattr(cpu_times, attr)) and not attr.startswith("__")}

        # Retrieve all information if not specified
        if information_type is None:
            return {attr: getattr(cpu_times, attr) for attr in available_types}

        # Validate information type
        if information_type not in available_types:
            raise ValueError(f"Invalid information type: {information_type}")

        # Return specific information
        return {information_type: getattr(cpu_times, information_type)}

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired) as error:
        # Log error message and raise exception
        logger.error(f"Error retrieving CPU times: {error}")
        raise error

    except KeyError:
        logger.error(f"Invalid attribute name: {information_type}")
        raise ValueError(f"Invalid attribute name: {information_type}")

if __name__ == "__main__":
    try:
        cpu_info = get_cpu_times()
        if cpu_info is not None:
            for seq_num, (name, value) in enumerate(cpu_info.items(), start=1):
                print(f"{seq_num}. {name}: {value} seconds  # Time spent in {name} mode")

        user_time = get_cpu_times("user")
        if user_time is not None:
            print(f"User time: {user_time} seconds  # Time spent by normal processes in user mode")
    except Exception as error:
        print(f"Error occurred: {error}")



"""The hasattr function checks if the specified attribute exists on the object.
The getattr function retrieves the value of the specified attribute on the object.
The dir(cpu_times) function returns a list of all attributes and methods of the cpu_times object.
The callable function checks if the specified attribute is a function or method.
The if not attr.startswith("__") condition excludes attributes starting with double underscores, which are typically internal or private attributes.
Resources: https://chat.openai.com/share/4fec93b9-09a4-43c1-87df-5f00ed8e05b9 """