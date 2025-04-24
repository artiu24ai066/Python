def decode_message(s):
    def decode(s, current):
        if not s:
            return [current]
        results = []
        
        if s[0] != '0': 
            results.extend(decode(s[1:], current + chr(int(s[0]) - 1 + ord('A'))))

        if len(s) >= 2 and '10' <= s[:2] <= '26':
            results.extend(decode(s[2:], current + chr(int(s[:2]) - 1 + ord('A'))))
        
        return results   
    return decode(s, '')

encoded_message = input("Enter any code:")
decoded_messages = decode_message(encoded_message)

for message in decoded_messages:
    print(message)
