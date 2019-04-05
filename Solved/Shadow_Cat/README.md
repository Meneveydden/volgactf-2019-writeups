# Shadow Cat
crypto

## Challenge 

We only know that one used /etc/shadow file to encrypt important message for us. 
	
- shadow.txt
- encrypted.txt

## Solution

If we do a default John-the-ripper attack, we see it cracking really slowly...

	$ /usr/local/Cellar/john-jumbo/1.8.0/share/john/john shadow.txt 
	...
	Remaining 26 password hashes with 26 different salts
	Press 'q' or Ctrl-C to abort, almost any other key for status
	0g 0:00:00:02 8.13% 1/3 (ETA: 13:26:50) 0g/s 692.5p/s 692.5c/s 692.5C/s 99999f
	0g 0:00:00:04 9.89% 1/3 (ETA: 13:27:06) 0g/s 694.3p/s 694.3c/s 694.3C/s j"
	0g 0:00:00:42 63.96% 1/3 (ETA: 13:27:31) 0g/s 687.6p/s 687.6c/s 687.6C/s B29
	0g 0:00:00:46 67.65% 1/3 (ETA: 13:27:33) 0g/s 687.5p/s 687.5c/s 687.5C/s U99999M
	d                (s)
	t                (u)
	g                (d)
	r                (y)

However, we find out that all the cracks are 1 char long.

Now, let's use some [John config files](https://www.reddit.com/r/AskNetsec/comments/52ljwt/is_there_a_way_to_pass_the_minimum_and_maximum/
) to limit our password length to 1.

	[Incremental:helloworld]
	File = /usr/local/Cellar/john-jumbo/1.8.0/share/john/ascii.chr
	MinLen=1
	MaxLen=1

And then execute it again.

	$ /usr/local/Cellar/john-jumbo/1.8.0/share/john/john --config=./john.conf --incremental:helloworld shadow.txt
	
	Warning: detected hash type "sha512crypt", but the string is also recognized as "sha512crypt-opencl"
	Use the "--format=sha512crypt-opencl" option to force loading these as that type instead
	Warning: hash encoding string length 98, type id $6
	appears to be unsupported on this system; will not load such hashes.
	Loaded 28 password hashes with 28 different salts (sha512crypt, crypt(3) $6$ [SHA512 64/64 OpenSSL])
	Remaining 1 password hash
	Warning: only 62 characters available
	Press 'q' or Ctrl-C to abort, almost any other key for status
	0g 0:00:00:03 64.49% (ETA: 21:44:57) 0g/s 631.3p/s 631.3c/s 631.3C/s gz
	0g 0:00:00:04 80.72% (ETA: 21:44:57) 0g/s 631.8p/s 631.8c/s 631.8C/s ex
	0g 0:00:00:06 DONE (2019-03-31 21:44) 0g/s 634.0p/s 634.0c/s 634.0C/s ZX
	Session completed

We get the results.

	$ /usr/local/Cellar/john-jumbo/1.8.0/share/john/john --show shadow.txt 

	jr:1:17792:0:99999:7:::
	z:_:17930:0:99999:7:::
	a:a:17930:0:99999:7:::
	x:b:17930:0:99999:7:::
	q:c:17930:0:99999:7:::
	l:w:17930:0:99999:7:::
	v:h:17930:0:99999:7:::
	e:i:17930:0:99999:7:::
	f:j:17930:0:99999:7:::
	b:k:17930:0:99999:7:::
	r:l:17930:0:99999:7:::
	g:m:17930:0:99999:7:::
	n:n:17930:0:99999:7:::
	o:x:17930:0:99999:7:::
	p:y:17930:0:99999:7:::
	s:d:17930:0:99999:7:::
	c:e:17930:0:99999:7:::
	w:f:17930:0:99999:7:::
	d:g:17930:0:99999:7:::
	t:o:17930:0:99999:7:::
	h:p:17930:0:99999:7:::
	m:q:17930:0:99999:7:::
	k:u:17930:0:99999:7:::
	i:v:17930:0:99999:7:::
	y:r:17930:0:99999:7:::
	j:s:17930:0:99999:7:::
	u:t:17930:0:99999:7:::
	underscore:z:17930:0:99999:7:::
	28 password hashes cracked, 0 left

After which, we can use a script to do a 1-to-1 replacement mapping.

	$ python3 solve.py 
	replacements [('jr', '1'), ('z', '_'), ('a', 'a'), ('x', 'b'), ('q', 'c'), ('l', 'w'), ('v', 'h'), ('e', 'i'), ('f', 'j'), ('b', 'k'), ('r', 'l'), ('g', 'm'), ('n', 'n'), ('o', 'x'), ('p', 'y'), ('s', 'd'), ('c', 'e'), ('w', 'f'), ('d', 'g'), ('t', 'o'), ('h', 'p'), ('m', 'q'), ('k', 'u'), ('i', 'v'), ('y', 'r'), ('j', 's'), ('u', 't'), ('_', 'z')]
	pass_hash_cracking_hashcat_always_lurks_in_the_shadows

## Flag

	VolgaCTF{pass_hash_cracking_hashcat_always_lurks_in_the_shadows}
