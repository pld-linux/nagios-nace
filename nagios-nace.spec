%include	/usr/lib/rpm/macros.perl
Summary:	Nagios Automated Configuration Engine
Summary(pl):	Nagios Automated Configuration Engine - silnik do automatycznej konfituracji Nagiosa
Name:		nagios-nace
Version:	0.3
Release:	0.4
Epoch:		0
License:	GPL v2
Group:		Applications
Source0:	http://www.adamsinfoserv.com/software/nace-%{version}.tar.gz
# Source0-md5:	be99a13eb5acebc7ee556476d256bbb1
Patch0:		%{name}-perl.patch
URL:		http://www.adamsinfoserv.com/AISTWiki/bin/view/AIS/NACE
BuildRequires:	sed >= 4.0
BuildArch:	noarch
Obsoletes:	nace
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir %{_datadir}/nace

%description
NACE is a generic query engine used to automatically create host and
service definitions for hosts on the network.

It is intended to be used in a shell script at regular intervals by an
experienced Nagios administrator to perform a query against the
supplied host list. It then creates host and service definitions using
the parameters supplied in the query.

%description -l pl
NACE to ogólny silnik odpytuj±cy s³u¿±cy do automatycznego tworzenia
definicji hostów i us³ug dla hostów w sieci.

Jest przeznaczony do u¿ywania jako skrypt powoki w regularnych
odstêpach czasu przez do¶wiadczonego administratora Nagiosa do
sprawdzania podanej listy hostów. Nastêpnie tworzy definicje hostów i
us³ug przy u¿yciu parametrów przekazanych do zapytania.

%prep
%setup -q -n nace-%{version}
%patch0 -p1

#sed -i -e '
#s#DebugMsg \(.*\);#DebugMsg(\1);#g
#' scripts/*.pl 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}/{bin,lib}

cp -a scripts/* $RPM_BUILD_ROOT%{_appdir}/bin
cp -a lib/* $RPM_BUILD_ROOT%{_appdir}/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL README README.old REQUIREMENTS THANKS TODO
%dir %{_appdir}
%dir %{_appdir}/bin
%attr(755,root,root) %{_appdir}/bin/*
%{_appdir}/lib
