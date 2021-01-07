{
    "targets": [
        {
            "target_name": "multihashing",
            "sources": [
                "src/multihashing.cc",
                "src/bcrypt.c",
                "src/blake.c",
                "src/boolberry.cc",
                "src/c11.c",
                "src/cryptonight.c",
		"src/cryptonight_fast.c",
                "src/fresh.c",
                "src/fugue.c",
                "src/groestl.c",
                "src/hefty1.c",
                "src/keccak.c",
                "src/lbry.c",
                "src/lyra2re.c",
                "src/lyra2z.c",
                "src/nist5.c",
                "src/quark.c",
                "src/qubit.c",
                "src/scryptjane.c",
                "src/scryptn.c",
                "src/sha1.c",
                "src/sha256d.c",
                "src/shavite3.c",
                "src/skein.c",
                "src/x11.c",
                "src/x13.c",
                "src/x15.c",
                "src/x16r.c",
                "src/x16rv2.c",
                "src/sha3/sph_hefty1.c",
                "src/sha3/sph_fugue.c",
                "src/sha3/aes_helper.c",
                "src/sha3/sph_blake.c",
                "src/sha3/sph_bmw.c",
                "src/sha3/sph_cubehash.c",
                "src/sha3/sph_echo.c",
                "src/sha3/sph_groestl.c",
                "src/sha3/sph_jh.c",
                "src/sha3/sph_keccak.c",
                "src/sha3/sph_luffa.c",
                "src/sha3/sph_shavite.c",
                "src/sha3/sph_simd.c",
                "src/sha3/sph_skein.c",
                "src/sha3/sph_whirlpool.c",
                "src/sha3/sph_shabal.c",
                "src/sha3/sph_ripemd.c",
                "src/sha3/sph_sha1.c",
                "src/sha3/sph_sha2.c",
                "src/sha3/sph_sha2big.c",
                "src/sha3/sph_tiger.c",
                "src/sha3/hamsi.c",
                "src/crypto/lyra2.c",
                "src/crypto/sponge.c",
                "src/crypto/oaes_lib.c",
                "src/crypto/c_keccak.c",
                "src/crypto/c_groestl.c",
                "src/crypto/c_blake256.c",
                "src/crypto/c_jh.c",
                "src/crypto/c_skein.c",
                "src/crypto/hash.c",
                "src/crypto/aesb.c",
                "src/crypto/sha256.c",
                "src/crypto/wild_keccak.cpp",
                "src/neoscrypt.c",
                "src/crypto/yescrypt/yescrypt-best.c",
                "src/crypto/yescrypt/yescryptcommon.c",
            ],
            "include_dirs": [
                "src/crypto",
                "<!(node -e \"require('nan')\")"
            ],
            "cflags_cc": [
                "-std=c++11"
            ],
        }
    ]
}
