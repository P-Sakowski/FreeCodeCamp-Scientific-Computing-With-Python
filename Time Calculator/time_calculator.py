def add_time(start, duration, startingDay = ""):

  weekdays = {
    0: "sunday",
    1: "monday",
    2: "tuesday",
    3: "wednesday",
    4: "thursday",
    5: "friday",
    6: "saturday"
  }

  def getDurationMinutes(duration):
    durationHours = int(duration.split(":")[0]) + int(int(duration.split(":")[1])/60)
    durationMinutes = int(duration.split(":")[1]) % 60 
    result = (durationHours * 60) + durationMinutes
    return result

  durationTotalMinutes = getDurationMinutes(duration)

  #convert start date to 24h format
  startSplitted = start.split()
  startHour = int(startSplitted[0].split(":")[0])
  if(startSplitted[1] == "PM"):
    startHour += 12
  startMinute = int(startSplitted[0].split(":")[1])
  
  #add minutes of duration to start date, change time sufix if necessary
  timeType = "AM"
  finalMinute = (startMinute + durationTotalMinutes) % 60
  finalHour = ((startHour + int((startMinute + durationTotalMinutes) / 60)) % 24)
  if(finalHour / 12 > 1):
    finalHour -= 12
    timeType = "PM"
  elif(finalHour == 12):
    timeType = "PM"
  elif(finalHour == 0):
    finalHour = 12
    timeType = "AM"

  #count days of difference between dates
  daysDiffText = ""
  totalMinutes = startHour * 60 + startMinute + durationTotalMinutes
  daysDiff = int(totalMinutes / 1440)
  if(daysDiff == 1):
    daysDiffText = " (next day)"
  elif(daysDiff > 1):
    daysDiffText = " (" + str(daysDiff) + " days later)"

  #add weekday's name if necessary
  if(startingDay != ""):
    startingDayNumber = list(weekdays.keys())[list(weekdays.values()).index(startingDay.lower())]
    endDayNumber = int(startingDayNumber + daysDiff) % 7
    endDayText = ", " + weekdays[endDayNumber].capitalize()
  else:
    endDayText = ""
  
  new_time = (f'{finalHour}:{finalMinute:02} {timeType}{endDayText}{daysDiffText}')
  return new_time