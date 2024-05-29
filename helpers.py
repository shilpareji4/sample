def getMaxLengthContent(headers):
        dict1 = {}
        c = 0
        for header in headers:
            c+=1
            dict1[str(c)] = len(header)
        dict2 = dict(dict1.items(),key=lambda x:x[1],reverse=True)  
        return dict2[list(dict2.keys())[0]] 

