letter = "abcdefghijklmnopqrstuvwxyz"

alphabet_array = []

for alphabet in letter:
    alphabet_array.append(alphabet)

text_to_idx = {k:i for i,k in enumerate(alphabet_array)}
idx_to_text = {i:k for i,k in enumerate(alphabet_array)}

def encode(text : str,step : int):
    array = []
    encode_text = ""
    for alphabet in text.strip().lower():
        array.append((text_to_idx[alphabet] + step) % 26)
    for idx in array:
        encode_text += idx_to_text[idx]

    return encode_text

def decode(text : str,step : int):
    array = []
    decode_text = ""
    for alphabet in text.strip().lower():
        array.append((text_to_idx[alphabet] - step) % 26)
    for idx in array:
        decode_text += idx_to_text[idx]

    return decode_text

print(encode("hello",8))
print(decode(encode("hello",8),8))