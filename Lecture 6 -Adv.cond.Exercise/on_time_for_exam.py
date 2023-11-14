hour_of_exam = int(input())
minute_of_exam = int(input())
arrival_hour =  int(input())
arrival_minute = int(input())

exam_time = hour_of_exam* 60 + minute_of_exam
arrival_time = arrival_hour * 60 + arrival_minute


if exam_time - 30 <= arrival_time <= exam_time:
    print("On time")
elif exam_time - 30 > arrival_time:
    print("Early")
elif arrival_time > exam_time:
    print("Late")

difference = abs(exam_time-arrival_time)
hours = difference // 60
minutes = difference % 60


if exam_time - 60 < arrival_time < exam_time:
    print(f"{minutes} minutes before the start")
elif arrival_time <= exam_time - 60:
    print(f"{hours}:{minutes:02d} hours before the start")
elif arrival_time >= exam_time + 60:
    print(f"{hours}:{minutes:02d} hours after the start" )
elif exam_time < arrival_time < exam_time +60:
    print(f"{minutes} minutes after the start")

