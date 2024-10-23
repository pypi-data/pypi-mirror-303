import re
import os
import pytz

from datetime import datetime, timedelta

from tzlocal import get_localzone

from .display import output_message

LUMEO_UPDATE_SCHEDULE_FILE = "/opt/lumeo/update_schedule_plan.txt"

#################################################
# Native impl based Time parser and checker functions
#################################################

def parse_time(time_str):
    # Parse time with AM/PM or without
    pattern = ['%I:%M%p', '%I:%M %p'] if ':' in time_str else ['%I%p', '%I %p']
    try:
        time = datetime.strptime(time_str, pattern[0]).time()
    except:
        time = datetime.strptime(time_str, pattern[1]).time()
    return time


def parse_date(date_str):
    # Parse date with different formats
    try:
        date = datetime.strptime(date_str, '%d/%m/%Y').date()
    except ValueError:
        try:
            date = datetime.strptime(date_str, '%Y/%m/%d').date()
        except ValueError:
            raise ValueError(f"Invalid date format. Date must be in either 'd/m/Y' or 'Y/m/d' format.")
    return date


def parse_time_range(time_range_str):
    time_ranges = []

    # Define regex patterns
    date_regex = r'\d{1,2}/\d{1,2}/\d{4}|\d{4}/\d{1,2}/\d{1,2}'
    time_regex = r'\d{1,2}:\d{2}\s?[ap]m|\d{1,2}\s?[ap]m'
    day_regex = r'monday|tuesday|wednesday|thursday|friday|saturday|sunday|weekdays|weekends'

    # Find matches
    dates = re.findall(date_regex, time_range_str, re.IGNORECASE)
    times = re.findall(time_regex, time_range_str, re.IGNORECASE)
    days = re.findall(day_regex, time_range_str, re.IGNORECASE)

    # Check if explicit dates are provided
    if dates:
        raise ValueError("Explicit dates are not supported in time ranges.")

    # Convert dates and times
    dates = [parse_date(date) if date else None for date in dates]
    times = [parse_time(time) for time in times]

    # Check if there's no end time specified
    if len(times) == 1:
        times.append(datetime.strptime('2359', '%H%M').time())  # Default end time to 11:59 PM

    # Prepare the result
    if days and (days[0] == 'weekdays' or days[0] == 'weekends'):
        # Substitute weekdays with monday-friday and weekends with saturday-sunday
        substitute_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday'] if days[0] == 'weekdays' else [
            'saturday', 'sunday']
        for day in substitute_days:
            time_range = {
                'start_date': None,
                'end_date': None,
                'start_dow': day,
                'end_dow': None,
                'start_time': times[0] if times else None,
                'end_time': times[1] if len(times) > 1 else None
            }
            validate_time_range(time_range, time_range_splitted=False)
            time_ranges.append(time_range)
    elif not (days or dates) and len(times) > 1 and times[0] > times[1]:
        # If no days or dates are specified, and the start time is after the end time,
        # then the time range spans midnight. Split it into two time ranges.

        # Check if the time range covers at least a 2-hour interval before we split it into two time ranges
        # Convert times to datetime objects
        start_time_dt = datetime.combine(datetime.min, times[0])
        end_time_dt = datetime.combine(datetime.min, times[1])

        # Adjust end time if it's on the next day
        if times[0] > times[1]:
            end_time_dt += timedelta(days=1)  # Add 1 day to end time

        # Calculate time difference in minutes
        time_diff_minutes = abs((end_time_dt - start_time_dt).total_seconds()) / 60

        if time_diff_minutes < 120:  # 2 hours
            raise ValueError("Time range must cover at least a 2-hour interval.")

        time_range = {
            'start_date': None,
            'end_date': None,
            'start_dow': None,
            'end_dow': None,
            'start_time': times[0],
            'end_time': datetime.strptime('2359', '%H%M').time()
        }
        validate_time_range(time_range, time_range_splitted=True)
        time_ranges.append(time_range)
        time_range = {
            'start_date': None,
            'end_date': None,
            'start_dow': None,
            'end_dow': None,
            'start_time': datetime.strptime('0000', '%H%M').time(),
            'end_time': times[1]
        }
        validate_time_range(time_range, time_range_splitted=True)
        time_ranges.append(time_range)
    else:
        time_range = {
            'start_date': dates[0] if dates else None,
            'end_date': dates[1] if len(dates) > 1 else None,
            'start_dow': days[0] if days else None,
            'end_dow': days[1] if len(days) > 1 else None,
            'start_time': times[0] if times else None,
            'end_time': times[1] if len(times) > 1 else None
        }
        validate_time_range(time_range, time_range_splitted=False)
        time_ranges.append(time_range)

    return time_ranges


def validate_time_range(time_range, time_range_splitted=False):
    # Check that result contains at least a start time.
    if not time_range['start_time']:
        raise ValueError("Start time must be specified.")

    # Check that result either contains days of the week or dates or neither. You can't mix DOW and dates.
    if (time_range['start_dow'] or time_range['end_dow']) and (time_range['start_date'] or time_range['end_date']):
        raise ValueError("Cannot mix days of the week with explicit dates.")

    # Check that end is not specified without start
    if (not time_range['start_dow'] and time_range['end_dow']) or (
            not time_range['start_date'] and time_range['end_date']):
        raise ValueError("Cannot specify end day/date without start.")

    # Check if start day/date/time is before the end/day/date/time when both are specified
    if time_range['start_date'] and time_range['end_date']:
        if time_range['start_date'] > time_range['end_date']:
            raise ValueError("Start date must be on or before the end date.")

    if (not time_range['start_dow'] and not time_range['start_date']) and \
            time_range['start_time'] and time_range['end_time'] and \
            time_range['start_time'] > time_range['end_time']:
        raise ValueError("Start time must be on or before the end time when dates / day of week are not specified.")

    # Check if the time range covers at least a 2-hour interval
    if not time_range_splitted and time_range.get('start_time') and time_range.get('end_time'):
        if time_range['start_dow'] and time_range['end_dow'] and time_range['start_dow'] != time_range['end_dow']:
            start_dow = datetime.strptime(time_range['start_dow'], '%A').date()
            end_dow = datetime.strptime(time_range['end_dow'], '%A').date()

            # If start and end days are different, we need to calculate the time difference considering both days
            start_time_minutes = time_range['start_time'].hour * 60 + time_range['start_time'].minute
            end_time_minutes = time_range['end_time'].hour * 60 + time_range['end_time'].minute

            # Calculate the time difference within the same day
            same_day_diff = (24 * 60) - abs(end_time_minutes - start_time_minutes)

            # Calculate the time difference across multiple days
            across_days_diff = (end_dow - start_dow).days * 24 * 60

            # Final time difference is the sum of both
            time_diff_minutes = same_day_diff + across_days_diff

            if time_diff_minutes < 120:
                raise ValueError("Time range must cover at least a 2-hour interval.")
        else:
            time_diff_minutes = abs((time_range['end_time'].hour * 60 + time_range['end_time'].minute) -
                                    (time_range['start_time'].hour * 60 + time_range['start_time'].minute))
            if time_diff_minutes < 120:  # 2 hours
                raise ValueError(f"Time range must cover at least a 2-hour interval.")

    return True


def is_datetime_in_range(time_range, now, tz, debug=False):
    # Convert day of week to date if needed
    if time_range['start_dow']:
        dow_mapping = {
            "monday": 0, "tuesday": 1, "wednesday": 2,
            "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6
        }

        # Adjust dates to the nearest matching day of the week
        start_dow_offset = dow_mapping[time_range['start_dow']] - now.weekday()
        end_dow_offset = dow_mapping[time_range['end_dow']] - now.weekday() if time_range[
            'end_dow'] else start_dow_offset

        if end_dow_offset < start_dow_offset:
            if end_dow_offset == 0:
                start_dow_offset -= 7
            elif start_dow_offset == 0:
                end_dow_offset += 7
            else:
                end_dow_offset += 7

        start_date = now.date() + timedelta(days=start_dow_offset)
        end_date = now.date() + timedelta(days=end_dow_offset)

    # Use provided dates if available
    else:
        start_date = time_range['start_date'] if time_range['start_date'] else now.date()
        end_date = time_range['end_date'] if time_range['end_date'] else start_date

    # Handle time span across days
    end_time = time_range['end_time'] if time_range['end_time'] else time_range['start_time']
    start_datetime = tz.localize(datetime.combine(start_date, time_range['start_time']))
    end_datetime = tz.localize(datetime.combine(end_date, end_time))

    # Adjust for end time earlier than start time
    if (not (time_range['end_date'] or time_range['end_dow'])) and \
            time_range['start_time'] and time_range['end_time'] and \
            time_range['start_time'] > time_range['end_time']:
        end_datetime += timedelta(days=1)

    result = start_datetime <= now <= end_datetime

    if debug:
        print(f"[{result}] {time_range} : {start_datetime} - {now} - {end_datetime}\n")

    return result


