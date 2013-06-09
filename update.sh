#!/bin/bash

if [ "$1" == "-h" ]; then
	echo "Usage: `basename $0` --option"
	exit 0
fi

if [ "$1" == "a13" ]
then
	wget -O lib/external_gateway.py https://raw.github.com/xuancaishaun/fyp_test/v0/nep2p2_a13/external_gateway.py
	wget -O lib/scheduler.py https://raw.github.com/xuancaishaun/fyp_test/v0/nep2p2_a13/scheduler.py
	wget -O lib/app_worker.py https://raw.github.com/xuancaishaun/fyp_test/v0/nep2p2_a13/app_worker.py
	wget -O lib/gateway.py https://raw.github.com/xuancaishaun/fyp_test/v0/nep2p2_a13/gateway.py
	wget -O lib/appsocket.py https://raw.github.com/xuancaishaun/fyp_test/v0/nep2p2_a13/appsocket.py

	wget -O lib/util/logger.py https://raw.github.com/xuancaishaun/fyp_test/v0/logger.py

	wget -O statCollect.py https://raw.github.com/xuancaishaun/fyp_test/v0/statCollect.py
	wget -O run.py https://raw.github.com/xuancaishaun/fyp_test/v0/nep2p2_a13/run.py
	wget -O cli.py https://raw.github.com/xuancaishaun/fyp_test/v0/nep2p2_a13/cli.py
	wget -O ddM16m8r92TO.txt https://raw.github.com/xuancaishaun/fyp_test/v0/ddM16m8r92TO.txt

elif [ "$1" == "a17" ] || [ "$1" == 'a17_rudp' ]
then
	wget -O lib/external_gateway.py https://raw.github.com/xuancaishaun/fyp_test/v0/external_gateway.py
	wget -O lib/internal_gateway.py https://raw.github.com/xuancaishaun/fyp_test/v0/internal_gateway.py
	wget -O lib/scheduler.py https://raw.github.com/xuancaishaun/fyp_test/v0/scheduler.py
	wget -O lib/app_worker.py https://raw.github.com/xuancaishaun/fyp_test/v0/app_worker.py
	wget -O lib/gateway.py https://raw.github.com/xuancaishaun/fyp_test/v0/gateway.py
	wget -O lib/appsocket.py https://raw.github.com/xuancaishaun/fyp_test/v0/appsocket.py
	wget -O lib/connection.py https://raw.github.com/xuancaishaun/fyp_test/v0/connection.py
	wget -O lib/batch_acknowledger.py https://raw.github.com/xuancaishaun/fyp_test/v0/batch_acknowledger.py
	

	wget -O lib/util/logger.py https://raw.github.com/xuancaishaun/fyp_test/v0/logger.py
	wget -O lib/util/ip.py https://raw.github.com/xuancaishaun/fyp_test/v0/ip.py
	wget -O lib/util/bmessage.py https://raw.github.com/xuancaishaun/fyp_test/v0/bmessage.py

	wget -O statCollect.py https://raw.github.com/xuancaishaun/fyp_test/v0/statCollect.py
	wget -O run.py https://raw.github.com/xuancaishaun/fyp_test/v0/run.py
	wget -O cli.py https://raw.github.com/xuancaishaun/fyp_test/v0/cli.py
	wget -O ddM16m8r92TO.txt https://raw.github.com/xuancaishaun/fyp_test/v0/ddM16m8r92TO.txt

	if [ "$1" == "a17_rudp" ]
	then
		wget -O lib/appsocket.py https://raw.github.com/xuancaishaun/fyp_test/v0/nep2p2_rudp/appsocket.py
		wget -O lib/gateway.py https://raw.github.com/xuancaishaun/fyp_test/v0/nep2p2_rudp/gateway.py
		wget -O lib/rudp.py https://raw.github.com/xuancaishaun/fyp_test/v0/nep2p2_rudp/rudp.py
		wget -O run.py https://raw.github.com/xuancaishaun/fyp_test/v0/nep2p2_rudp/run.py
	fi
elif [ "$1" == "a17_rudp_to_a17" ]
then
	wget -O lib/gateway.py https://raw.github.com/xuancaishaun/fyp_test/v0/gateway.py
	wget -O lib/appsocket.py https://raw.github.com/xuancaishaun/fyp_test/v0/appsocket.py

elif [ "$1" == "a13_to_a17" ]
then
	sudo yum install libffi
	sudo yum install libffi-devel
	export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig/
	wget -O cffi-0.6.tar.gz https://www.dropbox.com/s/5zazoqua7nf31t4/cffi-0.6.tar.gz
	tar -zxf cffi-0.6.tar.gz
	cd cffi-0.6
	python setup.py build
	sudo python setup.py install
	cd ..
	wget -O nep2p2_a16.zip https://www.dropbox.com/s/sanoagaumn9iyd8/nep2p2_a16.zip
	sudo yum install unzip
	unzip nep2p2_a16.zip
	sudo rm -r __MACOSX
	sudo rm -r bats_clean
	cp fyp_nep2p/libbatscore.so nep2p2_ms3/

elif [ "$1" == "gevent_upgrade" ]
then
	sudo yum install git
	sudo pip install greenlet==dev
	sudo pip install cython -e git://github.com/surfly/gevent.git#egg=gevent
fi
