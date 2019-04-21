with open('twain.txt','r',encoding='utf-8') as f: #the variable f is the file twian.txt opened
    contents=f.read()    #f.read reads the contents of the twian.txt
    correction=contents.replace('Huck','HucK') #correction contains the contents of the file with Huck converted to HucK

    with open('twain.txt', 'w', encoding='utf-8') as w:
        #then using write funtion we overwritted the contents of the variable f with Huck changed to HucK
        w.write(correction)



