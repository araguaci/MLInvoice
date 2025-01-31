Name:		mlinvoice
Version:	2.1.1
Release:	1%{?dist}
Summary:	MLInvoice - Web application to create Finnish invoices
Group:		Applications/Internet
License:	GPLv2
URL:		http://www.labs.fi/
Source0:	%{name}-%{version}%{?prever}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Obsoletes: vllasku

BuildRequires:	httpd
Requires:	httpd
Requires:	php >= 7.3.5
%if 0%{?el5}
Requires:	php-pecl-json
%endif
Requires:	php-mbstring
Requires: php-xml
Requires: php-xsl
Requires: php-mysqli
BuildArch:	noarch

%description
MLInvoice is a web application written in PHP for handling offers, dispatch notes,
invoices etc.
It is available in English, Finnish and Swedish. Among its features
are automatic invoice numbering and reference calculation, pdf
generation, Finvoice support, customer database and unlimited number of user
accounts. Data is stored in a MySQL database.

%prep
%setup -q -n %{name}-%{version}%{?prever}

%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__install} -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d

cat > $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/%{name}.conf <<EOM

Alias /%{name} %{_datadir}/%{name}

<Location /%{name}>
AddDefaultCharset UTF-8
php_value include_path      ".:%{_sysconfdir}/%{name}"
</Location>
EOM

%{__install} -d -m755 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
%{__install} -d -m755 $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__install} -m644 *.php *.ico *.xsl *.xsd config.php.sample $RPM_BUILD_ROOT%{_datadir}/%{name}
%{__cp} -a css datatables db_data fonts images js lang select2 send_api tests themes vendor $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE README.md create_database.sql update_database_1.0_to_1.1.sql update_database_1.1_to_1.2.sql update_database_1.2_to_1.3.sql update_database_1.3_to_1.4.sql update_database_1.4_to_1.5.sql
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%attr(2755,root,apache) %dir %{_sysconfdir}/%{name}
%{_datadir}/%{name}

