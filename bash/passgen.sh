#!/usr/bin/env sh

# Disclaimer: Password lists are harmful to make. What you do with them is up to you. Play nice.

# Print All arguments into password list
printf "$2\n$3\n$4\n$5\n$6\n$7\n$8\n$9\n${10}\n${11}" >> ~/passlst/$1 

# Run Python script that mangles the wordlist | sorts the new results | finds the unique lines | appends to password list
python2 ~/bin/makepasslist.py $2 $3 $4 $5 $6 $7 $8 $9 ${10} ${11} | sort | uniq | tee -a ~/passlst/$1;

# Get rid of any blank lines and re-write final list
#cat ~/passlst/$1 | sed '/^\s*$/d' > ~/passlst/$1;
cat ~/passlst/$1 | sed '/^\s*$/d' | tee $1

# Usage:
# Go into passlst dir and run script to generate the list correctly inside that dir.
# passgen usersName.lst dog cat fish 1975 Dylan Tom Kathy Dolphins 

# Now the password list has been generated

# Can run either of these commands with new list to use for attack vectors.
# john --stdout --wordlist=~/passlst/(passlist) --rules=(Single|KoreLogic)
# aircrack-ng -w - -b (bssid) (capture_file.cap)
