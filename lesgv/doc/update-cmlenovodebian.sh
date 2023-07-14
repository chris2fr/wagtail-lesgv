# set -e
source /home/mannchri/wagtail/venv/bin/activate
startdir=`pwd`
workdir=/home/mannchri/wagtail/wagtail-lesgv
scriptdir=/home/mannchri/wagtail/wagtail-lesgv/lesgv/doc
for command in 001 002 003 004 005 006 007
do
  echo "----------------------------------------------------------------------------------------"
  echo " DO $command `cat $scriptdir/update-cmlenovodebian/$command.sh`"
  echo "-' '--' '--' '--' '--' '--' '--' '--' '--' '--' '--' '--' '--' '--' '--' '--' '--' '--' "
  cd $workdir
  source $scriptdir/update-cmlenovodebian/$command.sh
  echo "-. .--. .--. .--. .--. .--. .--. .--. .--. .--. .--. .--. .--. .--. .--. .--. .--. .--. "
  echo "DONE update-cmlenovodebian/$command.sh"
  echo "========================================================================================"
done
cd $startdir


