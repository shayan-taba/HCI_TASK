"""
Blood Pressure Checker For Elderly When Input Is Given

Returns:
    STRING: resturs a string either indicating the input is invalid (abnormal, out of range) or your pressure to normal, low or high
"""

# Define acceptable ranges for SYSTOLIC and DIASTOLIC pressures

NORMAL_MAXIMUM_SYSTOLIC = 129  # This is the maximum (inclusive) SYSTOLIC pressure in mm Hg that can be considered "normal" or "elevated" based on official guidelines
LOW_MAXIMUM_SYSTOLIC = 89  # This is the maximum (inclusive) SYSTOLIC pressure in mm Hg that can be considered "low" based on official guidelines
MINIMUM_SYSTOLIC = 50  # This is the minimum (inclusive) SYSTOLIC pressure in mm Hg accepted by the system. It is otherwise known as EXTREME data and is near the BOUNDARY data.
MAXIMUM_SYSTOLIC = 250  # This is the maximum (inclusive) SYSTOLIC pressure in mm Hg accepted by the system. It is otherwise known as EXTREME data and is near the BOUNDARY data.


NORMAL_MAXIMUM_DIASTOLIC = 79  # This is the maximum (inclusive) DIASTOLIC pressure in mm Hg that can be considered "normal" or "elevated" based on official guidelines
LOW_MAXIMUM_DIASTOLIC = 59  # This is the maximum (inclusive) DIASTOLIC pressure in mm Hg that can be considered "low" based on official guidelines
MINIMUM_DIASTOLIC = 30  # This is the minimum (inclusive) SYSTOLIC pressure in mm Hg accepted by the system. It is otherwise known as EXTREME data and is near the BOUNDARY data.
MAXIMUM_DIASTOLIC = 150  # This is the maximum (inclusive) SYSTOLIC pressure in mm Hg accepted by the system. It is otherwise known as EXTREME data and is near the BOUNDARY data.


# Function to validate if input is a valid integer, but does not consider the numerical range of accepted values
def validateInput(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isnumeric():
            return int(user_input)
        else:
            print("Invalid input. Please enter a valid blood pressure (positive integer).")


def getInput():
    # Input SYSTOLIC and DIASTOLIC blood pressure values from the user
    SYSTOLIC = validateInput(
        "Enter your top number (SYSTOLIC blood pressure in mm Hg: "
    )
    DIASTOLIC = validateInput(
        "Enter your bottom number (DIASTOLIC) blood pressure in mm Hg: "
    )

    return SYSTOLIC, DIASTOLIC


def checkInputIfRejectable(SYSTOLIC, DIASTOLIC):
    # Check if SYSTOLIC or DIASTOLIC is within acceptable range
    if (
        SYSTOLIC > MAXIMUM_SYSTOLIC
        or SYSTOLIC < MINIMUM_SYSTOLIC
        or DIASTOLIC > MAXIMUM_DIASTOLIC
        or DIASTOLIC < MINIMUM_DIASTOLIC
    ):
        return "You have entered an invalid value for the blood pressure. Please confirm your pressure and try again. Accepted Range: Top number (Systolic): 50 to 250. Bottom number (Diastolic): 30 to 150."

    return False


def processInput(SYSTOLIC, DIASTOLIC, HIGH_COUNTER):
    if SYSTOLIC <= LOW_MAXIMUM_SYSTOLIC and DIASTOLIC <= LOW_MAXIMUM_DIASTOLIC:
        # This is low. Refer to the planning document for justification.
        return "Your blood pressure is low. Please contact your doctor."
    elif SYSTOLIC <= NORMAL_MAXIMUM_SYSTOLIC and DIASTOLIC <= NORMAL_MAXIMUM_DIASTOLIC:
        # This is normal, comprising of "normal" or "elevated" from the AHA guidelines. Refer to the planning document for justification.
        return "Your blood pressure is normal. No action is currently required."
    else:
        HIGH_COUNTER += 1
        if HIGH_COUNTER == 5:
            return "Your blood pressure has been high for five times in a row. Please contact your doctor."
        else:
            # This is high. It is comprised of both stages of hypertension stages and the hypertensive crisis stage.
            return "Your blood pressure is high. Rest, drink water, and retake a blood pressure test in 10 minutes."


def runChecker(HIGH_COUNTER):  # MAIN function to be invoked for the program to work
    SYSTOLIC, DIASTOLIC = getInput()  # Invokes the function to obtain the input
    rejectData = checkInputIfRejectable(SYSTOLIC, DIASTOLIC)
    if rejectData:  # Input was outside acceptabed range but it was numerical
        return rejectData
    else:  # Input was within accepted range
        return processInput(SYSTOLIC, DIASTOLIC, HIGH_COUNTER)


def reiterateChecker(HIGH_COUNTER):
    output = runChecker(HIGH_COUNTER)

    print(output)

    if "Your blood pressure is high" in output: # only triggers if blood pressure is high, but not high for five consecutive occasoins
        HIGH_COUNTER += 1
        reiterateChecker(HIGH_COUNTER)


def main():
    INITIAL_HIGH_COUNTER = 0 # initializes variable for counter of how many times the user has a high consecutive blood pressure
    reiterateChecker(INITIAL_HIGH_COUNTER)

if __name__ == "__main__":  # Only runs if the file is directly run. Ensure the program below only runs if intended.
    main()
