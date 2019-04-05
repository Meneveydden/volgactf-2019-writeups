# JOI
stego

## Challenge 

All we have is just one image

result.png

## Solution

QR code

	$ zbarimg result.png 
	QR-Code:C_F(n1, n2) = 14 * [C(n1,n2) / 14] + 7 * FLAG(n1,n2) + (C(n1,n2) mod 7)
	scanned 1 barcode symbols from 1 images in 0.04 seconds

But open in stegsolve and go to Red Plane 0.

	$ zbarimg red_plane_0.png
	QR-Code:VolgaCTF{5t3g0_m4tr3shk4_in_4cti0n}

## Flag

	VolgaCTF{5t3g0_m4tr3shk4_in_4cti0n}
