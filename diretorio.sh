#!/bin/bash
SHELL=/bin/sh
PATH=/sbin:/usr/sbin:/usr/bin:/bin

if ["/home/cimara/Documentos/PLP/Atv02/DirShell01" &&  "/home/cimara/Documentos/PLP/Atv02/DirShell02" ]
then
   echo " o diretorio ja existe"

else
   echo " o diretorio não existe criando..."

mkdir DirShell01 
mkdir DirShell02
fi

python operacoes.py

mv /home/cimara/Documentos/PLP/Atv02/DirShell01/operacoes.txt -t  /home/cimara/Documentos/PLP/Atv02/DirShell02
