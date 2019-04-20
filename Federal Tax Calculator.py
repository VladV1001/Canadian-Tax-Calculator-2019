print('Canadian Income Tax Calculator 2019')
b=(47630,95259,147667,210371,9999999999)
r=(.15,.205,.26,.29,.33)
print('This program does not take tax credits into account, it only calculates ones federal and provincial tax liability on their Division B Income, also known as net income for tax porpuses')
x=float(input('What is your net income for tax porpuses this year?'))
if x<=b[0]:
    tt=(x*r[0])
elif x<=b[1]:
    tt=(b[0]*r[0]+(x-b[0])*r[1])
elif x<=b[2]:
    tt=(b[0]*r[0]+(b[1]-b[0])*r[1]+(x-b[1])*r[2])
elif x<=b[3]:
    tt=(b[0]*r[0]+(b[1]-b[0])*r[1]+(b[2]-b[1])*r[2]+(x-b[2])*r[3])
elif x<=b[4]:
    tt=(b[0]*r[0]+(b[1]-b[0])*r[1]+(b[2]-b[1])*r[2]+(b[3]-b[2])*r[3]+(x-b[3])*r[4])
print('What province do you reside in?')
p=(input('ON//AB//SK//NB//BC//PEI//NF//NS//MB//YU//NU//NWT'))
if p=='ON':
    pb=(0,43906,87813,150000,220000,9999999999)
    pr=(0,.0505,.0915,.1116,.1216,.1316)
elif p=='NF':
    pb=(0,37591,75181,134224,187913,9999999999)
    pr=(0,.087,.145,.158,.173,.183)
elif p=='PEI':
    pb=(0,0,0,31984,63969,9999999999)
    pr=(0,0,0,.098,.138,.167)
elif p=='NS':
    pb=(0,29590,59180,93000,150000,9999999999)
    pr=(0,.0879,.1495,.1667,.175,.21)
elif p=='NB':
    pb=(0,42590,85184,138491,157778,9999999999)
    pr=(0,.0968,.1482,.1652,.1784,.203)
elif p=='SK':
    pb=(0,0,0,45225,129214,9999999999)
    pr=(0,0,0,.11,.1275,.174)
elif p=='AB':
    pb=(0,131220,157464,209952,314929,9999999999)
    pr=(0,.1,.12,.13,.14,.15)
elif p=='BC':
    pb=(0,40707,81416,93576,113503,153900,9999999999)
    pr=(0,.1,.12,.13,.14,.15)
elif p=='YU':
    pb=(0,0,47630,95259,147667,500000,9999999999)
    pr=(0,0,.064,.09,.109,.128,.15)
elif p=='NWT':
    pb=(0,0,0,43137,86277,140267,9999999999)
    pr=(0,0,0,.059,.086,.122,.1405)
elif p=='NU':
    pb=(0,0,0,45414,90829,147667,9999999999)
    pr=(0,0,0,.04,.07,.09,.115)
else:
    print('NOT RECOGNIZED, PLEASE TRY AGAIN')
if x<=b[0]:
    tb=(x*r[0])
elif x<=b[1]:
    tb=(100*r[1])
elif x<=b[2]:
    tb=(100*r[2])
elif x<=b[3]:
    tb=(100*r[3])
elif x<=b[4]:
    tb=(100*r[4])
if x<=pb[0]:
    ptt=(x*pr[0])
elif x<=pb[1]:
    ptt=(pb[0]*pr[0]+(x-pb[0])*pr[1])
elif x<=pb[2]:
    ptt=(pb[0]*pr[0]+(pb[1]-pb[0])*pr[1]+(x-pb[1])*pr[2])
elif x<=pb[3]:
    ptt=(pb[0]*pr[0]+(pb[1]-pb[0])*pr[1]+(pb[2]-pb[1])*pr[2]+(x-pb[2])*pr[3])
elif x<=pb[4]:
    ptt=(pb[0]*pr[0]+(pb[1]-pb[0])*pr[1]+(pb[2]-pb[1])*pr[2]+(pb[3]-pb[2])*pr[3]+(x-pb[3])*r[4])
elif x<=pb[5]:
    ptt=(pb[0]*pr[0]+(pb[1]-pb[0])*pr[1]+(pb[2]-pb[1])*pr[2]+(pb[3]-pb[2])*pr[3]+(pb[4]-pb[3])*pr[4]+(x-pb[4])*r[5])
elif x<=pb[5]:
    ptt=(pb[0]*pr[0]+(pb[1]-pb[0])*pr[1]+(pb[2]-pb[1])*pr[2]+(pb[3]-pb[2])*pr[3]+(pb[4]-pb[3])*pr[4]+(pb[5]-pb[4])*pr[5]+(x-pb[5])*r[6])
if x<=pb[0]:
    ptb=(x*pr[0])
elif x<=pb[1]:
    ptb=(100*pr[1])
elif x<=pb[2]:
    ptb=(100*pr[2])
elif x<=pb[3]:
    ptb=(100*pr[3])
elif x<=pb[4]:
    ptb=(100*pr[4])
elif x<=pb[5]:
    ptb=(100*pr[5])
elif x<=pb[6]:
    ptb=(100*pr[6])
print('Your federal tax liability for the year:$',float(tt))
print('Your provincial tax liability for the year:$',float(ptt))
print('Your total tax liability for the year:$',float(ptt)+float(tt))
print('Your federal income tax bracket for the year is ',tb,'%')
print('Your provincial income tax bracket for the year is ',ptb,'%')
print('Your effective federal tax rate is',100*tt/x,'%')
print('Your effective provincial tax rate is',100*ptt/x,'%')
print('Your total effective tax rate is',100*(ptt+tt)/x,'%')
print('Your net income after tax this year is $',x-tt-ptt)
if p=='ON':
    print('Here are your 2019 income tax resluts in the province of Ontario')
elif p=='NF':
    print('Here are your 2019 income tax resluts in the province of Newfoundland and Labrador')
elif p=='PEI':
    print('Here are your 2019 income tax resluts in the province of Prince Edward Island')
elif p=='NS':
    print('Here are your 2019 income tax resluts in the province of Nova Scotia')
elif p=='NB':
    print('Here are your 2019 income tax resluts in the province of New Brunswick')
elif p=='SK':
    print('Here are your 2019 income tax resluts in the province of Saskachewan')
elif p=='AB':
    print('Here are your 2019 income tax resluts in the province of Alberta')
elif p=='BC':
    print('Here are your 2019 income tax resluts in the province of British Columbia')
elif p=='YU':
    print('Here are your 2019 income tax resluts in the territory of Yukon')
elif p=='NWT':
    print('Here are your 2019 income tax resluts in the Northwest Territory')
elif p=='NU':
    print('Here are your 2019 income tax resluts in the territory of Nunavut')
else:
    print('Invalid input, disregard results and try again')
