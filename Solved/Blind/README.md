# Blind
crypto

## Challenge 
Pull the flag...if you can.

	nc blind.q.2019.volgactf.ru 7070

[server.py](server.py)

## Solution

### Functionality of the program

Verify function with (n, e) given

    def verify(self, message, signature):
        message = int(message.encode('hex'), 16)
        verify = pow(signature, self.e, self.n)
        return message == verify

And used for commands

	(sgn, cmd_exp) = message.split(' ', 1)
	# ...
	if not signature.verify(cmd_exp, sgn):
                    
---

### How to attack

This means that:
	
	encrypt(sgn) == cmd_exp

Since we can control only `cmd_exp`, thus we need to do

	sgn == decrypt(cmd_exp)

Notice that we can sign arbitary texts except those commands for `cat` and `cd`

```python
elif cmd == 'sign':
    try:
        send_message('Enter your command to sign:')
        message = read_message().strip()
        message = message.decode('base64')
        cmd_l = shlex.split(message)
        sign_cmd = cmd_l[0]
        if sign_cmd not in ['cat', 'cd']:
            sgn = signature.sign(sign_cmd)
            send_message(str(sgn))
        else:
            send_message('Invalid command')
    except Exception as ex:
        send_message(str(ex))
```

Using ls, we know we must do `cat flag` to get the flag.

If we try to sign anything with `cat` inside... It will throw and error

Try to sign

	Enter your command:
	0 sign      
	Enter your command to sign:
	Y2F0IGZsYWc=
	Invalid command


#### Signing and taking note of `shlex.split()`

Using a script, I made it convert a string to base64 payload to send to the server.

The server will decrypt it and return the decrypted-text. In my script, I will encrypt it again, to verify if our payload works. 

---

If we do a ls flag, the server returns ls...

	Received: Enter your command to sign:
	>> SEND OF MULTIPLE 1
	Cb: b'ls flag'
	Cb_b64: bHMgZmxhZw==
	Received: 5557127951869817283556204158088956835196321943825069404664596599944994126219965332904678276061218022805684978355823286007790529484830086142272225544666707965271106534540384882941815691104258135949033985228692159120390939173399942051750568887603403275598867467617264763608736130256251190821199752188292242016878681146944993878980985669330073182565225584506429951608801328382202378869113680471645411330075543333397714126011413373016678103877673388878053106095364973827514708102658468248585809479995861637060817348598326293249025942246179788910678866634861471717843407176138187778865192082619904375969739604908335967170
	>> RECEIVE OF MULTIPLE 1
	Cb: b'ls'
	No MATCH Cb

We notice that signing only does the first parameter split by space.

This is because our payload is filtered through `shlex.split()`

