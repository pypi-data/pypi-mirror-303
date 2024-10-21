import itertools

import pandas as pd
import numpy as np
from scipy import signal


# Function Call to calc engagement and return for upload
def service_detect_engagement(self, measurements, parameter):
    spindleSpeedIdentifier = parameter["spindleSpeedIdentifier"]
    spindleCurrentIdentifier = parameter["spindleCurrentIdentifier"]
    timeIdentifier = parameter["timeIdentifier"]
    mean_limit = parameter["mean_limit"]
    step = parameter["step"]

    start_bounds, end_bounds, results = detect_engagement(measurements=measurements,
                                                          spindleSpeedIdentifier=spindleSpeedIdentifier,
                                                          spindleCurrentIdentifier=spindleCurrentIdentifier,
                                                          timeIdentifier=timeIdentifier, mean_limit=mean_limit,
                                                          step=step)
    # return filtered spindle current and detected engagements
    return start_bounds, end_bounds, results


# --------------------------------------------------
# Specific Service Class for milling engagement
def pairwise(iterable):
    """
    Returns the elements of an iterable as pairwise tuples.
    s = [s0, s2, ..., sn] -> (s0,s1), (s1,s2), (s2, s3), ...


    Parameters
    ----------
    iterable: iterable
        iterable you want to iterate pairwise

    Returns
    -------
    zip(a,b)
        pairwise elements of given iterable
    """
    # source: https://docs.python.org/3/library/itertools.html#recipes
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def determine_milling_time_intervals(spindle_speed, delta=2.5, chunk_size=51):
    """
    Determines candidates for milling time intervals.
    Searches for intervals with constant data.


    Parameters
    ----------
    spindle_speed: arr of float
        the spindle speed data that will be analyzed
    delta: float, optional
        delta that a value may vary from median, by default value 2.5
    chunk_size: int, optional
        the minimum length of a interval, by default value 51

    Returns
    -------
    intervals: arr of tuples
        candidates for milling time
    """

    # filter the spindle speed
    spindle_speed = signal.medfilt(spindle_speed, 251)
    spindle_speed = signal.savgol_filter(spindle_speed, 101, 1)

    i, intervals, length = 0, [], len(spindle_speed)
    chunk_size = abs(chunk_size)
    while i < length:
        interval_start, interval_end = i, -1
        # get the median of the first chunk. median is basis for interval
        chunk_end = i + chunk_size if i + chunk_size < length else length - 1
        chunk = spindle_speed[i:chunk_end]
        chunk_median = np.median(chunk)

        # check if the first chunk fits criteria
        upper_limit = chunk_median + abs(delta)
        lower_limit = chunk_median - abs(delta)
        for j in range(i, chunk_end):
            value = spindle_speed[j]
            limit_condition = lower_limit <= value and value <= upper_limit
            if not limit_condition:
                i = j + 1
                break

        if not limit_condition:
            i = i + 1
            continue

        interval_end = chunk_end  # interval valid in first chunk

        # check how long the criteria fits
        for j in range(chunk_end, length):
            value = spindle_speed[j]
            limit_condition = lower_limit <= value and value <= upper_limit
            if not limit_condition:
                interval_end = j - 1
                break

        # save the interval
        if limit_condition:
            interval_end = length - 1
            i = length
        else:
            i = interval_end + 1

        intervals.append((interval_start, interval_end))
    return intervals


