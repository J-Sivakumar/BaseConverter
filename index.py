from flask import *

result = ''
d={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

# convertTo10() function is used to convert the number from any base to base 10
def convertTo10(n,b):
    r=0
    for i in range(len(n)):
        if n[i].isdigit():
            r+=int(n[i])*b**(len(n)-i-1)
        else:
            r+=d[n[i]]*b**(len(n)-i-1)
    return r

# convertFrom10() function is used to convert the number from base 10 to required base
def convertFrom10(d,b):
    n=d
    if n==0:
        return '0'
    r=''
    while n>0:
        s=n%b
        if s<=9:
            r+=str(s)
        else:
            r+=chr(55+s)
        n//=b
    return r[::-1]

#convertBase() is used convert number from source base to destination base
def convertBase(n,b,r):
    d=convertTo10(n,b)
    d1=convertFrom10(d,r)
    return d1

# DPconvertTo10() function is used to convert the number(that is present after decimal point) from any base to base 10
def DPconvertTo10(n,b):
    r=0
    for i in range(len(n)):
        if n[i].isdigit():
            r+=int(n[i])*b**(-i-1)
        else:
            r+=d[n[i]]*b**(-i-1)
    return r

# DPconvertFrom10() function is used to convert the number (that is present after decimal point) from base 10 to required base
def DPconvertFrom10(d,b):
    n=d
    r=''
    i=0
    while n>0 and i<21:
        i+=1
        a=n*b
        s=int(a)
        if s<=9:
            r+=str(s)
        else:
            r+=chr(55+s)
        n=a-s
    return r

#DPconvertBase() is used convert number(that is present after decimal point) from source base to destination base 
def DPconvertBase(n,b,r):
    d=DPconvertTo10(n,b)
    d1=DPconvertFrom10(d,r)
    return d1

# check() function will check whether the given number is in right base or not
def check(n,b):
        for i in n:
            if i.isdigit():
                if int(i)>=b:
                    break
            elif i.isupper():
                if d[i]>=b:
                    break
        else:
            return True
        return False

#check_input() will verify the input is valid or not. If valid, then base is converted
def check_input(n,s,d):
    global result
    if n.find('.')!=-1:
        b=s
        if(n.count('.')!=1):
            result = "Invalid Integer/ Decimal Number"
            return
        m,n=n.split('.')
        r=d
        if check(m,b) and check(n,b):
            s=convertBase(m,b,r)
            p=DPconvertBase(n,b,r)
            result = 'Result is : '+s+'.'+p+' ( in base '+str(r)+' )'
        else:
            result = 'Please enter a valid base(source base) for the given number'
    else:
        b=s
        r=d
        if check(n,b):
            s=convertBase(n,b,r)
            result = 'Result is : '+str(s) +' (in base'+str(r)+')'
        else:
            result = 'Please enter a valid base(source base) for the given number'


app = Flask(__name__)
@app.route('/')
def home():
    return render_template("baseconvert.html")

@app.route('/success',methods=['POST'])
def success():
    if request.method=='POST':
        number = (request.form['num']).upper()
        src = int(request.form['src'])
        dest = int(request.form['dest'])
        check_input(number,src,dest)
        input = 'Given Number: '+ number + ' (in Base '+str(src) +')'
        data = [number,src,dest]
        return render_template("baseconvert.html",result = result, input=input,form=data,s=True)

if __name__ == '__main__':
    app.run(debug=True)


    