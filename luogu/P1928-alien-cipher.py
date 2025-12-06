def decode_alien_cipher(cipher : str) -> str :
    def decode_inner(cipher : str) -> str :
        left  = cipher.rfind("[")
        right = cipher.find("]", left)

        if left == -1 and right == -1 :
            return cipher
        elif (left == -1 and right != -1) or (left != -1 and right == -1) :
            raise ValueError("Unpaired brackets !")
        else :
            num_last = left + 1
            while num_last <= right - 1 :
                if not cipher[num_last].isnumeric() :
                    break
                else :
                    num_last += 1
            repeated = int(cipher[left + 1:num_last])
            decoded = cipher[0:left]                \
                + cipher[num_last:right] * repeated \
                + cipher[right + 1:]
            return decode_inner(decoded)
    return decode_inner(cipher)

if __name__ == "__main__" :
    cipher = input().rstrip()
    print(decode_alien_cipher(cipher))