from zxcvbn import zxcvbn

def analyze_password(password):

    result = zxcvbn(password)

    score = result["score"]
    guesses = result["guesses"]

    crack_times = result["crack_times_display"]

    feedback = result["feedback"]

    return {
        "score": score,
        "guesses": guesses,
        "crack_times": crack_times,
        "feedback": feedback
    }