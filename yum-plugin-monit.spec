Name:      yum-plugin-monit
Version:   0.1
Release:   1%{?dist}
Summary:   Integrates monit with yum
Source:    https://github.com/sjinks/yum-plugin-monit/archive/0.1.tar.gz
Group:     Unspecified
License:   MIT
BuildArch: noarch
Requires:  monit yum /usr/bin/systemctl

%description
Stops monit before an RPM transaction and starts it afterwards
to make sure that monit will not interfere with the update process.

%prep
%setup

%build

%install
%{__install} -m 0644 -p -D monit.py "%{buildroot}%{_prefix}/lib/yum-plugins/monit.py"
%{__install} -m 0644 -p -D monit.conf "%{buildroot}%{_sysconfdir}/yum/pluginconf.d/monit.conf"

%files
%defattr(-, root, root, -)
#%doc GPL INSTALL TODO README
%dir %{_prefix}/lib/yum-plugins
%dir %{_sysconfdir}/yum/pluginconf.d
%{_prefix}/lib/yum-plugins/monit.*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/monit.conf

%changelog
* Wed Jun 13 2018 Volodymyr Kolesnykov <volodymyr@wildwolf.name> - 0.1-1
- Initial release
