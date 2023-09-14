import time, pydualsense


ds = pydualsense.pydualsense() # initialize pydualsense library

controller_connected = False

while not controller_connected:
    try:
        ds.init() # connect to and initialize controller
        print("Controller found!")
        controller_connected = True
    except:
        print("Controller not found, searching again...")
        time.sleep(1)
        


press_count = 0

def cross_counter(state): # event function counting presses
    global press_count
    if state:
        #print(f"Cross: {state}")
        press_count += 1


def cross_cps_test(seconds:int):  
    global press_count
    press_count = 0 # Reset counter
    
    print("Recording presses...")
    
    time.sleep(seconds) # pause for seconds amount of time
    
    cps = press_count / seconds # calculate cps
    print(f"Done! You achieved {round(cps,2)} clicks per second")
        


ds.cross_pressed += cross_counter # create event handler for cross button presses



has_printed = False
while not ds.state.R1: # Run program until R1 is pressed
    
    if not has_printed:
        print("Press 'SQUARE' to initiate CPS test \nPress 'R1' to exit program")
        has_printed = True
    
    if ds.state.square:
        cross_cps_test(3)
        has_printed = False
    
    

print("Exiting program!")
time.sleep(1)
ds.close() # close controller device


