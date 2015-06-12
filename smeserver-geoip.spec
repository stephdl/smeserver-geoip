%define name smeserver-geoip
%define version 1.2.0
%define release 1%{?dist}

Summary: SME Server geoip plugin
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Email
Source: %{name}-%{version}.tar.gz
Packager: Doug Kruhm <dakruhm@daknetworks.net>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: perl-Geo-IP
BuildRequires: e-smith-devtools >= 1.13.1-03

%description
The GEOIP plugin lets us know which country our mail server is receiving mail from. If we're receiving too much spam from a particular country, this will help track it down and then use that info to reject connections from that country. This ends up taking the load off our servers.

CHANGE THE CONFIG DB: config setprop qpsmtpd BadCountries <countrycode> (i.e. config setprop qpsmtpd BadCountries BR)
SIGNAL EVENT: signal-event email-update

%changelog
* Fri Jun 12 2015 stephane de Labrusse <stephdl@de-labrusse.fr> 1.2.0-1
- Initial release to sme9

* Mon Sep 03 2012 Doug Kruhm <dakruhm@daknetworks.net> 1.0.5
- defining $country to reduce noise if not found [SME: 5011]
- fixed misspelling in response if country is blocked [SME: 7058]
- cleaning up versioning to MAJOR-MINOR-PATCH

* Fri May 01 2009 Doug Kruhm <dakruhm@daknetworks.net> 1.0.0-04
- added response to connecting server if blocked [SME: 5011]

* Fri May 01 2009 Doug Kruhm <dakruhm@daknetworks.net> 1.0.0-03
- added line to reduce log noise [SME: 5011]

* Fri May 01 2009 Doug Kruhm <dakruhm@daknetworks.net> 1.0.0-02
- db defaults migrated from SPEC file to rpm files [SME: 5193]
- removed %post and %postun macros [SME: 5194]
- added Requires perl-Geo-IP [SME: 1866]
- added e-smith-devtools as a requirement [SME: 1866]

* Thu Jun 16 2007 Doug Kruhm <dakruhm@daknetworks.net>
- 1.0.0-01
- Original version


%prep
%setup

%build


%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
