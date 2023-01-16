#	Astrological Sign
#https://open.kattis.com/problems/astrologicalsign

from datetime import datetime

def datetimeFromDate(date):
    return datetime.strptime(date + " 2020", "%d %b %Y")

aq = datetimeFromDate("21 Jan")
pi = datetimeFromDate("20 Feb")
ar = datetimeFromDate("21 Mar")
ta = datetimeFromDate("21 Apr")
ge = datetimeFromDate("21 May")
ca = datetimeFromDate("22 Jun")
le = datetimeFromDate("23 Jul")
vir = datetimeFromDate("23 Aug")
lib = datetimeFromDate("22 Sep")
sco = datetimeFromDate("23 Oct")
sag = datetimeFromDate("23 Nov")
cap = datetimeFromDate("22 Dec")

numberOfDates = int(input())
for _ in range(numberOfDates):
    date = datetimeFromDate(input())
    if aq <= date < pi:
        print("Aquarius")
    elif pi <= date < ar:
        print("Pisces")
    elif ar <= date < ta:
        print("Aries")
    elif ta <= date < ge:
        print("Taurus")
    elif ge <= date < ca:
        print("Gemini")
    elif ca <= date < le:
        print("Cancer")
    elif le <= date < vir:
        print("Leo")
    elif vir <= date < lib:
        print("Virgo")
    elif lib <= date < sco:
        print("Libra")
    elif sco <= date < sag:
        print("Scorpio")
    elif sag <= date < cap:
        print("Sagittarius")
    else:
        print("Capricorn")
