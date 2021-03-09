'''by bus'''
stop_by_bus=10*2
speed=25/60
distance=4
time=distance/speed
print('time taken by bus',time)
totaltime=time+stop_by_bus
print('total time to reach the university is',totaltime)
#time taken while jogging
distance_for_first_mile=1
speed1=7/60
first_one_mile=distance_for_first_mile/speed
print('time taken for first mile is',first_one_mile)
distance_for_second_and_third_mile=2
speed2=15/60
second_and_third_mile=distance_for_second_and_third_mile/speed2
print('time taken in second and third mile is',second_and_third_mile)
distance_for_last_mile=1
speed3=7/60
last_mile=distance_for_last_mile/speed3
print('time taken in last minute is',last_mile)
total_time_taken_while_jogging=first_one_mile+second_and_third_mile+last_mile
print('the total time taken while jogging is',total_time_taken_while_jogging)

if total_time_taken_while_jogging<totaltime:
    print('going through bus is faster')
else:
    print('jogging is faster than going through bus')

