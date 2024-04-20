PROGRAM_PATH="fold"
MAX_TIME="30min"
EXTERNAL_FUNCTION="memchr,memcpy,memset,strchr,strcoll,strcspn,strlen,strncmp,strpbrk,strspn,strtok,memcmp,memmove,strcat,strcmp,strcpy,strerror,strncat,strncpy,strrchr,strstr,strxfrm"

/home/user/recolossus/build/bin/klee \
    --max-solver-time=30s \
    --recolossus \
    --recolossus-range=fold.c,getopt.c \
    --recolossus-external-function=${EXTERNAL_FUNCTION}\
    --max-fuzz-solver-time=10s \
    --search=bfs \
    --libc=uclibc --posix-runtime \
    --watchdog --max-time=${MAX_TIME}  \
    --output-dir=klee-${PROGRAM_PATH}-colossus-getopt-fixed\
    --external-calls=all \
    --only-output-states-covering-new \
    ../bcfiles/${PROGRAM_PATH}.bc --sym-args 0 1 10 --sym-args 0 2 7 --sym-files 1 8 --sym-stdin 8 --sym-stdout


