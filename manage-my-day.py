print("Welcome to 'Manage My Time'! Let's build your ultimate schedule for this upcoming week.")

print("Let's begin with your school schedule.")

days_of_the_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

layout_of_week = dict()

for i in days_of_the_week:
    
    layout_of_school_day = []
    print("Let's look at",i+".")
    
    class_number = int(input("How many classes do you have on that day?\nNumber of classes: "))
    
    for n in range(class_number):
    
        name_of_class = input("What is the name of your class?\nClass: ")
    
        start_time = input("What time does it start? (ex: 16:00)\nTime: ")
        transform_start = start_time.split(':')
        start_time_minutes = int(transform_start[0])*60+int(transform_start[1])
    
        end_time = input("What time does it end? (ex: 16:00)\nTime: ")
        transform_end = end_time.split(':')
        end_time_minutes = int(transform_end[0])*60+int(transform_end[1])
    
        interval_of_time = [start_time_minutes,end_time_minutes]
        layout_of_school_day.append(interval_of_time)
        
    layout_of_week[i] = layout_of_school_day
    
work = input("Do you work?\nYes or no: ")

if work.lower() == 'yes':

    print("Now let's take a look at your work schedule.")

    for i in days_of_the_week:
    
        layout_of_work_day = []
        print("Let's look at",i+".")
    
        shift_number = int(input("How many shifts do you have on that day?\nNumber of shifts: "))
    
        for n in range(shift_number):
    
            print("For shift",i+":")
            start_time = input("What time does it start? (ex: 16:00)\nTime: ")
            transform_start = start_time.split(':')
            start_time_minutes = int(transform_start[0])*60+int(transform_start[1])
    
            end_time = input("What time does it end? (ex: 16:00)\nTime: ")
            transform_end = end_time.split(':')
            end_time_minutes = int(transform_end[0])*60+int(transform_end[1])
    
            interval_of_time = [start_time_minutes,end_time_minutes]
            layout_of_work_day.append(interval_of_time)
        
        layout_of_week[i] += layout_of_work_day
        
print("Let's take note of extracurriculars or other events.")

add_another = input("Would you like to add one? Yes or no: ")

if add_another.lower() == "yes":
    while add_another.lower() == "yes": 
    
        layout_of_event = []
        day_of_week = input("Which day of the week does it take place? (ex: Tuesday) ")
        name_of_event = input("What's the name of the event? ")
    
        start_time = input("What time does it start? (ex: 16:00)\nTime: ")
        transform_start = start_time.split(':')
        start_time_minutes = int(transform_start[0])*60+int(transform_start[1])
    
        end_time = input("What time does it end? (ex: 16:00)\nTime: ")
        transform_end = end_time.split(':')
        end_time_minutes = int(transform_end[0])*60+int(transform_end[1])
    
        interval_of_time = [start_time_minutes,end_time_minutes]
        layout_of_event.append(interval_of_time)

        add_another = input("Would you like to add another? Yes or no: ")


    layout_of_week[day_of_week] += layout_of_event
    
print(layout_of_week)

#Calculate free time

layout_of_week_free = dict()
for day in layout_of_week:
    if layout_of_week[day] != []:

        layout_of_day_free = []
        busy_hours = layout_of_week.get(day)
        first_interval = [0,busy_hours[0][0]]
        layout_of_day_free.append(first_interval)
        
        if len(busy_hours) > 1:
    
            for hours in range(1,len(busy_hours)):
                interval = [busy_hours[hours-1][1],busy_hours[hours][0]]
                layout_of_day_free.append(interval)
        
        last_interval = [busy_hours[-1][1], 1440]
        layout_of_day_free.append(last_interval)
        layout_of_week_free[day] = layout_of_day_free
        
    else:
        layout_of_week_free[day] = [[0, 1440]]
            
print(layout_of_week_free)

    



            
        
        



    

    
    
