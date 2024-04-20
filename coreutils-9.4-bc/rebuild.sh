#!/bin/bash

cd /home/user/recolossus/krpk
cargo build --release

cd /home/user/recolossus/build
ninja klee -j8
