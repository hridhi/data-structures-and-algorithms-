class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i in range(len(emails)):
            local,host=emails[i].split("@")
            if "+" in local:
                #print(local)
                #might be many + 
                x=local.split("+")
                local=x[0]
            if "." in local:
                local=local.replace('.', '')
                #local=''
                #for j in range(len(x)):
                 #  local+=x[j]
            emails[i]=local+"@"+host
            print(emails[i])
        emails=set(emails)
        print(emails)
        return len(emails)
        
