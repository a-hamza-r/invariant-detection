#!/bin/bash

display_usage() {
	echo "Provide required arguments"
	echo "Usage: $0 benchmark_name num_of_traces"
	echo ""
	echo "benchmark_name : directory name for the benchmark to run. this would correspond to the c file name in that directory"
	echo "num_of_traces : number of traces you want to use for the algorithm"
	echo "exiting..."
}

if [ "$#" -le 1 ]
then 
	display_usage
	exit 1
fi

benchmark=$1
num_of_traces=$2

for ((i=1;i<=$num_of_traces;i++))
do
	gcc -gdwarf-2 -no-pie "$benchmark/$benchmark.c" -o "$benchmark/$benchmark$i"
	if [ ! -d "$benchmark/daikon-output" ]
	then
		mkdir "$benchmark/daikon-output"
	fi
	kvasir-dtrace --dtrace-file="$benchmark/daikon-output/$benchmark$i.dtrace" --decls-file="$benchmark/daikon-output/$benchmark$i.decls" "$benchmark/$benchmark$i"
	if [ -d "$daikon-output" ]
	then
		rmdir "daikon-output"
	fi
done
