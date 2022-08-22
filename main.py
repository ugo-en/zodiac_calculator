"""
This is a simple app to calculate your zodiac sign
"""

# Create the zodiac class
class ZodiacSign:
    def __init__(self, name, start_month, start_day, end_month, end_day):
        self.name = name
        self.start_month = start_month
        self.start_day = start_day
        self.end_month = end_month
        self.end_day = end_day
    
    def check(self,month,day):
        """
        This is the method that confirms if the month and day provided fall within its timeframe
        :param month:
        :param day:
        """
        return (month == self.start_month and day >= self.start_day) or (month == self.end_month and day <= self.end_day)

# create the zodiac objects
aries = ZodiacSign("Aries",3,21,4,19)
taurus = ZodiacSign("Taurus",4,20,5,20)
gemini = ZodiacSign("Gemini",5,21,6,20)
cancer = ZodiacSign("Cancer",6,21,7,22)
leo = ZodiacSign("Leo",7,23,8,22)
virgo = ZodiacSign("Virgo",8,23,9,22)
libra = ZodiacSign("Libra",9,23,10,22)
scorpio = ZodiacSign("Scorpio",10,23,11,21)
sag = ZodiacSign("Sagittarius",11,22,12,21)
cap = ZodiacSign("Capricorn",12,22,1,19)
aquarius = ZodiacSign("Aquarius",1,20,2,18)
pisces = ZodiacSign("Pisces",2,19,3,20)

# put them in the list
zodiacs = [aries,taurus,gemini,cancer,leo,virgo,libra,scorpio,sag,cap,aquarius]

# Welcome message
print("WELCOME TO MY ZODIAC CALCULATOR")

#  accept input
month = int(input("What month were you born in? (1-12): "))
day = int(input("What day of the month were you born in? (1-31): "))

# check each zodiac
for zodiac in zodiacs:
    if zodiac.check(month,day):
        print(f"You are a/an {zodiac.name}")
        break
        
    
