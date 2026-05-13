import math 
from log import log_info, log_warning, log_error



def calculate_square_root(numbers: list) -> None:
    for number in numbers:
        try:
            if number < 0:
                #Logging of negative figure warning
                log_warning(f"Negative figure found {number}. Skip")
                continue
            root = math.sqrt(number)
            log_info(f"Square root of {number} is {root:.2f}")
        
        except Exception as e:
            #Logging of any other exception
            log_error(f"Issue calculating square root for {number}: {e}")
if __name__ == "__main__":
    numbers = [16, -4, 9, 25, 0, 4, "16"] 
    calculate_square_root(numbers)       