def check_update_schedule():
    try:
        if not os.path.exists(LUMEO_UPDATE_SCHEDULE_FILE):
            return True  # Early return if the file doesn't exist

        with open(LUMEO_UPDATE_SCHEDULE_FILE, "r") as file:
            schedule_plan = file.read()
            if schedule_plan:
                local_timezone = pytz.timezone(datetime.now(tz=get_localzone()).strftime('%Z'))

                for time_range_str in schedule_plan.split(","):
                    parsed_time_ranges = parse_time_range(time_range_str.lower())
                    if parsed_time_ranges:
                        time_ranges = parsed_time_ranges
                        # Are we at or within the specified time range ?
                        if time_ranges:
                            time_range_result = False
                            now = datetime.now(local_timezone)

                            for time_range in time_ranges:
                                time_range_result = is_datetime_in_range(time_range, now,
                                                                         local_timezone) or time_range_result
                                if time_range_result:
                                    return True
                output_message("[lumeo-container-update] Current time outside update schedule. Skipping update.",
                               "info")
                return False
    except Exception as err:
        output_message("Update Schedule file does not exist or has wrong format. "
                       "Will proceed with update check. Exception: {}".format(err), "error")

    return True


def edit_update_schedule():
    if os.path.exists(LUMEO_UPDATE_SCHEDULE_FILE):
        # Print the current schedule
        with open(LUMEO_UPDATE_SCHEDULE_FILE, "r") as file:
            schedule = file.read().strip()  # Read file content and remove leading/trailing whitespace
            print("Current update schedule:", schedule)
    else:
        print("No update schedule found.")

    while True:
        try:
            user_input = input("\nEnter the update schedule or write 'remove' to delete existing.\n\n"
                               "Format: [day of week | weekdays | weekends] start time - end time\n"
                               "Example: friday 10am - 6pm or weekdays 12am - 3am\n")

            if user_input.strip().lower() == "":
                # Break the loop if the input is empty
                print("Returning to the main menu, no changes were applied to the Update Schedule")
                break

            if user_input.strip().lower() == "remove":
                # Remove the schedule file if it exists
                if os.path.exists(LUMEO_UPDATE_SCHEDULE_FILE):
                    os.remove(LUMEO_UPDATE_SCHEDULE_FILE)
                    print("Update schedule removed.")
                else:
                    print("No update schedule to remove.")
                break
            else:
                # Parse the update schedule string to check for valid time ranges
                for time_range_str in user_input.split(","):
                    parse_time_range(time_range_str.lower())

                # Write the schedule line to the file
                with open(LUMEO_UPDATE_SCHEDULE_FILE, "w") as file:
                    file.write(user_input.strip())
                print("Update schedule successfully saved.")
                break
        except Exception as error:
            output_message(f"Invalid update schedule format, please retry! Exception: {error}", "error")


def save_update_schedule_from_env():
    # Store the contents of LUMEO_UPDATE_SCHEDULE environment variable to file
    update_schedule = os.getenv("LUMEO_UPDATE_SCHEDULE")
    if update_schedule:
        try:
            # Parse the update schedule string to check for valid time ranges
            for time_range_str in update_schedule.split(","):
                parse_time_range(time_range_str.lower())

            if not os.path.exists("/opt/lumeo"):
                os.makedirs("/opt/lumeo")

            # Write the update schedule info to file
            with open(LUMEO_UPDATE_SCHEDULE_FILE, "w") as file:
                file.write(update_schedule)
        except Exception as error:
            output_message(f"Error storing update schedule. Exception: {error}", "error")    