- [shlex.split()](https://stackoverflow.com/a/34679668)

To overcome this, we need to pass a shell-escaped string. We can do this by using `shlex.quote()`

- [shlex.quote()](https://stackoverflow.com/questions/18116465/escape-a-string-for-shell-commands-in-python)

Now put it into the script and it is working...

	$ python3 solver.py 
	Received: Enter your command:
	Received: Enter your command to sign:

	>> SEND OF MULTIPLE 1
	Cb_quoted: b"'cat flag'"
	Cb_quoted_b64: J2NhdCBmbGFnJw==
	Received: 24276592954466402792157532919706447334355948690098023035375614012157378412616233865544533025515869836447793226406373271083160180523082800598281266834619631704245143244545577613294590334637358684061108293899492468337030535564036215463887905645938530571058038030943037016298964167966109577883005551522062164917343818964991120441652232394288629520079832539360872798332983684006902802429243645009242747601354050053448137191986860769673762567997572657102990869994555786984110522299362261357652756180804304984027320764350120137457095771345729635881422070403269427999652221843885023772233721400195669139542781850847904777323

	>> RECEIVE OF MULTIPLE 1
	Cb_orig: b'cat flag'
	Cb_recv: b'cat flag'

However, due to the check for `cat flag`, we are unable to send that command.

### Chosen ciphertext attack

We can do a chosen ciphertext attack ("blinding" attack)

- https://crypto.stackexchange.com/questions/2323/how-does-a-chosen-plaintext-attack-on-rsa-work
- https://crypto.stackexchange.com/questions/9452/is-a-private-rsa-key-vulnerable-to-a-chosen-plaintext-encrypted-with-that-privat?rq=1

We can multiply our ciphertext by a multiple to bypass the check for `cat flag`. 

This way, we can sign `'cat flag' * multiple`. Then receive the signature and then divide by `multiple` to get the real signature of 'cat flag'.

We need to do a modulo division to get the real signature, we may need to wrap around (due to modulo) with the following code.

	def calculate_plaintext(sgn):
	    signature = sgn // multiple
	    if (signature * multiple != sgn):
	        # modulo division error, try adding n
	        return calculate_plaintext(sgn + n)
	    ...
	    ...

### Final flag

	$ python3 solver.py 
	Received: Enter your command:
	Received: Enter your command to sign:

	>> SEND OF MULTIPLE 2
	Cb_quoted: b'\'\x9b\xa8\x86m\xcb\xc1+B\x86s\\\xb1\x19\xef\xe6w\x02\x9fX\x0f\x1b?\xc8-\x1a1\x85\xd5\x9b\x1d\x98\x98\x19R\xc6:\xa6\xf9J\xa1\xa1\x98\x02\xc6\n~\xd7\xba8\x17p\xc0\x14\xd6\xc0\x98k\x1b0\xf4\xcc\x17{{p\x8c\x01K8%[\xd0\x00@\x81\xe4\xb6!Sf\r\x88&cb\xe8\x1c\x93\xab-\xcf\x8dW\x12\x1b$\xd5\xe1\x87\x99\xcf\xfe,N"\xcb\xa2D\x1d\x0e\x86\x85\x97\x96\xfer\x81b\x94\x0c\xc1\xcb\x13\xc9\x05\xf6\xea\xf1)\xb3\x98\xbew3-\x08\xef\xec\xb1.\xfb\xf2\x82+\xb1D\xd3\x0f\xbdc\xa2)8))^\x8a:R\xc7@\x8d\xbdht7t\xd4\xa7\x13:\xfd;Q\xa8\xa7r\x9f\xf0k\'"\'"\'B?\xc0\x8e\x88\xac\xfd\x91\xff\xd7\xad\xcc\x9eL\x9f.\x1dF\x16\xefN\x94z\xbc\x8c\xee\x95\xe8p\xfe\xee\x05\xbei\xc1\xc2\xca\xaa\xa2\x1d\x0bnP\xb3\xd3\x98m\xf7\xb8\xdf}\xea\xcc\x1a\x02\xdf\xea`\xca\xbd\x07*SKEI\xa8R"\xda^\xee\xc8\xb8\x07\''
	Cb_quoted_b64: J5uohm3LwStChnNcsRnv5ncCn1gPGz/ILRoxhdWbHZiYGVLGOqb5SqGhmALGCn7XujgXcMAU1sCYaxsw9MwXe3twjAFLOCVb0ABAgeS2IVNmDYgmY2LoHJOrLc+NVxIbJNXhh5nP/ixOIsuiRB0OhoWXlv5ygWKUDMHLE8kF9urxKbOYvnczLQjv7LEu+/KCK7FE0w+9Y6IpOCkpXoo6UsdAjb1odDd01KcTOv07Uaincp/wayciJyInQj/Ajois/ZH/163MnkyfLh1GFu9OlHq8jO6V6HD+7gW+acHCyqqiHQtuULPTmG33uN996swaAt/qYMq9BypTS0VJqFIi2l7uyLgHJw==
	Received: 22045594397242921594291169450390532857538863396145029581236806567301117203722505117756741388809584989829412515154251179717587198317347958855323076184017397914564074530974120302841959433098513151277034276794242462124965940821521807736858330676725967200621387154978557683164247320727277535049849064457533434775871207665566905077422889482804185682024447346130244845892222903871523089895110910395035718358661634360565582595196154975490638357852125926741848595121664842529253796951743023903122854013855380456207687869464711471160079428174836069970116352950191126913337619252392768114474911865158436055175904194082226157679
	
	>> RECEIVE OF MULTIPLE 2
	Cb_orig: b'\x9b\xa8\x86m\xcb\xc1+B\x86s\\\xb1\x19\xef\xe6w\x02\x9fX\x0f\x1b?\xc8-\x1a1\x85\xd5\x9b\x1d\x98\x98\x19R\xc6:\xa6\xf9J\xa1\xa1\x98\x02\xc6\n~\xd7\xba8\x17p\xc0\x14\xd6\xc0\x98k\x1b0\xf4\xcc\x17{{p\x8c\x01K8%[\xd0\x00@\x81\xe4\xb6!Sf\r\x88&cb\xe8\x1c\x93\xab-\xcf\x8dW\x12\x1b$\xd5\xe1\x87\x99\xcf\xfe,N"\xcb\xa2D\x1d\x0e\x86\x85\x97\x96\xfer\x81b\x94\x0c\xc1\xcb\x13\xc9\x05\xf6\xea\xf1)\xb3\x98\xbew3-\x08\xef\xec\xb1.\xfb\xf2\x82+\xb1D\xd3\x0f\xbdc\xa2)8))^\x8a:R\xc7@\x8d\xbdht7t\xd4\xa7\x13:\xfd;Q\xa8\xa7r\x9f\xf0k\'B?\xc0\x8e\x88\xac\xfd\x91\xff\xd7\xad\xcc\x9eL\x9f.\x1dF\x16\xefN\x94z\xbc\x8c\xee\x95\xe8p\xfe\xee\x05\xbei\xc1\xc2\xca\xaa\xa2\x1d\x0bnP\xb3\xd3\x98m\xf7\xb8\xdf}\xea\xcc\x1a\x02\xdf\xea`\xca\xbd\x07*SKEI\xa8R"\xda^\xee\xc8\xb8\x07'
	Cb_recv: b'\x9b\xa8\x86m\xcb\xc1+B\x86s\\\xb1\x19\xef\xe6w\x02\x9fX\x0f\x1b?\xc8-\x1a1\x85\xd5\x9b\x1d\x98\x98\x19R\xc6:\xa6\xf9J\xa1\xa1\x98\x02\xc6\n~\xd7\xba8\x17p\xc0\x14\xd6\xc0\x98k\x1b0\xf4\xcc\x17{{p\x8c\x01K8%[\xd0\x00@\x81\xe4\xb6!Sf\r\x88&cb\xe8\x1c\x93\xab-\xcf\x8dW\x12\x1b$\xd5\xe1\x87\x99\xcf\xfe,N"\xcb\xa2D\x1d\x0e\x86\x85\x97\x96\xfer\x81b\x94\x0c\xc1\xcb\x13\xc9\x05\xf6\xea\xf1)\xb3\x98\xbew3-\x08\xef\xec\xb1.\xfb\xf2\x82+\xb1D\xd3\x0f\xbdc\xa2)8))^\x8a:R\xc7@\x8d\xbdht7t\xd4\xa7\x13:\xfd;Q\xa8\xa7r\x9f\xf0k\'B?\xc0\x8e\x88\xac\xfd\x91\xff\xd7\xad\xcc\x9eL\x9f.\x1dF\x16\xefN\x94z\xbc\x8c\xee\x95\xe8p\xfe\xee\x05\xbei\xc1\xc2\xca\xaa\xa2\x1d\x0bnP\xb3\xd3\x98m\xf7\xb8\xdf}\xea\xcc\x1a\x02\xdf\xea`\xca\xbd\x07*SKEI\xa8R"\xda^\xee\xc8\xb8\x07'
	>>> RECV plaintext*multiple: 22045594397242921594291169450390532857538863396145029581236806567301117203722505117756741388809584989829412515154251179717587198317347958855323076184017397914564074530974120302841959433098513151277034276794242462124965940821521807736858330676725967200621387154978557683164247320727277535049849064457533434775871207665566905077422889482804185682024447346130244845892222903871523089895110910395035718358661634360565582595196154975490638357852125926741848595121664842529253796951743023903122854013855380456207687869464711471160079428174836069970116352950191126913337619252392768114474911865158436055175904194082226157679
	verify: b'cat flag'
	
	>>> ATTACK PAYLOAD: 24276592954466402792157532919706447334355948690098023035375614012157378412616233865544533025515869836447793226406373271083160180523082800598281266834619631704245143244545577613294590334637358684061108293899492468337030535564036215463887905645938530571058038030943037016298964167966109577883005551522062164917343818964991120441652232394288629520079832539360872798332983684006902802429243645009242747601354050053448137191986860769673762567997572657102990869994555786984110522299362261357652756180804304984027320764350120137457095771345729635881422070403269427999652221843885023772233721400195669139542781850847904777323 cat flag
	Received: Enter your command:
	Received: VolgaCTF{B1ind_y0ur_tru3_int3nti0n5}
	Received: Enter your command:
	Received: VolgaCTF{B1ind_y0ur_tru3_int3nti0n5}


## Flag

	VolgaCTF{B1ind_y0ur_tru3_int3nti0n5}
