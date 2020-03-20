#!/bin/sh
sudo apt update
sudo apt install -y gpg

echo Make sure to use Curve25519!!!
gpg --full-generate-key --expert

key=`gpg --list-secret-keys --keyid-format LONG | grep sec |  awk -v OFS='\t' '{print $2}' | awk -F/ '{print $NF}'`
echo Your new key is ${key}

git config --global user.signingkey $key
git config --global commit.gpgsign true

echo "Please paste this into github:"

gpg --armor --export $key
