
class LanguageHelper:
    def __init__(self, words):
       self._words=words
       s=set()
       for i in words:
           s.add(i)
       self._s=s
    def __contains__(self, query):
        if query in self._s:
            return True
        else:
            return False
    def getSuggestions(self, query):
        list1=[]
        if query in self._s:
            return []
        # implement capitalization check
        if query[0].islower() and query.capitalize() in self._s :
            list1.append(query.capitalize())

            
        if query.isupper() and query.lower() in self._s:
            list1.append(query.lower())


        # Mixed word
        if not query.isupper() and not query.islower():
            if query.upper() in self._s:
                list1.append(query.upper())
            if query.lower() in self._s:
                list1.append(query.lower())
            

        # Try Deletion
        for i in range(len(query)-1):
            word=query
            word = word[0 : i : ] + word[i + 1 : :]
            if word in self._s:
                    if query[0].isupper():
                        list1.append(word.capitalize())
                    else:
                        list1.append(word)

        # Try insertion
        alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in range(len(query)):
            for j in range(26):
                word=query.lower()
                word= word[0 : i : ] +alpha[j]+word[i : :]
                if word in self._s:
                    if query[0].isupper():
                        list1.append(word.capitalize())
            
                    else:
                        list1.append(word)
                        
                        


                        
        # Try Replacement:
        for i in range(len(query)-1):
            for j in range(26):
                word=query
                word = word[0 : i : ] +alpha[j] +word[i + 1 : :]
                if word in self._s:
                    if query[0].isupper()and query!=word.capitalize():
                        list1.append(word.capitalize())
                      
                    else:
                        list1.append(word)
                       
                        




        
        #Nissouri return Missouri      
        if query[0].isupper():
            for j in range(26):
                word=query
                word= alpha[j].upper()+word[1 : :]
                if word in self._s:
                    list1.append(word)
                    
                        


        # gate search date return Date             
        if query[0].isupper():
            for j in range(26):
                word=query
                word= alpha[j]+word[1 : :]
                if word in self._s:
                    if query[0].isupper() and query !=word.capitalize():
                        list1.append(word.capitalize())
                     
                    else:
                        list1.append(word)
                     

        #Swap letters
        for i in range(0,len(query)-2):
            word=query
            x=word[i]
            y=word[i+1]
            word = word[0 : i : ] +y+x+word[i + 2 : :]
            if word in self._s :
                if query[0].isupper() and query !=word.capitalize():
                    list1.append(word.capitalize())
                
                else:
                    list1.append(word)
                   


                        

        # Return list of words suggestions
        if len(list1)>0:
            # remove duplicates from list
            list1 = list(dict.fromkeys(list1))
  
            return sorted(list1)
        else:
            return []






            










        
