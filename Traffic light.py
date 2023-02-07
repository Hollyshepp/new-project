##Task 1
##colour = ''
##while colour != '4':
##    colour = input('Enter a number 1-3 ')
##    if colour == '1':
##        print('Green')
##    elif colour == '2':
##        print('Amber')
##    elif colour == '3':
##        print('Red')
##    else:
##        print('Incorrect input')
##print('Exit')

##Task 2
##Road junction with traffic lights
##lane = ''
##while lane != '0':
##    lane = input('Input lane value from 1-4 ')
##    if lane == '1' or lane == '2':
##        print('EW_road (Phase A) GREEN ')
##        print('NS_road (Phase B) RED')
##    elif lane == '3' or lane == '4':
##        print('EW_road (Phase A) RED ')
##        print('NS_road (Phase B) GREEN')
##    else:
##        print('Input error')
##print('Exit')   


##Task 3
##LAYOUT 1
##import time
##lane = ''
##while lane != '0':
##    print('Enter 0 to exit')
##    lane = input('Input lane value 1-4 ')
##    if lane == '1' or lane == '2':
##        print('EW_road (Phase A) RED ')
##        time.sleep(2)
##        print('EW_road (Phase A) RED - AMBER')
##        time.sleep(2)
##        print('EW_road (Phase A) GREEN')
##    elif lane == '3' or lane == '4':
##        print('NS_road (Phase B) RED')
##        time.sleep(2)
##        print('NS_road (Phase B) RED - AMBER')
##        time.sleep(2)
##        print('NS_road (Phase B) GREEN')
##    else:
##        print('Input error')
##print('Exit')

##LAYOUT 2
##import time
##lane = ''
##while lane != '0':
##    print('Enter 0 to exit')
##    lane = input('Input lane value 1-4 ')
##    if lane == '1' or lane == '2':
##        print('Lane 1/2: RED')
##        print('Lane 3/4: GREEN')
##        time.sleep(2)
##        print('Lane 1/2: RED - AMBER')
##        print('Lane 3/4: AMBER')
##        time.sleep(2)
##        print('Lane 1/2: AMBER')
##        print('Lane 3/4: RED-AMBER')
##        time.sleep(2)
##        print('Lane 1/2: GREEN')
##        print('Lane 3/4: RED')
##    elif lane == '3' or lane == '4':
##        print('Lane 3/4: RED')
##        print('Lane 1/2: GREEN')
##        time.sleep(2)
##        print('Lane 3/4: RED - AMBER')
##        print('Lane 1/2: AMBER')
##        time.sleep(2)
##        print('Lane 3/4: AMBER')
##        print('Lane 1/2: RED-AMBER')
##        time.sleep(2)
##        print('Lane 3/4: GREEN')
##        print('Lane 1/2: RED')
##    else:
##        print('Input error')
##print('Exit')

#LAYOUT 3
import time
lane = ''
while lane != '0':
    print('Enter 0 to exit')
    lane = input('Input lane value 1-4 ')
    if lane == '1' or lane == '2':
        print('EW_road (Phase A) RED ')
        print('NS_road (Phase B) GREEN')
        time.sleep(2)
        print('EW_road (Phase A) RED - AMBER')
        print('NS_road (Phase B) AMBER')
        time.sleep(2)
        print('EW_road (Phase A) AMBER')
        print('NS_road (Phase B) AMBER - RED')
        time.sleep(2)
        print('EW_road (Phase A) GREEN')
        print('NS_road (Phase B) RED')
    elif lane == '3' or lane == '4':
        print('NS_road (Phase B) RED')
        print('EW_road (Phase A) GREEN')
        time.sleep(2)
        print('NS_road (Phase B) RED - AMBER')
        print('EW_road (Phase A) AMBER')
        time.sleep(2)
        print('NS_road (Phase B) AMBER')
        print('EW_road (Phase A) AMBER - RED')
        time.sleep(2)
        print('NS_road (Phase B) GREEN')
        print('EW_road (Phase A) RED')
    else:
        print('Input error')
print('Exit')
quit()

##Task 4 

# yes





