def fix_milling_time_intervals(spindle_speed, time_intervals,
                               delta=2.5, chunk_size=51):
    """
    Auxiliary function, to fuse intervals that are split due to outliers.

    Paramters
    ---------
    spindle_speed: arr of float
        the spindle speed data that will be analyzed
    time_intervals: arr of tuples
        detected intervals for spindle speed data
    delta: float, optional
        delta used to detect time intervals, by default value 2.5
    chunk_size: int, optional
        the minimum length of a interval, by default value 51

    Returns
    -------
    fixed_time_intervals: arr of tuples
        the fixed time intervals
    fixed_time_mean: arr of float
        intervals according to fixed time interval
    """
    # declare variables
    time_intervals_length = len(time_intervals)
    fixed_time_intervals, i = [], 0
    fixed_time_mean, delta = [], abs(delta)

    # iterate incremental
    while i < time_intervals_length:
        # pick and calculate current interval values
        current_interval = time_intervals[i]
        a1, b1 = current_interval[0], current_interval[1]
        current_mean = np.mean(spindle_speed[a1:b1])
        if i == time_intervals_length - 1:
            i = i + 1
        for j in range(i + 1, len(time_intervals)):
            # pick and calculate adjacent interval values
            adjacent_interval = time_intervals[j]
            a2, b2 = adjacent_interval[0], adjacent_interval[1]
            i = j
            # check for distance (?)
            if abs(b1 - a2) < chunk_size:
                adjacent_mean = np.mean(spindle_speed[a2:b2])
                upper_limit = current_mean + delta
                lower_limit = current_mean - delta
                lower_cond = lower_limit <= adjacent_mean
                upper_cond = adjacent_mean <= upper_limit
                # condition...
                if lower_cond and upper_cond:
                    current_interval = (a1, b2)
                    current_mean = np.mean(spindle_speed[a1:b2])
                    b1 = b2
                    i = j + 1
                    continue
            break
        # append current (maybe unified) interval to fixed
        fixed_time_intervals.append(current_interval)
        fixed_time_mean.append(current_mean)

    # return the changed time intervals and accordingly the means
    return fixed_time_intervals, fixed_time_mean


def milling_engagement_simple(filtered_spindle_current, candidate_interval,
                              step=500):
    """
    Calculate the milling engagement for a certain spindle interval.
    Without approaching the noise floor.

    Parameters
    ----------
    filtered_spindle_current: arr of float
        the spindle current (filtered)
    candidate_interval: tuple
        an interval (a,b) which is observed
    step: int
        how far into the noise floor to search for min/max

    Returns
    -------
    engagement: numpy array of positions
        a numpy array that contains detected engagement positions
    """
    a, b = candidate_interval[0], candidate_interval[1]
    current_mean = np.mean(filtered_spindle_current[a:b])
    engagement = []
    front = filtered_spindle_current[a:a + step]
    end = filtered_spindle_current[b - step:b]
    min_front, min_end = min(front), min(end)
    max_front, max_end = max(front), max(end)
    minimum = min((min_front, min_end))
    maximum = max((max_front, max_end))
    for i in range(a + 120, b - 50):
        value = filtered_spindle_current[i]
        if current_mean <= 0:
            noise_condition = value >= minimum
        else:
            noise_condition = value <= maximum
        if not noise_condition:
            engagement.append(i)
    return np.array(engagement, dtype=int)


def milling_engagement(filtered_spindle_current, candidate_interval, step=125):
    """
    Calculate the milling engagement for a certain spindle interval.

    Parameters
    ----------
    filtered_spindle_current: arr
        the spindle current (filtered)
    candidate_interval: tuple
        an interval (a,b) which is observed
    step: int, optional
        how far into the noise floor to search for min/max,
        by default value 125

    Returns
    -------
    engagement: numpy array of int
        a numpy array that contains detected engagement positions
    """

    # intialize variables for the algorithm
    engagement = []
    a, b = candidate_interval[0], candidate_interval[1]
    current_mean = np.mean(filtered_spindle_current[a:b])

    # check if interval is bigger than step * 2
    if (abs(b - a) < step * 2):
        return np.array(engagement, dtype=int)

    # approach the noise floor from the start
    a_end, b_start = a, b
    dir_start = filtered_spindle_current[a + 1] - filtered_spindle_current[a]
    for i in range(a + 1, b - 1):
        l_val = filtered_spindle_current[i]
        r_val = filtered_spindle_current[i + 1]

        dir_temp = r_val - l_val
        if np.sign(dir_start) == np.sign(dir_temp):
            dir_start = dir_temp
        else:
            a_end = i
            break

    # approach the noise floor from the end
    dir_end = filtered_spindle_current[b - 1] - filtered_spindle_current[b]
    for i in range(b - 1, a + 1, -1):
        l_val = filtered_spindle_current[i - 1]
        r_val = filtered_spindle_current[i]

        dir_temp = r_val - l_val
        if np.sign(dir_end) == np.sign(dir_temp):
            dir_end = dir_temp
        else:
            b_start = i
            break

    # detect min and max values for start and end
    front = filtered_spindle_current[a_end:a_end + step]
    end = filtered_spindle_current[b_start - step: b_start]
    minimum = min(np.amin(front), np.amin(end))  # minimum
    maximum = max(np.amax(front), np.amax(end))  # maximum

    # classify the values between the start and end noise floor,
    # iterate the spindle current.
    for i in range(a_end + step, b_start - step):
        value = filtered_spindle_current[i]

        # change the classifying condition depending on wether
        # the electric current direction is positive or negative
        if current_mean <= 0:
            noise_condition = value >= minimum
        else:
            noise_condition = value <= maximum

        if not noise_condition:
            engagement.append(i)  # save detected engagement

    # return all detected engagement positions as numpy array
    return np.array(engagement, dtype=int)


