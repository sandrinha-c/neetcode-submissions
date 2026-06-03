class Solution:
    def encode(self, strs: List[str]) -> str:
        s="" # str
        for word in strs:
            s+= str(len(word))+"#"+word
        return s
        


    def decode(self, s: str) -> List[str]:
        print(s)
        decode_str=[]
        i=0
        while i < len (s) and s[i]!="#":
            stop=int(s.find("#"))
            print ("stop: ",stop)
            len_word=int(s[i:stop]) #correct
            print ("len_word:", len_word)
            decode_str.append(s[stop+1:stop+1+len_word])
            print ("decode_str",decode_str) 
            i=0
            s=s[stop+1+len_word:]
            print ("i: ", i)
        return decode_str           

