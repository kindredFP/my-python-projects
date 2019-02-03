import logging

# standard logging config; you can just add filename=myFilename.log before level
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

# uncomment next statement to turn on/off logging quickly
# logging.disable(logging.CRITICAL)

logging.debug("Starting to log")
try:
    raise Exception('Forcing to throw an exception')

except ValueError:
    print("This is capturing a specific Value Error")
    # if the error goes here then it will log critical which will affect the logging enablement on line 7
    logging.critical("This is a critical error")

except:
    print("the error is consumed, this is the catch all")

print('*****')
denominator = 0

if denominator == 0:
    try:
        answer = 10 / denominator
    except ZeroDivisionError:
        print("You cant divide by 0")
        answer = 0

print(answer)

logging.debug("End of log")