def detect_engagement(measurements, spindleSpeedIdentifier="ss", spindleCurrentIdentifier="sc", timeIdentifier="time",
                      mean_limit=100., step=125):
    """
    Detect the engagement of a milling process analyzing the spindle current.

    Parameters
    ----------
    spindle_current: arr
        the spindle current data that will be analyzed
    candidate_intervals: arr of tuples
        found milling time intervals
    interval_means: arr of floats
        means of the milling time intervals used to filter unfit intervals
    mean_limit: float, optional
        defines the minimum mean of intervals, by default value 100
    step: int, optional
        how far the noise floor of the spindle current is analyzed,
        by default value 125

    Returns
    -------
    spindle_current: arr of float
        the filtered spindle current
    engagements: arr of int
        positions of the analyzed spindle current that classified as engagement
    """
    spindle_speed = measurements[spindleSpeedIdentifier].to_numpy()
    spindle_current = measurements[spindleCurrentIdentifier].to_numpy()
    time = measurements[timeIdentifier].to_numpy()
    spindle_speed_intervals = determine_milling_time_intervals(spindle_speed, 5.5)
    spindle_speed_intervals, interval_means = fix_milling_time_intervals(spindle_speed, spindle_speed_intervals)
    # return variable - engagements array (process)
    engagements = np.empty(0, dtype=int)

    # remove all intervals with a median below limit
    means = np.array(interval_means)
    candidates = np.array(spindle_speed_intervals)
    remove_indices = np.where(means < mean_limit)  # removal condition
    # removal of unfit means and candidates
    means = np.delete(means, remove_indices)  # apply removal
    candidates = np.delete(candidates, remove_indices, 0)

    # filter spindle current
    spindle_current = signal.savgol_filter(spindle_current, 51, 1)

    # iterate interval candidates
    for candidate in candidates:
        # call function to calculate engagement
        a, b = candidate[0], candidate[1]
        engagement = milling_engagement(spindle_current, (a, b), step=step)
        # append found engagements to result
        engagements = np.concatenate((engagements, engagement))

    results = []
    start_bounds = []
    end_bounds = []
    startEng = []
    endEng = []

    changeEng = np.diff(engagements) > 1
    nEng = np.count_nonzero(changeEng)
    if (nEng > 0):
        startEng = np.insert(changeEng, 0, True)
    startEng = engagements[startEng]
    if (nEng > 0):
        endEng = np.append(changeEng, True)
    endEng = engagements[endEng]
    if (nEng > 0):
        if engagements[0] > 0:
            start_bounds.append((time[0]).to_pydatetime())
            end_bounds.append((time[engagements[0]]).to_pydatetime())
            results.append({"bool_engagement": False, "int_engagement": 0})

        print(f"{(time[0]).to_pydatetime()}-->{(time[engagements[0]]).to_pydatetime()} FALSE")

    for i in range(nEng):
        # Im Eingriff
        start_bounds.append((time[startEng[i]]).to_pydatetime())
        end_bounds.append((time[endEng[i]]).to_pydatetime())
        print(f"{(time[startEng[i]]).to_pydatetime()}-->{(time[endEng[i]]).to_pydatetime()} TRUE")
        results.append({"bool_engagement": True, "int_engagement": 1})
        # Nicht im Eingriff
        start_bounds.append((time[endEng[i]]).to_pydatetime())
        if i < nEng:
            end_bounds.append((time[startEng[i + 1]]).to_pydatetime())
        print(f"{(time[endEng[i]]).to_pydatetime()}-->{(time[startEng[i + 1]]).to_pydatetime()} FALSE")
        results.append({"bool_engagement": False, "int_engagement": 0})

    # end_bounds.append((time[-1]).to_pydatetime())

    # return filtered spindle current and detected engagements    
    return start_bounds, end_bounds, results


