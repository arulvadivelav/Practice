import time
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_result


# Retry function only execute for the below
def retry_for(response):
    return response == 500

# Decorate the function you want to apply retry logic to
@retry(retry=retry_if_result(retry_for), stop=stop_after_attempt(3), wait=wait_fixed(2))
def do_something_unreliable():
    try:
        for i in range(0,10):
            if i==7:
                print("Exeception")
                raise Exception("Failed xxxxxxxxxxxxxxx")
            print("True")
        return 200
    except:
        return 500

# Function will retry up to 3 times with a 2-second delay between each attempt
message = do_something_unreliable()
print(message)
