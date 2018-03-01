LIST=$1

. ./cpu_mem_check.sh ${LIST} >> testwoo1010.txt

rcp -p testwoo1010.txt root@VCSYSTS1577:/root/environments/my_env/static/
rsh -x -l root '. ./environments/my_env/bin/activate'
rsh -x -l root 'python text-to-excel.py testwoo1010.txt'

. ./environments/my_env/bin/activate | python environments/my_env/static/text-to-excel.py testwoo1010.txt