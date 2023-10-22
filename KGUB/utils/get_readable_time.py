def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    # s - seconds
    # m - minutes
    # h - hours
    # D - days
    # w - weeks
    time_suffix_list = ["s", "m", "h", "D", "w"]

# TODO: understand the use of count variable
    while count < 4:
        count += 1

        # remainder after division in remainder
        # result after modulo in result
        remainder, result = int(divmod(seconds, 60 if count < 3 else 24)) 

        # nothing left to divide and no remainder then get out of the loop
        if seconds == 0 and remainder == 0:
            break

        # adds the result to the list of time
        time_list.append(result)
        # second is updated using remainder
        seconds = remainder

# ==========OLD CODE IGNORE============
        # if count < 3:
        #     remainder, result = divmod(seconds, 60)
        # else:
        #     remainder, result = divmod(seconds, 24)
        # if seconds == 0 and remainder == 0:
        #             break
        # time_list.append(int(result))
        # seconds = int(remainder)
# =====================================

    # iterate on the indices of the list
    for x in range(len(time_list)):
        # takes the time values and add the suffix to it
        time_list[x] = str(time_list[x]) + time_suffix_list[x]

    if len(time_list) == 4:
        # TODO: why is this?
        ping_time += time_list.pop() + ", "

    # reverses the list items
    time_list.reverse()
    # creates the time sting in the h:m:s format
    ping_time += ":".join(time_list)

    # give back the time in time string format
    return ping_time