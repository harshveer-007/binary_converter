# What if implementing binary to decimal conversion and then implementing binary to decimal 

# I feel like binary to decimal conversion would be much easier than the latter
# So I am about to try binary to decimal conversion 

def main():
    binary = list(input("Enter a binary number: "))
    return_value = check_binary(binary)
    if return_value == True:
        print(conversion_to_decimal(binary))
    else:
        print(return_value)

# This checks whether the user entered a valid binary input though its still not comprehensive and might skip those corner cases.
def check_binary(binary):
    for bit in binary:
        if int(bit) > 1:
            return "Not a valid binary number!"

    return True

# Sucessfully converts the binary to decimal though I fell something is lacking, I don't feel somewhat satisfied with my code. It does the job but I think somethins is
# missing and it could do more.
def conversion_to_decimal(binary):
    conversion = 0
    power = len(binary) - 1
    for bit in binary:
        conversion = conversion + (int(bit) * (2 ** power))
        power = power - 1
    
    return conversion

if __name__ == "__main__":
    main()

# As I expected the code works, and this is a great feat since I have been struggling with converting decimal to binary, and I never thought of doing the opposite. 
# The opposite was way simpler and I could easily come up with a working algorithm and put the logic to practice.
# Now I thought "If I could convert the binary to decimal, what if I make a machine that constantly creates binary numbers and also their decimal counterparts."
# This thought has a problem though how do I know the pattern of binary numbers, and I think this is where gray code might come in handy
# Again I have the tools but implementing the logic and making a working algorithm out of seems the difficult task. 
# Anyways this is my next step to binary conveter and my second working prototype.

# Next goal is to convert decimal to binary.
      
