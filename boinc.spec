Summary:	boinc - a bash script used to manage boinc client
Summary(pl):	boinc - napisany w bashu skrypt do zarządzanie klientem boinc
Name:		boinc
Version:	1.5
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://phileimer.9online.fr/%{name}-%{version}.tar.bz2
# Source0-md5:	24a148365107dae762cbf76bc4cac8b4
# Source0-size:	12859
Patch0:		%{name}-path.patch
URL:		http://phileimer.9online.fr/
Requires:	setiathome
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
boinc is a bash script for unix like systems used to manage client 
of the BOINC project (Berkeley Open Infrastructure for Network 
Computing).

%description -l pl
boinc to napisany w bashu skrypt dla systemów uniksowych służący do
zarządzania klientem projektu BOINC (Berkeley Open Infrastructure for
Network Computing).

%prep
%setup -q
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install boinc $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
