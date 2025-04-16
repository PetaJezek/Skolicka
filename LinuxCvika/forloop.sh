#!/bin/sh

usage() {
    echo "Usage: $1 [-V] [-o filename] [-h] input [files]"
    echo " -V          Print program version and terminate."
    echo " -o filename Store output into filename instead to stdout."
    echo " -h          Print this help and exit."
}

output_file="/dev/stdout"
print_version=false

while getopts "Vho:" opt; do
    case "$opt" in
        h)
            usage "$0"
            exit 0
            ;;
        V)
            print_version=true
            ;;
        o)
            output_file="$OPTARG"
            ;;
        *)
            usage "$0" >&2;
            exit 1
            ;;
    esac
done
shift $(( OPTIND - 1))

if $print_version; then
    echo "My script, version 0.0.1"
    exit 0
fi

cat "$@" | pandoc -t html >"$output_file"
