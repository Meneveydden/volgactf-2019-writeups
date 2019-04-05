from base64 import b64encode
import shlex
import socket

n = 26507591511689883990023896389022361811173033984051016489514421457013639621509962613332324662222154683066173937658495362448733162728817642341239457485221865493926211958117034923747221236176204216845182311004742474549095130306550623190917480615151093941494688906907516349433681015204941620716162038586590895058816430264415335805881575305773073358135217732591500750773744464142282514963376379623449776844046465746330691788777566563856886778143019387464133144867446731438967247646981498812182658347753229511846953659235528803754112114516623201792727787856347729085966824435377279429992530935232902223909659507613583396967
e = 65537

# any number of multiple will work, use 2 because it is simple/small
multiple = 2
cmd_exp = "cat flag"

def to_hex(i):
    i_hex = hex(i)[2:]
    if len(i_hex) % 2 == 1:
        i_hex = '0' + i_hex
    return i_hex


def make_payload(cmd_exp="exit"):
    # RSA encode with chosen ciphertext attack
    Cx = int(cmd_exp.encode().hex(), 16)
    Ca = pow(multiple, e, n)
    Cb = (Ca * Cx) % n

    # convert to byte array
    Cb_hex = to_hex(Cb)
    Cb = bytes.fromhex(Cb_hex)
    # print("Cb:", Cb)

    # excape it using shlex
    Cb_quoted = shlex.quote(Cb.decode('latin_1')).encode('latin_1')
    # print("Cb_quoted:", Cb_quoted)

    # ensure that the escaped text is the same,
    # after being parsed in shlex.split()
    cmd_l = shlex.split(Cb_quoted.decode('latin_1'))
    assert (cmd_l[0].encode('latin_1') == Cb)
    # print("split:", cmd_l)

    # form payload as the server takes it in b64-form
    payload = Cb_quoted
    payload_b64 = b64encode(payload).decode()
    return (payload, payload_b64)


def check_recv(sgn):
    Cb = pow(sgn, e, n)
    Cb_text = bytes.fromhex(to_hex(Cb))
    # print("Cb:", Cb_text)
    return Cb_text


def calculate_plaintext(sgn):
    signature = sgn // multiple
    if (signature * multiple != sgn):
        # modulo division error, try adding n
        return calculate_plaintext(sgn + n)
    verify = pow(signature, e, n)
    verify_text = bytes.fromhex(to_hex(verify))
    print("verify:", verify_text)
    return signature


def main():
    global multiple

    s = socket.socket()
    s.connect(('blind.q.2019.volgactf.ru', 7070))

    # first part: send chosen-ciphertext attack to server
    while True:
        data = s.recv(2048).decode().strip()
        if not data:
            continue
        print('Received:', data)

        if 'Enter your command:' in data:
            # choose menu option
            payload = '0 sign'
            s.send(payload.encode() + b'\n')

        elif 'Enter your command to sign:' in data:
            # make chosen-ciphertext payload
            # we will send: cmd_exp * multiple
            Cb_quoted, Cb_quoted_b64 = make_payload(cmd_exp)
            print(">> SEND OF MULTIPLE", multiple)
            print("Cb_quoted:", Cb_quoted)
            print("Cb_quoted_b64:", Cb_quoted_b64)
            s.send(Cb_quoted_b64.encode() + b'\n')

        elif data.strip().isdigit():
            # decode returned ciphertext
            sgn = int(data)
            Cb_recv = check_recv(sgn)
            Cb_orig = shlex.split(Cb_quoted.decode('latin_1'))
            Cb_orig = Cb_orig[0].encode('latin_1')

            print(">> RECEIVE OF MULTIPLE", multiple)
            print("Cb_orig:", Cb_orig)
            print("Cb_recv:", Cb_recv)

            # encrypt again to make sure that original 
            # ciphertext has survived through the shlex.split()
            if (Cb_orig != Cb_recv):
                print("NO MATCH: Cb\n")
                quit()

            # else: if it matches then we can execute attack
            # calculate by doing modulo division of the original multiple
            print('>>> RECV:', data)
            Attack_sgn = calculate_plaintext(sgn)

            # Then form the payload
            final_payload = f"{Attack_sgn} {cmd_exp}"
            print('>>> ATTACK PAYLOAD:', final_payload)
            break

    # second part: send the calculated signature to `cat flag`
    while True:
        data = s.recv(2048).decode().strip()
        if not data:
            continue
        print('Received:', data)

        if 'Enter your command:' in data:
            s.send(final_payload.encode() + b'\n')

        if 'VolgaCTF{' in data:
            quit()

if __name__ == '__main__':
    main()
