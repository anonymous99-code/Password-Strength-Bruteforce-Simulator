import time

def simulate_attack(target_password, wordlist_path):

    attempts = 0

    start_time = time.time()

    try:

        with open(wordlist_path, "r") as file:

            passwords = file.readlines()

        for password in passwords:

            password = password.strip()

            attempts += 1

            if password == target_password:

                end_time = time.time()

                return {
                    "success": True,
                    "password": password,
                    "attempts": attempts,
                    "time": round(end_time - start_time, 4)
                }

        end_time = time.time()

        return {
            "success": False,
            "attempts": attempts,
            "time": round(end_time - start_time, 4)
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }