# LG
Crypto

## Challenge 

WazzUP! My homie bought a new UltraSmartTV, but he forgot a secret key from an admin panel. After a few attempts to crack this "smart" IoT device it started to generate new passwords on its own, and now we are stuck.

Can you help?

nc lg.q.2019.volgactf.ru 8801

Second host: nc 95.213.235.103 8801

## Solution

### Linear Congruential Generators

Crack LCG: https://tailcall.net/blog/cracking-randomness-lcgs/

Put into a script

Run a few times because it can't be solved for some cases.

	LG $ python3 solve.py 
	Received: Hi, bro!
	Try this:
	42876864878649679574847342
	32925093549911920214468161
	24857357813773036954929369
	19712901521541957490189510
	19456760456322972296079072
	14056535416776088686777556
	71345725052302635857238249
	Predict next one!
	>>>
	## states: [42876864878649679574847342, 32925093549911920214468161, 24857357813773036954929369, 19712901521541957490189510, 19456760456322972296079072, 14056535416776088686777556, 71345725052302635857238249]
	Received: CONGRATULATIONS!
	VolgaCTF{pR3d1ct1ng_1s_n0t_oNlY_f0r_0O0rAculs}

## Flag

	VolgaCTF{pR3d1ct1ng_1s_n0t_oNlY_f0r_0O0rAculs}
