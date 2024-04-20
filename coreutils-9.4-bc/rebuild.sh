#!/bin/bash
rm nohup*
rm -rf result_all
cd ../../recolossus/krpk
cargo build
cd ../../recolossus/build
ninja klee
cd /home/user/coreutils-test/coreutils-9.4-bc


# /home/user/recolossus/build/bin/klee --recolossus --max-solver-time=30 --search=bfs --external-calls=all --libc=uclibc --posix-runtime -max-time=600 