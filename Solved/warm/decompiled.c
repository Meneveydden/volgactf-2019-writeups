int sub_9ec(int arg0, int arg1) {
    r7 = (sp - 0xf0) + 0x0;
    *(r7 + 0x4) = arg0;
    *r7 = arg1;
    *(r7 + 0xdc) = **0x10fe8;
    setvbuf(**0x10ff4, 0x0, 0x2, 0x0);
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
    do {
            *(r7 + 0x10) = _IO_getc();
            if (*(r7 + 0x10) == 0xffffffff) {
                break;
            }
            putchar(*(r7 + 0x10));
    } while (true);
    fclose(*(r7 + 0xc));
    r0 = 0x0;
    if (*(r7 + 0xdc) != **0x10fe8) {
            r0 = __stack_chk_fail();
    }
    return r0;
}


int sub_788(int arg0) {
    r7 = (sp - 0x18) + 0x0;
    *(r7 + 0x4) = arg0;
    if (strlen(*(r7 + 0x4)) <= 0xf) {
            r3 = 0x1;
    }else {
            *(r7 + 0xf) = 0x23;
            if (((((((((zero_extend_32(*(int8_t *)(r7 + 0xf) ^ *(int8_t *)*(r7 + 0x4)) == 0x55) && (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0x1) ^ *(int8_t *)*(r7 + 0x4)) == 0x4e)) && (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0x2) ^ *(int8_t *)(*(r7 + 0x4) + 0x1)) == 0x1e)) && (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0x3) ^ *(int8_t *)(*(r7 + 0x4) + 0x2)) == 0x15)) && (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0x4) ^ *(int8_t *)(*(r7 + 0x4) + 0x3)) == 0x5e)) && (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0x5) ^ *(int8_t *)(*(r7 + 0x4) + 0x4)) == 0x1c)) && (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0x6) ^ *(int8_t *)(*(r7 + 0x4) + 0x5)) == 0x21)) && (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0x7) ^ *(int8_t *)(*(r7 + 0x4) + 0x6)) == 0x1)) && (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0x8) ^ *(int8_t *)(*(r7 + 0x4) + 0x7)) == 0x34)) {
                    if (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0x9) ^ *(int8_t *)(*(r7 + 0x4) + 0x8)) == 0x7) {
                            if (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0xa) ^ *(int8_t *)(*(r7 + 0x4) + 0x9)) == 0x35) {
                                    if (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0xb) ^ *(int8_t *)(*(r7 + 0x4) + 0xa)) == 0x11) {
                                            if (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0xc) ^ *(int8_t *)(*(r7 + 0x4) + 0xb)) == 0x37) {
                                                    if (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0xd) ^ *(int8_t *)(*(r7 + 0x4) + 0xc)) == 0x3c) {
                                                            if (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0xe) ^ *(int8_t *)(*(r7 + 0x4) + 0xd)) == 0x72) {
                                                                    if (zero_extend_32(*(int8_t *)(*(r7 + 0x4) + 0xf) ^ *(int8_t *)(*(r7 + 0x4) + 0xe)) == 0x47) {
                                                                            r3 = 0x0;
                                                                    }
                                                                    else {
                                                                            r3 = 0x2;
                                                                    }
                                                            }
                                                            else {
                                                                    r3 = 0x2;
                                                            }
                                                    }
                                                    else {
                                                            r3 = 0x2;
                                                    }
                                            }
                                            else {
                                                    r3 = 0x2;
                                            }
                                    }
                                    else {
                                            r3 = 0x2;
                                    }
                            }
                            else {
                                    r3 = 0x2;
                            }
                    }else {
                            r3 = 0x2;
                    }
            } else {
                    r3 = 0x2;
            }
    }
    r0 = r3;
    return r0;
}