1. the "testservice.service" should be created in the path /etc/sytemd/system/ with root permission

2. create the sample.sh file in the location of your choice with the correct file permission. File permission
   can be set by using chmod 677 "filename" (677 modify as per permission you want to set)

3. After created the files mentioned in point one and two, go ahead and enable the service with the following commands

  reload daemon
  
  $sudo systemctl daemon-reload

  enable the service
  
  $sudo systemctl enable testservice.service

  to disable the service

  $sudo systemctl disable testservice.service

  Note: On very modification of the file "testservice.service" use the following commands
  
  $sudo systemctl daemon-reload
  $sudo systemctl restart testservice.service

3. You can also use a timer to similar affect and control when to start the service. Refer to minitest.timer

   $sudo systemctl disable testservice.service
   $sudo systemctl enable minitest.timer


Other details: reference link

https://www.linux.com/training-tutorials/writing-systemd-services-fun-and-profit/


https://www.linux.com/training-tutorials/systemd-services-beyond-starting-and-stopping/


https://www.linux.com/topic/desktop/setting-timer-systemd-linux/

