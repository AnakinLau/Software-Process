import datetime
import calendar
import conversionHelper as CH

def predictHelper():

    # Helper Classes Specifically for Predict()
    def createStarDict():

        starDict = {
            'Alpheratz': {'SHA': '357d41.7', 'declination': '29d10.9'},
            'Ankaa': {'SHA': '353d14.1', 'declination': '-42d13.4'},
            'Schedar': {'SHA': '349d38.4', 'declination': '56d37.7'},
            'Diphda': {'SHA': '348d54.1', 'declination': '-17d54.1'},
            'Achernar': {'SHA': '335d25.5', 'declination': '-57d09.7'},
            'Hamal': {'SHA': '327d58.7', 'declination': '23d32.3'},
            'Polaris': {'SHA': '316d41.3', 'declination': '89d20.1'},
            'Akamar': {'SHA': '315d16.8', 'declination': '-40d14.8'},
            'Menkar': {'SHA': '314d13.0', 'declination': '4d09.0'},
            'Mirfak': {'SHA': '308d37.4', 'declination': '49d55.1'},
            'Aldebaran': {'SHA': '290d47.1', 'declination': '16d32.3'},
            'Rigel': {'SHA': '281d10.1', 'declination': '-8d11.3'},
            'Capella': {'SHA': '280d31.4', 'declination': '46d00.7'},
            'Bellatrix': {'SHA': '278d29.8', 'declination': '6d21.6'},
            'Elnath': {'SHA': '278d10.1', 'declination': '28d37.1'},
            'Alnilam': {'SHA': '275d44.3', 'declination': '-1d11.8'},
            'Betelgeuse': {'SHA': '270d59.1', 'declination': '7d24.3'},
            'Canopus': {'SHA': '263d54.8', 'declination': '-52d42.5'},
            'Sirius': {'SHA': '258d31.7', 'declination': '-16d44.3'},
            'Adara': {'SHA': '255d10.8', 'declination': '-28d59.9'},
            'Procyon': {'SHA': '244d57.5', 'declination': '5d10.9'},
            'Pollux': {'SHA': '243d25.2', 'declination': '27d59.0'},
            'Avior': {'SHA': '234d16.6', 'declination': '-59d33.7'},
            'Suhail': {'SHA': '222d50.7', 'declination': '-43d29.8'},
            'Miaplacidus': {'SHA': '221d38.4', 'declination': '-69d46.9'},
            'Alphard': {'SHA': '217d54.1', 'declination': '-8d43.8'},
            'Regulus': {'SHA': '207d41.4', 'declination': '11d53.2'},
            'Dubhe': {'SHA': '193d49.4', 'declination': '61d39.5'},
            'Denebola': {'SHA': '182d31.8', 'declination': '14d28.9'},
            'Gienah': {'SHA': '175d50.4', 'declination': '-17d37.7'},
            'Acrux': {'SHA': '173d07.2', 'declination': '-63d10.9'},
            'Gacrux': {'SHA': '171d58.8', 'declination': '-57d11.9'},
            'Alioth': {'SHA': '166d19.4', 'declination': '55d52.1'},
            'Spica': {'SHA': '158d29.5', 'declination': '-11d14.5'},
            'Alcaid': {'SHA': '152d57.8', 'declination': '49d13.8'},
            'Hadar': {'SHA': '148d45.5', 'declination': '-60d26.6'},
            'Menkent': {'SHA': '148d05.6', 'declination': '-36d26.6'},
            'Arcturus': {'SHA': '145d54.2', 'declination': '19d06.2'},
            'Rigil Kent.': {'SHA': '139d49.6', 'declination': '-60d53.6'},
            'Zubenelg.': {'SHA': '137d03.7', 'declination': '-16d06.3'},
            'Kochab': {'SHA': '137d21.0', 'declination': '74d05.2'},
            'Alphecca': {'SHA': '126d09.9', 'declination': '26d39.7'},
            'Antares': {'SHA': '112d24.4', 'declination': '-26d27.8'},
            'Atria': {'SHA': '107d25.2', 'declination': '-69d03.0'},
            'Sabik': {'SHA': '102d10.9', 'declination': '-15d44.4'},
            'Shaula': {'SHA': '96d20.0', 'declination': '-37d06.6'},
            'Rasalhague': {'SHA': '96d05.2', 'declination': '12d33.1'},
            'Etamin': {'SHA': '90d45.9', 'declination': '51d29.3'},
            'Kaus Aust.': {'SHA': '83d41.9', 'declination': '-34d22.4'},
            'Vega': {'SHA': '80d38.2', 'declination': '38d48.1'},
            'Nunki': {'SHA': '75d56.6', 'declination': '-26d16.4'},
            'Altair': {'SHA': '62d06.9', 'declination': '8d54.8'},
            'Peacock': {'SHA': '53d17.2', 'declination': '-56d41.0'},
            'Deneb': {'SHA': '49d30.7', 'declination': '45d20.5'},
            'Enif': {'SHA': '33d45.7', 'declination': '9d57.0'},
            'Alnair': {'SHA': '27d42.0', 'declination': '-46d53.1'},
            'Fomalhaut': {'SHA': '15d22.4', 'declination': '-29d32.3'},
            'Scheat': {'SHA': '13d51.8', 'declination': '28d10.3'},
            'Markab': {'SHA': '13d36.7', 'declination': '15d17.6'}
        }
        return starDict


    def checkBodyFormat(body):
        starDict = createStarDict()
        if(not(body.title() in starDict)):
            return False
        else:
            return True


    def checkDateFormat(dateInput):
        try:
            dateObj = datetime.datetime.strptime(dateInput, '%Y-%m-%d')
            if(dateObj.year > 2000):
                return True
            else:
                return False
        except ValueError:
            return False

    def checkTimeFormat(timeInput):
        try:
            timeObj = datetime.datetime.strptime(timeInput, '%H:%M:%S')
            return True
        except ValueError:
            return False

    def getAdjustedGHA(dateInput, timeInput):
        starDateTimeString = dateInput + ' ' + timeInput
        starDateTimeObj = datetime.datetime.strptime(starDateTimeString,
                                                     '%Y-%m-%d %H:%M:%S')
        GHAADateTimeObj = datetime.datetime.strptime('2001-01-01 00:00:00',
                                                     '%Y-%m-%d %H:%M:%S')
        GHAADeg = '100d42.6'
        cumProg = 0

        # Get Difference in years
        if(starDateTimeObj.year > GHAADateTimeObj.year):
            yearDiff = starDateTimeObj.year - GHAADateTimeObj.year
            print('convertDegMinStrToNum={0}'.format(CH.convertDegMinStrToNumber(
                                                   '-0d14.31667')))
            cumProg = getCumProg(yearDiff)

        #Consider Leap Years
        leapYears = getNumOfLeapYearInbtw(GHAADateTimeObj.year, starDateTimeObj.year)
        totalProg = getTotalProgression(leapYears)
        primeMeriRotat = getPrimeMeriRotation(GHAADeg,cumProg,totalProg)
        rotatFromYearStart = getEarthRotatSinceYearStart(starDateTimeObj)
        adjustedGHA = getTotalAdjustedGHA(primeMeriRotat, rotatFromYearStart)

        return adjustedGHA # FOR NOW~

    def getCumProg(yearDiff):
        return CH.convertNumToDegMinString(yearDiff *
                                               CH.convertDegMinStrToNumber(
                                                   '-0d14.31667'))


    # Find num of leap years after xxx before yyy
    def getNumOfLeapYearInbtw(after, before):
        startYear = after + 1
        numOfLeapYears = 0
        for x in xrange(startYear, before):
            if(calendar.isleap(x)):
                numOfLeapYears = numOfLeapYears + 1
        return numOfLeapYears

    def getTotalProgression(numOfLeapYears):
        return CH.convertNumToDegMinString(numOfLeapYears
                                        * CH.convertDegMinStrToNumber('0d59.0'))


    def getPrimeMeriRotation(GHAADeg, CumProg, LeapProg):
        answer = CH.convertDegMinStrToNumber(GHAADeg) + CH.convertDegMinStrToNumber(CumProg)\
        + CH.convertDegMinStrToNumber(LeapProg)
        return CH.convertNumToDegMinString(answer)

    def getEarthRotatSinceYearStart(viewingDateTime):
        yearStartDateTimeObj = datetime.datetime.strptime(str(viewingDateTime.year) + '-01-01 00:00:00',
                                                     '%Y-%m-%d %H:%M:%S')
        #totalSec = viewingDateTime - datetime.datetime(viewingDateTime.year, '%Y')
        totalSec = viewingDateTime - yearStartDateTimeObj
        print('totalSec={0}'.format(totalSec.total_seconds()))
        return CH.convertNumToDegMinString(totalSec.total_seconds()/ 86164.1 * 360)

    def getTotalAdjustedGHA(primeMeriRotat, yearRotat):
            return CH.convertNumToDegMinString(CH.convertDegMinStrToNumber(primeMeriRotat) +
                                     CH.convertDegMinStrToNumber(yearRotat))

