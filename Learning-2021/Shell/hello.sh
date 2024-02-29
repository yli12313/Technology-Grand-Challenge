#!/bin/bash

###############
## Important ##
###############

# - Must always put '$' before using a variable!
# - Must always put '$' before using a variable!
# - Must always put '$' before using a variable!
# - Must always put '$' before using a variable!

# # - hash
# ! - bang

#################
## (1) and (2) ##
#################
# this is a comment

# echo "Hello World" # this is also a comment


# echo "Our shell name is $BASH"
# echo "Our shell version name is $BASH_VERSION"
# echo "Our home directory is $HOME"
# echo "Our current working directory is $PWD"

# name=Mark
# VALUE=10
# echo "The name is $name"
# echo "value $VALUE"

#########
## (3) ##
#########

# echo "Enter names : "
# read name1 name2 name3
# echo "Entered names : $name1, $name2, $name3"

# read -p "username : " user_var
# read -sp "password : " pass_var
# echo
# echo "username : $user_var"
# echo "password : $pass_var"

# echo "Enter names : "
# read
# echo "Name : $REPLY"

#########
## (4) ##
#########
# echo $0 $1 $2 $3 ' > echo $1 $2 $3'

# args=("$@")

# Array: 0 index is for the first argument
# echo ${args[0]} ${args[1]} ${args[2]}

# echo $@
# echo $#

#########
## (5) ##
#########

# Expressions
# An expression can be: String comparison, Numeric comparison, File operators and Logical operators and it is represented by [expression]:
# String Comparisons:  
# ---------------------------------
# =  compare if two strings are equal
# !=  compare if two strings are not equal
# -n  evaluate if string length is greater than zero
# -z  evaluate if string length is equal to zero

# Examples:
# [ s1 = s2 ]  (true if s1 same as s2, else false)
# [ s1 != s2 ]  (true if s1 not same as s2, else false)
# [ s1 ]   (true if s1 is not empty, else false)
# [ -n s1 ]   (true if s1 has a length greater then 0, else false)
# [ -z s2 ]   (true if s2 has a length of 0, otherwise false)

# (Extra Stuff)
# = - is equal to - if [ "$a" = "$b" ]
# == - is equal to - if [ "$a" == "$b" ]
# != - is not equal to - if [ "$a" != "$b" ]
# < - is less than, in ASCII alphabetical order - if [[ "$a" < "$b" ]]
# > - is greater than, in ASCII alphabetical order - if [[ "$a" > "$b" ]]
# -z - string is null that is, has zero length - if [ -z "$String" ]
# -n - string is not null - if [ -n "$String" ]

# Number Comparisons:
# ------------------------------------
# -eq compare if two numbers are equal
# -ge compare if one number is greater than or equal to a number
# -le compare if one number is less than or equal to a number
# -ne compare if two numbers are not equal
# -gt compare if one number is greater than another number
# -lt compare if one number is less than another number

# Examples:
# [ n1 -eq n2 ]  (true if n1 same as n2, else false) (==)
# [ n1 -ge n2 ]  (true if n1greater then or equal to n2, else false) (>=)
# [ n1 -le n2 ]  (true if n1 less then or equal to n2, else false) (<=)
# [ n1 -ne n2 ]  (true if n1 is not same as n2, else false) (!=)
# [ n1 -gt n2 ]  (true if n1 greater then n2, else false) (>)
# [ n1 -lt n2 ]  (true if n1 less then n2, else false) (<)

# -eq : ==
# -ge : >=
# -le : <=
# -ne : !=
# -gt : >
# -lt : <

###########################################################
## Take note of the double parentheses! Only for Integer ##
## comparisons where <, <=, >, >= are used!)             ##
###########################################################

# < - is less than - (( "$a" < "$b" ))
# <= - is less than or equal to - (( "$a" <= "$b" ))
# > - is greater than - (("$a" > "$b"))
# >= - is greater than or equal to - (("$a" >= "$b"))

########

# word=c

# if [[ $word == "b" ]]
# then
# echo "condition b is true"
# elif [[ $word == "a" ]]
# then
# echo "condition a is true"
# else
# echo "condition is false"
# fi

