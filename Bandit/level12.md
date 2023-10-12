# Level 12
Given Prompt: The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)

Setup
ssh `bandit12@bandit.labs.overthewire.org -p 2220`

`ls` current directory in `bandit12` to find `data.txt`

`cat data.txt` to find a hexdump that looks like:
```
00000000: 1f8b 0808 6855 1e65 0203 6461 7461 322e  ....hU.e..data2.
00000010: 6269 6e00 013d 02c2 fd42 5a68 3931 4159  bin..=...BZh91AY
00000020: 2653 5948 1b32 0200 0019 ffff faee cff7  &SYH.2..........
00000030: f6ff e4f7 bfbc ffff bff7 ffb9 39ff 7ffb  ............9...
00000040: bd31 eeff b9fb fbbb b9bf f77f b001 3b2c  .1............;,
00000050: d100 0d03 d200 6868 0d00 0069 a00d 0340  ......hh...i...@
00000060: 1a68 00d0 0d01 a1a0 0001 a680 0003 46d4  .h............F.
00000070: 6434 3234 611a 340d 07a4 c351 068f 5000  d424a.4....Q..P.
00000080: 069a 0680 0000 0006 8006 8da4 681a 6868  ............h.hh
00000090: 0d06 8d00 6834 3400 d07a 9a00 01a0 0341  ....h44..z.....A
000000a0: ea1e a190 da40 3d10 ca68 3468 6800 00c8  .....@=..h4hh...
000000b0: 1a1a 1b50 0683 d434 d069 a0d0 3100 d000  ...P...4.i..1...
000000c0: 001e a680 00d0 1a00 d0d0 6864 d0c4 d0d0  ..........hd....
000000d0: 000c 8641 7440 0108 032e 86b4 4cf0 22bb  ...At@......L.".
000000e0: 6682 2b7e b3e2 e98d aa74 dacc 0284 330d  f.+~.....t....3.
000000f0: bbb2 9494 d332 d933 642a 3538 d27e 09ce  .....2.3d*58.~..
00000100: 53da 185a 505e aada 6c75 59a2 b342 0572  S..ZP^..luY..B.r
00000110: 249a 4600 5021 25b0 1973 c18a 6881 1bef  $.F.P!%..s..h...
00000120: 3f9b 1429 5b1d 3d87 68b5 804f 1d28 42fa  ?..)[.=.h..O.(B.
00000130: 16c2 3241 98fb 8229 e274 5a63 fe92 3aca  ..2A...).tZc..:.
00000140: 70c3 a329 d21f 41e0 5a10 08cb 888f 30df  p..)..A.Z.....0.
00000150: f3da ce85 418b 0379 6a65 cfa2 eeb7 9f01  ....A..yje......
00000160: 782c da0e 288b e0c3 fe13 7af5 45ab 2b22  x,..(.....z.E.+"
00000170: a432 bf2f e32d b9e6 1465 2296 d805 a45e  .2./.-...e"....^
00000180: d1c1 eacb 7483 6aac ca0e cf24 8864 bd40  ....t.j....$.d.@
00000190: 118c 644a 1dc6 a127 375c b7a6 c124 bdae  ..dJ...'7\...$..
000001a0: 6d31 63a0 a223 3ea0 61d4 bdf0 450f 56fb  m1c..#>.a...E.V.
000001b0: a546 8d34 08a2 4f1d 43d3 9063 404d dd43  .F.4..O.C..c@M.C
000001c0: b4f2 e65d bcb7 5932 0f5e 6802 3892 a988  ...]..Y2.^h.8...
000001d0: 443d 8e89 7e09 4fb0 499d ee4e 4470 46c0  D=..~.O.I..NDpF.
000001e0: 2ba6 7c62 234a 7f76 151b aec0 23ee 4a97  +.|b#J.v....#.J.
000001f0: bc64 e34c de8a 5724 a1c3 9b89 cd96 1879  .d.L..W$.......y
00000200: d560 0cbb 5c26 09e4 efaf 5b94 402a 7780  .`..\&....[.@*w.
00000210: 4d87 30ce b8a3 946e 72c1 a643 1db7 a060  M.0....nr..C...`
00000220: 6524 629c 0c7e 8e7b e0f8 820c d5cb 60a0  e$b..~.{......`.
00000230: 003c a584 d4c1 61ef eb02 3f65 3a54 a3a2  .<....a...?e:T..
00000240: a565 c154 34c2 b162 d206 1ff8 bb92 29c2  .e.T4..b......).
00000250: 8482 40d9 9010 b3a9 e478 3d02 0000       ..@......x=...
```

run `xxd -r > data` to revert hexdump and redirect into `data`

`cat data` file to see someting like:
```
00000000: 3030 3030 3030 3030 3a20 3166 3862 2030  00000000: 1f8b 0
00000016: 3830 3820 3638 3535 2031 6536 3520 3032  808 6855 1e65 02
00000032: 3033 2036 3436 3120 3734 3631 2033 3232  03 6461 7461 322
00000048: 6520 202e 2e2e 2e68 552e 652e 2e64 6174  e  ....hU.e..dat
00000064: 6132 2e0a 3030 3030 3030 3130 3a20 3632  a2..00000010: 62
00000080: 3639 2036 6530 3020 3031 3364 2030 3263  69 6e00 013d 02c
00000096: 3220 6664 3432 2035 6136 3820 3339 3331  2 fd42 5a68 3931
00000112: 2034 3135 3920 2062 696e 2e2e 3d2e 2e2e   4159  bin..=...
00000128: 425a 6839 3141 590a 3030 3030 3030 3230  BZh91AY.00000020
00000144: 3a20 3236 3533 2035 3934 3820 3162 3332  : 2653 5948 1b32
00000160: 2030 3230 3020 3030 3139 2066 6666 6620   0200 0019 ffff 
00000176: 6661 6565 2063 6666 3720 2026 5359 482e  faee cff7  &SYH.
00000192: 322e 2e2e 2e2e 2e2e 2e2e 2e0a 3030 3030  2...........0000
00000208: 3030 3330 3a20 6636 6666 2065 3466 3720  0030: f6ff e4f7 
00000224: 6266 6263 2066 6666 6620 6266 6637 2066  bfbc ffff bff7 f
00000240: 6662 3920 3339 6666 2037 6666 6220 202e  fb9 39ff 7ffb  .
00000256: 2e2e 2e2e 2e2e 2e2e 2e2e 2e39 2e2e 2e0a  ...........9....
00000272: 3030 3030 3030 3430 3a20 6264 3331 2065  00000040: bd31 e
00000288: 6566 6620 6239 6662 2066 6262 6220 6239  eff b9fb fbbb b9
00000304: 6266 2066 3737 6620 6230 3031 2033 6232  bf f77f b001 3b2
(LINES CUT OFF FOR LENGTH)
```

running `file data` returns `data: gzip compressed data, was "data2.bin`

Sequence of Steps
1. `mv data data2.gz` and `gzip -d data2.gz` to get `data2`
2. `file data2` to get `data2: bzip2 compressed data, block size = 900k`
3. `mv data2 data2.bz` to rename
4. `bzip2 -d data2.bz` and `file data2` to get `data2: gzip compressed data, was "data4.bin"`
5. `mv data2 data4.gz`to rename
6. `gzip -d data4.gz` and `file data4` to get `data4: POSIX tar archive (GNU)`
7. `mv data4 data4.tar` and `tar -xf data4.tar` to find `data5.bin`
8. `mv data5.bin data5.tar`and `tar` again to get `data6.bin`
9. `mv data6.bin data6.tar` and tar again to get `data8.bin`
10. `file` to get `data8.bin: gzip compressed data, was "data9.bin`
11. Rename file once more, `gzip` and then `cat` file details to get password
End Result is something like:
`The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw`