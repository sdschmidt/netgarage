#!/bin/bash

echo 'Hallo'
read -p 'Enter the 3 digit passcode to enter: ' numbers
if [ $numbers == 123 ]; then
  echo 'passcode'
fi