####

# word='e'

# if [ -n $word ]; then
# echo "Word is not null!"
# elif  [[ $word =~ ^[0-9]+$ ]]; then
# echo "A number!"
# else
# echo "Word is null!"
# fi

#########
## (6) ##
#########

# echo -e "Enter the name of the file : \c"
# read file_name

# if [ -e $file_name ]; then (Checks if file exists)
# if [ -f $file_name ]; then (Checks for a normal file)
# if [ -d $file_name ]; then (Checks for directory)
# if [ -s $file_name ]; then
# echo "$file_name not empty"
# else
# echo "$file_name empty"
# fi

#########
## (7) ##
#########

# echo -e "Enter the name of the file : \c"
# read file_name

# if [ -f $file_name ]; then
# if [ -w $file_name ]; then
# echo "Type some text data. To quit press ctrl+d"
# cat >> $file_name
# else
# echo "The file do not have write permissions"
# fi
# else
# echo "$file_name not exists"
# fi

#########
## (8) ##
#########

# age=60

# if [ "$age" -gt 18 -a "$age" -lt 30 ]; then
# echo "valid age"
# else
# echo "age not valid"
# fi

#########
## (9) ##
#########

# age=25

# if [[ "$age" -eq 18 || "$age" -eq 30 ]]; then
# echo "valid age"
# else
# echo "age not valid"
# fi

##########
## (10) ##
##########

# num1=20
# num2=5

# echo $(( num1 + num2 ))
# echo $(( num1 - num2 ))
# echo $(( num1 * num2 ))
# echo $(( num1 / num2 ))
# echo $(( num1 % num2 ))

# echo $( expr $num1 + $num2 )
# echo $( expr $num1 - $num2 )
# echo $( expr $num1 \* $num2 )
# echo $( expr $num1 / $num2 )
# echo $( expr $num1 % $num2 )

##########
## (11) ##
##########

# num1=20.5
# num2=5

# echo "$num1+$num2" | bc
# echo "$num1-$num2" | bc
# echo "20.5*5" | bc
# echo "scale=20;20.5/5" | bc
# echo "20.5%5" | bc

# num=4

# echo "scale=2;sqrt($num)" | bc -l
# echo "scale=2;3^3" | bc -l

##########
## (12) ##
##########

# case expression in
# pattern1 )
# statements ;;
# pattern2 )
# statements ;;
# ...
# esac

# vehicle=$1

# case $vehicle in
# "car" )
# echo "Rent of $vehicle is 100 dollar" ;;
# "van" )
# echo "Rent of $vehicle is 80 dollar" ;;
# "bicycle" )
# echo "Rent of $vehicle is 5 dollar" ;;
# "truck" )
# echo "Rent of $vehicle is 150 dollar" ;;
# * )
# echo "Unknown vehicle" ;;
# esac

##########
## (13) ##
##########

# echo -e "Enter some character : \c"
# read value

# case $value in
# [a-z] )
# echo "User entered $value a to z" ;;
# [A-Z] )
# echo "User entered $value A to Z" ;;
# [0-9] )
# echo "User entered $value 0 to 9" ;;
# ? )
# echo "User entered $value special character" ;;
# * )
# echo "Unknown input" ;;
# esac

##########
## (14) ##
##########

# os=('ubuntu' 'windows' 'kali')
# os[3]='mac'
# os[0]='hp'
# os[6]='mac'

# unset os[2]

# echo "${os[@]}" # Print elements of array
# echo "${os[0]}"
# echo "${os[1]}"
# echo "${os[5]}"
# echo "${os[6]}"
# echo "${!os[@]}" # Indices of array
# echo "${#os[@]}" # Length of array

# string=ejfjef2i3rj # Can treat variable as array, but it is assigned to the 0th index
# echo "${string[@]}"
# echo "${string[0]}"
# echo "${string[1]}"
# echo "${#os[@]}"

##########
## (15) ##
##########

# while loops
# n=1