%changelog
* Tue 28 Feb 2023 Ere Maijala <ere@labs.fi> - 2.1.1
- updated for version 2.1.1
* Sat 26 Nov 2022 Ere Maijala <ere@labs.fi> - 2.1.0
- updated for version 2.1.0
* Sat 19 Feb 2022 Ere Maijala <ere@labs.fi> - 2.0.2
- updated for version 2.0.2
* Sun 2 Jan 2022 Ere Maijala <ere@labs.fi> - 2.0.1
- updated for version 2.0.1
* Sun 31 Oct 2021 Ere Maijala <ere@labs.fi> - 2.0.0
- updated for version 2.0.0
* Sun 31 Oct 2021 Ere Maijala <ere@labs.fi> - 1.23.1
- updated for version 1.23.1
* Tue 19 Oct 2021 Ere Maijala <ere@labs.fi> - 1.23.0
- updated for version 1.23.0
* Mon 18 Oct 2021 Ere Maijala <ere@labs.fi> - 1.22.0
- updated for version 1.22.0
* Sat 31 Aug 2019 Ere Maijala <ere@labs.fi> - 1.21.2
- updated for version 1.21.2
* Wed 21 Aug 2019 Ere Maijala <ere@labs.fi> - 1.21.1
- updated for version 1.21.1
* Sat 17 Aug 2019 Ere Maijala <ere@labs.fi> - 1.21.0
- updated for version 1.21.0
* Tue Apr 30 2019 Ere Maijala <ere@labs.fi> - 1.20.5
- updated for version 1.20.5
* Thu Apr 4 2019 Ere Maijala <ere@labs.fi> - 1.20.4
- updated for version 1.20.4
* Tue Apr 2 2019 Ere Maijala <ere@labs.fi> - 1.20.3
- updated for version 1.20.3
* Sun Mar 31 2019 Ere Maijala <ere@labs.fi> - 1.20.2
- updated for version 1.20.2
* Mon Mar 25 2019 Ere Maijala <ere@labs.fi> - 1.20.1
- updated for version 1.20.1
* Sat Mar 23 2019 Ere Maijala <ere@labs.fi> - 1.20.0
- updated for version 1.20.0
- fix included files and directories
- stop copying config.php.sample so that initial setup is executed
* Fri Sep 7 2018 Ere Maijala <ere@labs.fi> - 1.19.0
- updated for version 1.19.0
* Sat Jun 30 2018 Ere Maijala <ere@labs.fi> - 1.18.1
- updated for version 1.18.1
* Wed Jun 6 2018 Ere Maijala <ere@labs.fi> - 1.18.0
- updated for version 1.18.0
* Tue Feb 27 2018 Ere Maijala <ere@labs.fi> - 1.17.0
- updated for version 1.17.0
* Fri Dec 22 2017 Ere Maijala <ere@labs.fi> - 1.16.1
- updated for version 1.16.1
* Wed Dec 20 2017 Ere Maijala <ere@labs.fi> - 1.16.0
- updated for version 1.16.0
* Fri Sep 22 2017 Ere Maijala <ere@labs.fi> - 1.15.5
- updated for version 1.15.5
* Sun Aug 20 2017 Ere Maijala <ere@labs.fi> - 1.15.4
- updated for version 1.15.4
* Wed Jul 5 2017 Ere Maijala <ere@labs.fi> - 1.15.3
- updated for version 1.15.3
* Tue Jun 20 2017 Ere Maijala <ere@labs.fi> - 1.15.2
- updated for version 1.15.2
* Sat Jun 13 2017 Ere Maijala <ere@labs.fi> - 1.15.1
- updated for version 1.15.1
* Sat May 23 2017 Ere Maijala <ere@labs.fi> - 1.15.0
- updated for version 1.15.0
* Fri May 26 2017 Ere Maijala <ere@labs.fi> - 1.15.0-beta1-1
- updated for version 1.15.0-beta1
* Sun Mar 26 2017 Ere Maijala <ere@labs.fi> - 1.14.2-1
- updated for version 1.14.2
* Sat Mar 18 2017 Ere Maijala <ere@labs.fi> - 1.14.1-1
- updated for version 1.14.1
- removed copying of tcpdf directory
- added copying of vendor directory
* Sun Mar 5 2017 Ere Maijala <ere@labs.fi> - 1.14.0-1
- updated for version 1.14.0
* Sun Apr 3 2016 Ere Maijala <ere@labs.fi> - 1.13.0-1
- updated for version 1.13.0
- removed php-mysql from dependencies since only php-mysqli is used
* Thu Dec 31 2015 Ere Maijala <ere@labs.fi> - 1.12.2-1
- updated for version 1.12.1
* Wed Dec 23 2015 Ere Maijala <ere@labs.fi> - 1.12.1-1
- updated for version 1.12.1
* Sun Dec 6 2015 Ere Maijala <ere@labs.fi> - 1.12.0-1
- updated for version 1.12.0
* Sat Mar 14 2015 Ere Maijala <ere@labs.fi> - 1.11.1-1
- updated for version 1.11.1
* Sat Feb 21 2015 Ere Maijala <ere@labs.fi> - 1.11.0-1
- updated for version 1.11.0
* Sat Jan 10 2015 Ere Maijala <ere@labs.fi> - 1.10.0-1
- updated for version 1.10.0
- added php-mysqli to requirements
* Sat Feb 08 2014 Ere Maijala <ere@labs.fi> - 1.9.0-1
- updated for version 1.9.0
- added lang and select2 directories
* Tue Mar 05 2013 Ere Maijala <ere@labs.fi> - 1.8.0-1
- updated for version 1.8.0
* Wed Feb 13 2013 Ere Maijala <ere@labs.fi> - 1.7.0-1
- updated for version 1.7.0
* Mon Oct 5 2012 Ere Maijala <ere@labs.fi> - 1.6.1-1
- updated for version 1.6.1
* Sat Jul 7 2012 Ere Maijala <ere@labs.fi> - 1.6.0-1
- rebranded and updated for version 1.6.0
* Sat Jun 2 2012 Ere Maijala <ere@labs.fi> - 1.5.3-1
- updated for version 1.5.3
* Wed May 23 2012 Ere Maijala <ere@labs.fi> - 1.5.2-1
- updated for version 1.5.2
* Sun May 20 2012 Ere Maijala <ere@labs.fi> - 1.5.1-1
- updated for version 1.5.1
* Sun Mar 18 2012 Ere Maijala <ere@labs.fi> - 1.5.1-1
- updated for version 1.5.1
* Sun Mar 18 2012 Ere Maijala <ere@labs.fi> - 1.5.0-1
- updated for version 1.5.0
* Wed Jan 11 2012 Ere Maijala <ere@labs.fi> - 1.4.3-1
- updated for version 1.4.3
* Mon Jan 9 2012 Ere Maijala <ere@labs.fi> - 1.4.2-1
- updated for version 1.4.2
- Added php-xml and php-xsl to requirements
* Sat Jan 7 2012 Ere Maijala <ere@labs.fi> - 1.4.1-1
- updated for version 1.4.1
* Sat Dec 3 2011 Ere Maijala <ere@labs.fi> - 1.4.0-1
- updated for version 1.4.0
* Fri Jun 3 2011 Ere Maijala <ere@labs.fi> - 1.3.0-1
- initial spec from Mika Ilmaranta <ilmis@foobar.fi>
