letter = '''  
       Dear <|Name|>, 
       You are selected! 
       <|Date|> 
        '''

print(letter.replace("<|Name|>", "Urmit").replace("<|Date|>", "21th January 2030"))
