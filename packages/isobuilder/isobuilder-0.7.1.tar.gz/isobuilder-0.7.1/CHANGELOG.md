# isolinux Changelog

## 22-10-2024 0.7.1
* Use chpasswd to update the root password

## 21-10-2024 0.7.0
* Update to use autoinstall and cloud-init instead of d-i to customise the install

## 08-07-2024 0.6.1
* Ensure we refresh the nodes repo before reading files

## 08-07-2024 0.6.0
* Add support for determining the partman disk based on disk model

## 02-07-2024 0.5.2
* update md5sum.txt

## 02-07-2024 0.5.1
* Add new partitions /media/sdcard /media/boss
* fix up late_command to make debugging easier

## 16-04-2024 0.5.0
* Add additional preseed commands to prevent further questions

## 16-04-2024 0.4.9
* Fix the partitioning so that we always have some space left in the volume group

## 16-04-2024 0.4.8
* Increase /usr and /var partitions to be 8G by default

## 16-04-2024 0.4.7
* This is actually just 0.4.6

## 06-02-2024 0.4.6
* Drop rsync in-place

## 06-02-2024 0.4.5
* 0.4.4 did not include the MR and is really just 0.4.3

## 06-02-2024 0.4.4
* Update to use unique location for souce mount and build dir

## 06-02-2024 0.4.3
* move back to using ttyS1 as we changes things in the BIOS

## 06-02-2024 0.4.2
* Fix serial device which is ttyS0 at least with some of the newer servers

## 06-02-2024 0.4.1
* Fix up kickstarter file
* use UEFI partition schema

## 05-02-2024 0.4.0
* Fix kernel line
* add preseed/early_command string umount /media.  work around a bug where sda1 
  is mounted to media
* Change rsync chmod to u+w
* moved configuration to preseed

## 01-02-2024 0.3.3
* Ad serial redirection to grub config

## 01-02-2024 0.3.2
* update rsync add -a back to rsync

## 01-02-2024 0.3.1
* update rsync to use chmod=0777 to make it easir to update the files

## 01-02-2024 0.3.0
* update to work with UEFI and grub2

## 01-02-2024 0.2.1
* Add "partman/unmount\_active boolean true" to preseed

## 24-01-2024 0.1.3
* Add support for config file

## 24-01-2024 0.1.2
* Inline the authorized key directly in the late comand
* Bug: use dnsops folder not dns0ps

## 22-01-2024 0.1.1
* improve help message

## 22-01-2024 0.1.0
* Add logging

## 22-01-2024 0.0.9
* bug: use chmod on isolinux not write_text

## 22-01-2024 0.0.8
* ensure permissions are correct after rsync part 2

## 22-01-2024 0.0.7
* ensure permissions are correct after rsync

## 22-01-2024 0.0.6
* cleanly unmount iso after finsh

## 22-01-2024 0.0.5
* Fix minor typos and copy/paste errors

## 22-01-2024 0.0.4
* update get_args to handles passing args correctly

## 22-01-2024 0.0.3
* update script name

## 22-01-2024 0.0.2
* Add change log
