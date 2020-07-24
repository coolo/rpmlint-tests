Name:		permissions2
Version:	0
Release:	0
Group:          Development/Tools/Building
Summary:	Lorem ipsum
License:	GPL-2.0+
BuildRoot:	%_tmppath/%name-%version-build
Url:            http://www.opensuse.org/
PreReq:         permissions

%description
Lorem ipsum dolor sit amet, consectetur adipisici elit, sed
eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
aliquid ex ea commodi consequat. Quis aute iure reprehenderit in
voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui
officia deserunt mollit anim id est laborum.

%prep
%build

%install
install -d -m 755 %buildroot/usr/bin
cp /bin/su %buildroot/usr/bin
cp /bin/su %buildroot/usr/bin/foo
printf '\0' >> %buildroot/usr/bin/foo
cp /bin/su %buildroot/usr/bin/bar
printf '\0\0' >> %buildroot/usr/bin/bar
# postfix and sendmail are allowed to install their own permissions file
mkdir -p %buildroot/etc/permissions.d %buildroot/usr/share/permissions/permissions.d
echo "/usr/bin/foo root:root 4755" > %buildroot/etc/permissions.d/postfix
echo "/usr/bin/bar root:root 4755" > %buildroot/usr/share/permissions/permissions.d/sendmail

%clean
rm -rf %buildroot

%verifyscript
%verify_permissions -e /usr/bin/su
%verify_permissions -e /usr/bin/foo
%verify_permissions -e /usr/bin/bar

%post
%set_permissions /usr/bin/su
%set_permissions /usr/bin/foo
%set_permissions /usr/bin/bar

%files
%defattr(-,root,root)
%attr(4755,root,root) /usr/bin/su
%attr(4755,root,root) /usr/bin/foo
%attr(4755,root,root) /usr/bin/bar
%config /etc/permissions.d/postfix
%attr(0600,root,root) /etc/permissions.d/postfix
%attr(0600,root,root) /usr/share/permissions/permissions.d/sendmail

%changelog
* Mon Apr 18 2011 lnussel@suse.de
- dummy
