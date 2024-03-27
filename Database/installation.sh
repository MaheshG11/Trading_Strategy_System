#!/bin/bash

sudo service mysql start
mysql Schema.sql
mysql sqlusersetup.sql
# RUN sudo mysql
# RUN ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Ghumare123@';
# RUN exit