# # 1) while [ $n -le 10 ]
# while (( $n <= 10 ))
# do
# echo "$n"
# # 1) n=$(( n+1 ))
# # 2) (( $n+1 ))
# # 3) (( n++ ))
# (( ++n ))
# done

##########
## (16) ##
##########

# while loops
# n=1

# while [ $n -le 3 ]
# do
# echo "$n"
# (( n++ ))
# sleep 1
# done

# while [ $n -le 3 ]
# do
# echo "$n"
# (( n++ ))
# gnome-terminal &
# done

##########
## (17) ##
##########

# while IFS=' ' read -r line
# do
# echo $line
# done < /etc/host

##########
## (18) ##
##########
# until loops
# n=1

# until [ $n -ge 10 ]
# do
# echo $n
# n=$(( n+1 ))
# done

# until [ $n -gt 10 ]
# do
# echo $n
# n=$(( n+1 ))
# done

# until (( $n > 10 ))
# do
# echo $n
# n=$(( n+1 ))
# done

# until (( $n > 10 ))
# do
# echo $n
# n=$(( n++ ))
# done


##########
## (19) ##
##########
# for loops

# for i in 1 2 3 4 5
# do
# echo $i
# done

# for i in {1..10}
# do
# echo $i
# done

# Cannot be used for any bash version < 4
# for i in {0..10..2}
# do
# echo $i
# done

# for i in ${BASH_VERSION}
# do
# echo $i
# done

# for (( i=0; i<5; i++ ))
# do
# echo $i
# done

##########
## (20) ##
##########
# for loops

# for command in ls pwd date
# do
# echo "-----$command-----"
# $command
# done

# for item in *
# do
# if [ -f $item ]; then
# echo $item
# fi
# done

##########
## (21) ##
##########
# select loop

# select name in mark john tom ben
# do
# case $name in
# mark)
# echo mark selected
# ;;
# john)
# echo john selected
# ;;
# tom)
# echo tom selected
# ;;
# ben)
# echo ben selected
# ;;
# *)
# echo "Error please provide the number between 1..4"
# esac
# done

##########
## (22) ##
##########
# for (( i=1; i<=10; i++ ))
# do
# if [ $i -gt 5 ]; then
# break
# fi
# echo "$i"
# done

# for (( i=1; i<=10; i++ ))
# do
# if [[ $i -eq 3 || $i -eq 6 ]]; then
# continue
# fi

# echo "$i"
# done

##########
## (23) ##
##########

# function name(){
# Commands
# }

# name () {
# Commands
# }

# function print(){
# echo $1 $2 $3
# }


# quit () {
# exit
# }

# print Hello World Again

# echo "foo"
# quit

##########
## (24) ##
##########

# function print(){
# local name=$1
# echo "The name is $name"
# }

# name="Tom"
# echo "The name is $name : Before"

# print Max
# echo "The name is $name : After"

##########
## (25) ##
##########

#!/bin/bash

# usage() {
# 	echo "You need to provide an argument : "
# 	echo "usage : $0 file_name"
# }

# is_file_exist() {
# 	local file="$1"
# 	[[ -f "$file" ]] && return 0 || return 1
# }

# [[ $# -eq 0 ]] && usage

# if ( is_file_exist "$1" )
# then
# 	echo "File found"
# else
# 	echo "File not found"
# fi

##########
## (26) ##
##########

# var=31

# readonly var

# var=50

# echo "var => $var"

# hello() {
# 	echo "Hello World"
# }

# readonly -f hello

# hello() {
# 	echo "Hello World Again"
# }

# readonly -f

##########
## (27) ##
##########

# set -x
# file=/Users/yingquanli/Work/shell/file.txt
# set +x

# trap "rm -f $file && echo file deleted; exit" 0 2 9 15

# echo "pid is $$"
# while (( COUNT < 10 ))
# do
# 	sleep 10
# 	(( COUNT ++ ))
# 	echo $COUNT
# done
# exit 0

# trap "echo Exit command is detected" 0

# echo "Hello world"

# exit 0

##########
## (28) ##
##########

# bash -x ./hello.sh

#!/bin/bash -x

# set -x
# set +x
