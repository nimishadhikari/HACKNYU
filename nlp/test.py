'''
Test file to figure out nlp

Will put json objects from web console analysis in here, then try different ways to handle them

'''

import datefinder
import dateparser
import daterangeparser

data_ray =  ["MARCH FOR SCIENCE\nNew York City\nRALLY &amp; SCIENCE EXPO\nAPRIL 14, 2018 | 9 AM\nW ASHINGTON SQUARE PARK, NEW YORK CITY\nEVERY ONE'S WELCOME!\n#marchforsciencenyc\n#ScienceMarchesOn\nLearn more :\nmarchforsciencenyc.com\nfacebook.com/mfsnyc\no marchforsciencenyo\nnyc _ m arch\n", "FIFT8\nKoprrier\n| IT'S IN T\nT'S IN THE GA\nGAME NIGHT\n2 V 2 Single Elimination Fifa Tournament\n(Max 12 teams allowed)\nMarch 30\n6:00 - 9:00 PM\nMAGNET (Room 811 8 812)\nMario Kart Casual Play\nPrizes For Winners\nFree Food\nRegister by March 29 at 5 PM\nRSVP: https://goo.gl/agq6Wm\nPgn\npolygamingnetwork\nTANDO UNDERGRADUATE\nSTUDENT COUNCIL\nGRADUATE STUDENT COUNCIL\nPootinvolved\n1851\n", "Snow (Titanium) White\nllung Ingige) fitone/Blanco de Tidni\nACRYLIC PAINT\nPEINTURE ACRYLIQUE\nPINTURA ACRÍLICA\nTINTA ACRÍLICA\nCOLORE ACRILICO\nDecorf\nCOLORE ACRILICO NAS ON\nSpring Intermission\nARTISTIC WORKSHOP\nSu be with decorating\nniars? Come celebrate\nHow creative can you be with decorat\nand painting mason jars? Come cele\nthe onset of the spring season!\nMar 27 @ 5:00PM\nRSVP: bit.ly/spring-intermission\nGREENHOUSE\nat MakerSpace\nTANDON SCHOOL\nOF ENGINEERING\nO NYU TANERNE\n","lokerspace\nse\nService Month\n– E VENTS-\nEvent 2 - Food Packaging\nMarch 6 | March 27\niches to donate to\nBowery Mission.\nHelp make sandwiches to don\ndonate to the Bowery M:\nvourself a sandwich if.\nmake two or more sand\nMake yourself a so\nse sandwiches!\nsation - Makerspace E.\nhace Foyer\nLocation : M\n"]



for i, data in enumerate(data_ray):
    print("------")
    print(data)
    lines = data.split('\n')
    for j, line in enumerate(lines):
        if "|" in line:
            line_ray = line.split("|")
            for line in line_ray:
                date = dateparser.parse(line)
                if date is not None:
                    print(lines[j-1])
                    print(date)
                    print(lines[j+1])
        else:
            date = dateparser.parse(line)
            if date is not None:
                print(lines[i-1])
                print(date)
                print(lines[i+1])
    
    if i == 2:
        break
    print("------")

'''
datefinder.find
dateparser.parse
daterangeparser.parse
'''
