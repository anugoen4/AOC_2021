data = open('data.txt', 'r')
_list = data.read().split('\n')
data.close()


bit_map = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111"
}

def decimal(bit):
    multiplier = 1
    number = 0

    count = len(bit) - 1
    while(count >= 0):
        number += (multiplier * int(bit[count]))
        count -= 1
        multiplier *= 2
    return number

def generate_bit_string(hex):
    string = ""
    for h in hex:
        string += (bit_map[h])
    return string


ans = 0
def parse(bits, i):
    global ans
    version = decimal(bits[i + 0: i + 3])
    ans += version
    type_id = decimal(bits[i + 3:i + 6])

    if(type_id == 4):
        i += 6
        v = 0
        while True:
            v = v * 16 + decimal(bits[i+1: i+5])
            if bits[i] == '0':
                return v, i + 5
            else:
                i += 5
    else:
        len_id = decimal(bits[i + 6])
        vs = []
        if len_id == 0:
            len_bits = decimal(bits[i + 7: i + 7 + 15])
            start_i = i + 7 + 15
            i = start_i
            while True:
                v, next_i = parse(bits, i)
                vs.append(v)
                i = next_i
                if next_i - start_i == len_bits:
                    break
        else:
            n_packets = decimal(bits[i + 7 : i + 7 + 11])
            i += 18
            for _ in range(n_packets):
                v, next_i = parse(bits, i)
                vs.append(v)
                i = next_i
        
        if type_id == 0:
            return sum(vs), i
        elif type_id == 1:
            ans_ = 1
            for v in vs:
                ans_ *= v
            return ans_ , i
        elif type_id == 2:
            return min(vs), i
        elif type_id == 3:
            return max(vs), i
        elif type_id == 5:
            return (1 if vs[0] > vs[1] else 0) , i
        elif type_id  == 6:
            return (1 if vs[0] < vs[1] else 0) , i
        elif type_id == 7:
            return (1 if vs[0] == vs[1] else 0) , i


binary = generate_bit_string(_list[0])
print(parse(binary,0))
print(ans)