import cv2

def cesar(msg, state, key):
	if key == '': key = '0'
	if state == 1:
		for num in key:
			if int(num) == 0: continue
			temp = ''
			for l in msg:
				shift = int(num) + ord(l)
				shift = shift if (shift <= 122) else ((shift - 122) + 65)
				temp += chr(shift) if (l.isalnum()) else l
			msg = temp
		return msg
	else:
		key = list(reversed(key))
		for num in key:
			temp = ''
			if int(num) == 0: continue
			for l in msg:
				shift = ord(l) - int(num)
				shift = shift if(shift >= 65) else (122 - (65 - shift))
				temp += chr(shift) if (l != " ") else " "

			msg = temp
		return msg

def to_binary(inp, key = '0'):
    if type(inp) is str:
        out = ''
        inp = cesar(inp, 1, key) + '/*-'
        for l in inp: out += "{0:08b}".format(ord(l))
        return out
    else:
        out = [''] * 3
        for v in range(3): out[v] = "{0:08b}".format(inp[v])
        return out

def to_value(inp, key = '0'):
    if type(inp) is str:
        out = ''
        for i in range(0, len(inp), 8):
            byte = inp[i:i+8]
            out += chr(int(byte,2))
        out = cesar(out, 0, key)
        return out
    else:
        out = [0] * 3
        for v in range(3): out[v] = int(inp[v], 2)
        return out

def decode_key(key = "0000"):
    key_o = ''
    for l in key:
        if l.isalpha(): key_o += str(ord(l))
        else: key_o += l
    return int(key_o[:2]), int(key_o[2:4]), key_o[4:]
	

def embed(img, msg, savePath, key, out_):
    l = 0
    x_cords, y_cords, cesar_key = decode_key(key)
    img = cv2.imread(img)
    msg = to_binary(msg, cesar_key)
    for i in range(x_cords, img.shape[0]): # iter over rows
        for j in range(y_cords, img.shape[1], 2): # iter over cols
            if not l == len(msg):
                byte = msg[l:l+8]
            else: break
                
            p1 = to_binary(img[i][j])
            p2 = to_binary(img[i][j+1])
                    
            p1[0] = p1[0][:6] + byte[:2]
            p1[1] = p1[1][:6] + byte[2:4]

            p2[0] = p2[0][:6] + byte[4:6]
            p2[1] = p2[1][:6] + byte[6:]

            img[i][j] = to_value(p1)
            img[i][j+1] = to_value(p2)

            print("{} and {} are done, {} chars remain".format(p1, p2,len(msg) - l))
            l += 8
        if l == len(msg): break
    
    cv2.imwrite(str(savePath + out_) , img)
    print("Done !!")
    return msg 
                

def decode(path, key):
    img = cv2.imread(path)
    msg = ''
    x_cords, y_cords, cesar_key = decode_key(key)
    done = False
    for i in range(x_cords, img.shape[0]): # iter over rows
        for j in range(y_cords, img.shape[1], 2): # iter over cols
            p1 = to_binary(img[i][j])
            p2 = to_binary(img[i][j+1])

            msg += (p1[0][-2:] + p1[1][-2:] + p2[0][-2:] + p2[1][-2:])
            if msg[-24:] == '001011110010101000101101':
                done = True
                break
        if done == True: break
            
    return to_value(msg[:-24], cesar_key)
       
    

